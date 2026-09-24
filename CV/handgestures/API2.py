import requests 
import random
import html

education_category_id=9
api_url="https://opentdb.com/api.php?amount=10&category=17&difficulty=easy&type=multiple"

def get_education_questions():
    response=requests.get(api_url)
    if response.status_code==200:
        data=response.json()
        if data['response_code']==0 and data['results']:
            return data['results']
    return None

def run_quiz():
    questions=get_education_questions()
    if not questions:
        print("No questions available.")
        return
    score=0

    print("welcome to the education quize!\n")

    for i, q in enumerate(questions,1):
        question=html.unescape(q['question'])
        correct=html.unescape(q['correct_answer'])
        incorrect=[html.unescape(a) for a in q['incorrect_answers']]

        options= incorrect + [correct]
        random.shuffle(options)

        print(f"question{i}: {question}")
        for idx, option in enumerate(options,1):
            print(f"{idx}. {option}")

        while True:
            try:
                choice=int(input("Enter your answer (1-4): "))
                if 1<=choice<=4:
                    break
            except ValueError:
                pass
            print("Invalid input. Please enter a number between 1 and 4.")

        if options[choice-1]==correct:
            print("Correct!\n")
            score+=1
        else:
            print(f"Wrong! The correct answer was: {correct}\n")
    print(f"Quiz finished! Your score: {score}/{len(questions)}")
    print(f"percentage: {score/len(questions)*100:.1f}%")

if __name__=="__main__":
    run_quiz()