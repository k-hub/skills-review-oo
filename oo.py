class Student():
    """Input student first and last names and address."""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question():

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = raw_input(self.question + " > ")

        return answer == self.correct_answer


class Exam():

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        prompt_question = Question(question, correct_answer)
        self.questions.append(question)

    def administer(self):
        score = 0

        for question in self.questions:
            if prompt_question.ask_and_evaluate():  # if True. How do I use a method from a different class?
                score += 1

        return score


def take_test(exam, student_first, student_last, student_address):

    student_exam = Exam(exam)
    exam_score = student_exam.administer()  # Student's score bound to an identifier to use later to set that score as an instance attribute for the student.

    student = Student(student_first, student_last, student_address)
    student.score = exam_score  # Create an instance attribute for student and assign it to the exam score.

def example():

    make_exam = Exam()

    make_exam.add_question(question, correct_answer)

    make_student = Student(student_first, student_last, student_address)

    make_exam.administer()

class Quiz(Exam):

    def administer(self):
        super(Quiz, self).administer(self)
        # Return questions answered correctly / total questions > .5

