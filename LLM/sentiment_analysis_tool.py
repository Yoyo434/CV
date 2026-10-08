import random
import re

from huggingface_hub import InferenceClient
from config import HF_API_KEY

MODEL="sentence-transformers/all-MiniLM-L6-v2"
THRESHOLD=0.72
client=InferenceClient(model=MODEL, provider="hf_interface", token=HF_API_KEY)

DEMOS=[
    {"how to delete my account","how do i remove my account"},
    {"start the game","begin the game"},
    {"nearest hospital to me","where is the closest hospital"},
    {"mobile games are getting bigger in size","game size on phone is increasing"},
    {"is it going to rain today","will it rain today"},
    {"reset my password","change my password"},
]

NEGATIONS=[
    {'not','never','no','cannot','don\'t','doesn\'t','isn\'t','wasn\'t','shouldn\'t','wouldn\'t','couldn\'t'},
]

OPPOSITES=[
    {"increase","decrease"},{"bigger","smaller"},{"more","less"},{"add","remove"},{"open","close"},{"enable","disable"},
]

def words(text):
    return re.findall(r"[a-z0-9']+", text.lower())

def adjusted_score(first,second):
    score=client.sentence_similarity(first,[second])[0]
    first_words,second_words=set(words(first)),set(words(second))
    strong_first={word for word in first_words if len(word)>4}
    strong_second={word for word in second_words if len(word)>4}
    shared=strong_first&strong_second
    union=strong_first|strong_second
    overlap=len(shared)/max(1,len(union))

    score+=(0.04 if len(shared)>=2 else 0)
    score+=(0.03 if len(shared)>=0.20 else 0)
    score+=(0.05 if len(shared)>=0.35 else 0)

    numbers_first=set(re.findall(r"\d+(?:\.\d+)?", first))
    numbers_second=set(re.findall(r"\d+(?:\.\d+)?", second))
    if numbers_first and numbers_second and numbers_first!=numbers_second:
        score-=0.1
    if bool(first_words&NEGATIONS)!=bool(second_words&NEGATIONS):
        score-=0.12
    if any((a in first_words and b in second_words) or (b in first_words and a in second_words) for a,b in OPPOSITES):
        score-=0.12

    return max(0.0,min(1.0,score))

def show_result(score):
    label = "✅ DUPLICATE" if score >= THRESHOLD else (
        "🤔 CLOSE MATCH" if score >= THRESHOLD - 0.05 else "❌ DIFFERENT"
    )
    bar = "█" * int(score * 10) + "░" * (10 - int(score * 10))
    print(f"\n🎯 Similarity: {score * 100:.1f}% [{bar}] → {label}")
    print(f"Rule: score ≥ {THRESHOLD} means DUPLICATE")

def compare(first,second,title):
    print(f"\n---{title}---")
    show_result(adjusted_score(first,second))
    print(f"Rule: score ≥ {THRESHOLD} means DUPLICATE")

def main():
    print("Compare two questions. Type 'exit' anytime to quit.\n")
    while True:
        first=input("Question 1:").strip()
        if first.lower()=="exit":
            break
        second=input("Question 2:").strip()
        if second.lower()=="exit":
            break
        if not first or not second:
            print("Please enter both questions.\n")
            continue

        try:
            compare(first,second,"User Input")
            for number,(demo_first,demo_second) in enumerate(random.sample(DEMOS,2),start=1):
                compare(demo_first,demo_second,f"Demo {number}")
        except Exception as error:
            print(f"\nHugging Face inference failed: {error}\n")

if __name__=="__main__":
    main()