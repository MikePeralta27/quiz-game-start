from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def create_question_bank(data) -> list:
    """Takes a list of dictionaries data and create and return a question object list"""
    question_list = []
    for question in data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_list.append(new_question)
    return question_list


question_bank = create_question_bank(data=question_data)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number}")