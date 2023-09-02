class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def display_question(self):
        current_question = self.questions[self.current_question_index]
        print(current_question.question)
        for i, option in enumerate(current_question.options, start=1):
            print(f"{i}. {option}")

    def get_user_answer(self):
        while True:
            try:
                user_answer = int(input("Enter the number of your answer: "))
                if 1 <= user_answer <= len(self.questions[self.current_question_index].options):
                    return user_answer
                else:
                    print("Invalid input. Please enter a valid option number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def start_quiz(self):
        for question in self.questions:
            self.display_question()
            user_answer = self.get_user_answer()
            if question.is_correct(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print("Incorrect. The correct answer was:", question.options.index(question.correct_answer) + 1)
                print()
            self.current_question_index += 1

    def display_score(self):
        print(f"You scored {self.score}/{len(self.questions)}.")

class Admin:
    def __init__(self):
        self.questions_to_add = []

    def add_question(self, question, options, correct_answer):
        new_question = Question(question, options, correct_answer)
        self.questions_to_add.append(new_question)
        print("Question added successfully!")

    def view_pending_questions(self):
        print("Pending Questions:")
        for index, question in enumerate(self.questions_to_add, start=1):
            print(f"{index}. {question.question}")

    def approve_questions(self):
        approved_questions = self.questions_to_add.copy()
        self.questions_to_add.clear()
        return approved_questions

if __name__ == "__main__":
    admin = Admin()
    user = Quiz()

    while True:
        print("\nSelect User Type:")
        print("1. Admin")
        print("2. User")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Admin Section
            print("\nAdmin Section:")
            while True:
                print("1. Add a Question")
                print("2. View Pending Questions")
                print("3. Approve Questions")
                print("4. Back to Main Menu")
                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    question = input("Enter the question: ")
                    options = input("Enter options separated by commas: ").split(",")
                    correct_answer = input("Enter the correct option: ")
                    admin.add_question(question, options, correct_answer)
                elif admin_choice == "2":
                    admin.view_pending_questions()
                elif admin_choice == "3":
                    approved_questions = admin.approve_questions()
                    for q in approved_questions:
                        user.add_question(q)
                    print("Questions approved and added to the quiz.")
                elif admin_choice == "4":
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")

        elif choice == "2":
            # User Section
            print("\nUser Section:")
            user.start_quiz()
            user.display_score()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
