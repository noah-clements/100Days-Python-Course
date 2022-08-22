from tkinter import *
import random
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")


# Read word file
df = None
try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
finally:
    dict_list = df.to_dict(orient="records")
languages = list(df.columns)
from_lang = languages[0]
to_lang = languages[1]
# print(f"{from_lang} -> {to_lang}")
this_word = {}
# timer = None

# Check answer
def flip_card():
    canvas.itemconfig(bg_img, image=back_img)
    canvas.itemconfig(lang_text, text=to_lang, fill="white")
    canvas.itemconfig(word_text, text=this_word[to_lang], fill="white")

# Next word
def next_card():
    global timer, this_word
    window.after_cancel(timer)
    this_word = random.choice(dict_list)
    quiz_word = this_word[from_lang]
    canvas.itemconfig(bg_img, image=front_img)
    canvas.itemconfig(lang_text, text=from_lang, fill="black")
    canvas.itemconfig(word_text, text=quiz_word, fill="black")
    timer = window.after(3000, func=flip_card)
    # print(timer)

# Know the answer - remove it from quiz words
def known_word():
    dict_list.remove(this_word)
    next_card()


# UI Setup
window = Tk()
window.title("Vocabulary Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
bg_img = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR)
lang_text = canvas.create_text(400, 150, font=LANGUAGE_FONT, text=from_lang, fill="black")
word_text = canvas.create_text(400, 263, font=WORD_FONT, text="", fill="black")
canvas.grid(column=0, row=0, columnspan=2)
# just getting the id here so can use in both check and dk
timer = window.after(3000, func=flip_card)
next_card()

cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_btn.grid(column=0, row=1)

check_img = PhotoImage(file="images/right.png")
known_btn = Button(image=check_img, highlightbackground=BACKGROUND_COLOR, command=known_word)
known_btn.grid(column=1, row=1)

window.mainloop()
# save words to learn
to_learn = pd.DataFrame(dict_list)
to_learn.to_csv("data/words_to_learn.csv", index=False)

