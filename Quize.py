              
import random

def ask_question(question, options, correct_option, prize):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    player_answer = int(input("Enter the number of your answer: "))
    if player_answer == correct_option:
        print(f"Correct! You won ${prize}\n")
        return prize
    else:
        print("Incorrect! The correct answer was option", correct_option)
        return 0

def quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Paris", "Madrid", "Rome"],
            "correct_option": 2,
            "prize": 100
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Mars", "Venus", "Jupiter", "Saturn"],
            "correct_option": 1,
            "prize": 200
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "correct_option": 2,
            "prize": 300
        },
        # Add more questions as needed
    ]

    total_prize = 0

    random.shuffle(questions)

    for question_data in questions:
        total_prize += ask_question(**question_data)

    print(f"Congratulations! You won a total of ${total_prize}")

if __name__ == "__main__":
    quiz()