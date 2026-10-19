
questions = [
    {
        "question": "Which language is known for its use in AI?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. XML"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["A. Stack", "B. Tree", "C. Queue", "D. Graph"],
        "answer": "C"
    },
    {
        "question": "Which symbol starts a Python comment?",
        "options": ["A. //", "B. #", "C. <!--", "D. **"],
        "answer": "B"
    },
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["A. func", "B. function", "C. def", "D. define"],
        "answer": "C"
    }
]

score = 0

print("===== PYTHON QUIZ GAME =====")

for number, item in enumerate(questions, start=1):
    print(f"\nQ{number}. {item['question']}")
    for option in item["options"]:
        print(option)

    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. Correct answer:", item["answer"])

print("\n===== QUIZ RESULTS =====")
print(f"Score: {score}/{len(questions)}")
print(f"Percentage: {score / len(questions) * 100:.1f}%")
