import random
import re

from huggingface_hub import inferenceClient
from config import HF_API_KEY

MODEL="sentence-transformers/all-MiniLM-L6-v2"
THRESHOLD=0.72
client=inferenceClient(model=MODEL, provider="hf_interface", token=HF_API_KEY)

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
    score=client.sentence_similarity(sentence=first,other_sentence=second)
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

