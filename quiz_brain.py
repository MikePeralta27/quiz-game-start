class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ")

# TODO: 1. Asking the question


# TODO: 2. Checking if the answer was correct


# TODO: 3. Checking if we're the end of the quiz
