import tkinter as tk
import random

class MathGameApp:
    def __init__(self, root, username):
        self.root = root
        self.root.title("Math Game")
        self.root.geometry("400x200")

        self.score = 0
        self.num_questions = 0
        self.max_difficulty = 3  # Set the maximum difficulty level

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0")  # Score label
        self.score_label.pack()  # Pack the score label

        self.difficulty = 1
        self.username = username  # Store the username

        self.generate_question()

    def generate_question(self):
        try:
            if self.difficulty <= self.max_difficulty:
                if self.num_questions < 10:  # Check if the player has answered 10 questions
                    if self.difficulty == 1:
                        num1 = random.randint(1, 10)
                        num2 = random.randint(1, 10)
                    elif self.difficulty == 2:
                        num1 = random.randint(10, 20)
                        num2 = random.randint(1, 10)
                    elif self.difficulty == 3:
                        num1 = random.randint(10, 20)
                        num2 = random.randint(10, 20)

                    if random.choice([True, False]):
                        self.answer = num1 + num2
                        question_text = f"What is {num1} + {num2}?"
                    else:
                        if num1 < num2:
                            num1, num2 = num2, num1
                        self.answer = num1 - num2
                        question_text = f"What is {num1} - {num2}?"

                    self.question_label.config(text=question_text)
                    self.answer_entry.delete(0, "end")
                    self.result_label.config(text="")
                else:
                    # Transition to the next difficulty level or end the game
                    self.num_questions = 0  # Reset the question count
                    self.difficulty += 1  # Increase the difficulty
                    self.generate_question()  # Generate the first question of the new difficulty
            else:
                self.question_label.config(text="Game Completed")
                self.answer_entry.config(state="disabled")
                self.submit_button.config(state="disabled")
        except Exception as e:
            # Handle and display the error
            self.question_label.config(text="An error occurred.")
            print(f"An error occurred: {str(e)}")

    def check_answer(self):
        user_answer = self.answer_entry.get()
        if user_answer.isdigit():
            user_answer = int(user_answer)
            if user_answer == self.answer:
                self.score += 1
                self.result_label.config(text="Correct!", fg="green")
            else:
                self.result_label.config(text="Incorrect. Try again.", fg="red")
        else:
            self.result_label.config(text="Invalid input. Try again.", fg="red")

        self.num_questions += 1

        if self.num_questions < 10:
            self.generate_question()
        else:
            # Transition to the next difficulty level or end the game
            self.num_questions = 0  # Reset the question count
            self.difficulty += 1  # Increase the difficulty
            self.generate_question()  # Generate the first question of the new difficulty

        # Update the score label with the current score
        self.score_label.config(text=f"Score: {self.score}")

def run(username):
    root = tk.Tk()
    app = MathGameApp(root, username)
    root.mainloop()