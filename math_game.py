import tkinter as tk
import random

class MathGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Game")
        self.root.geometry("400x200")

        self.score = 0
        self.num_questions = 0

        self.question_label = tk.Label(root, text="")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.generate_question()

    def generate_question(self):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

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
        self.update_score()

        if self.num_questions < 10:
            self.generate_question()
        else:
            self.question_label.config(text="Game Over")
            self.answer_entry.config(state="disabled")
            self.submit_button.config(state="disabled")

    def update_score(self):
        self.root.title(f"Math Game - Score: {self.score}/{self.num_questions}")

def run():
    root = tk.Tk()
    app = MathGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    run()
