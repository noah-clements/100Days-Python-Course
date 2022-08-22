import pandas as pd
import turtle

ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_writer = turtle.Turtle()
state_writer.penup()
state_writer.hideturtle()
state_writer.color("black")

df = pd.read_csv("50_states.csv")
game_is_on = True
guessed_states = []
all_states = df.state.tolist()
title = "Guess the State"   # Starting title
prompt = "Enter a state name."  #Starting prompt

while game_is_on and len(guessed_states) <  50:
    answer_state = screen.textinput(title=title, prompt=prompt)

    if isinstance(answer_state, str):
        answer_state = answer_state.title()
    else:
        game_is_on = False

    if answer_state not in all_states:
        prompt=f"{answer_state} is not a state. Try again."
        continue
    elif answer_state in guessed_states:
        prompt=f"You already guessed {answer_state}. Try again."
        continue
    else:
        guessed_states.append(answer_state)
        title = f"{len(guessed_states)}/50 States Correct"
        prompt = "What's another state name?"

    # lookup the coordinates from the dataframe
    x_cor = int(df[df.state == answer_state].x)
    y_cor = int(df[df.state == answer_state].y)

    state_writer.goto(x_cor, y_cor)
    state_writer.write(answer_state, align=ALIGNMENT, font=FONT)

screen.exitonclick()

# find all missing states and write them to a file
states_to_learn = [state for state in all_states if state not in guessed_states]

learn_df = pd.DataFrame({"state": states_to_learn})
learn_df.to_csv("states_to_learn.csv") 


    # def get_mouse_click_coor(x, y):
    #     print(x, y)
    # turtle.onscreenclick(get_mouse_click_coor)
    # turtle.mainloop()
