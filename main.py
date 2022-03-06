from question_model import Question
from data import question_data
import quiz_brain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

# print(question_bank)
qb = quiz_brain.QuizBrain(question_bank)

while qb.still_has_questions():
    qb.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {qb.score}/{qb.question_number}")