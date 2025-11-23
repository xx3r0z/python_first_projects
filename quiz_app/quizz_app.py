# When working with list, you want tpo put items of similar nature in list, when the items are different, use dictionaries {}

import json

with open('questions.json', 'r') as file:
    content = file.read()
    # This loads it as a string

data = json.loads(content)
# Json to load it as a list

score = 0
for question in data:
    print(question["question_text"])
    for number, objective in enumerate(question["objectives"]):
        print(f"{number + 1}. {objective}")

    answer = int(input("Enter your answer: "))
    subtract = answer - 1
    question["user_response"] = question["objectives"][subtract]

    if answer == question["correct_answer"]:
        score = score + 1
        question["score_emoji"] = "✅"
    else:
        question["score_emoji"] = "❌"

for index, question in enumerate(data):
    message = f"{question['score_emoji']}{index + 1}. Your answer: {question['user_response']}, Correct answer:{question['correct_answer']}"
    print(message)



