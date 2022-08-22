from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain) -> None:
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(background=THEME_COLOR, foreground="white")
        self.score_label.grid(column=1, row=0)
        self.score_label.config(text="Score: 0")

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text", 
                                                     font=FONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightbackground=THEME_COLOR, 
                               command=self.check_if_true)
        self.true_btn.grid(column=0, row=2)
    
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightbackground=THEME_COLOR,
                                command=self.check_if_false)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.button_enable()
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, 
                                   text="You've completed the quiz.\n" +
                                    f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")

    def check_if_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_if_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        self.button_disable()
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.window.after(2000, self.get_next_question)

    def button_enable(self):
        self.true_btn.config(state="normal")
        self.false_btn.config(state="normal")
     
    def button_disable(self):
        self.true_btn.config(state="disabled")
        self.false_btn.config(state="disabled")
     
    # def do_nothing(self):
    #     pass
        