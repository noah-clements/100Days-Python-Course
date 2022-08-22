from flask import Flask
import random
app = Flask(__name__)
number = random.randint(0, 9)

@app.route('/')
def ask_for_guess():
    global number
    number = random.randint(0, 9)
    return '<h1>Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:guess>')
def check_guess(guess):
    if guess < number:
        return '<h1 style="color:red">Too low, try again!</h1>' \
            '<img src="https://media2.giphy.com/media/eJLwreQ3JfIdjWl8lX/100.webp">'
    elif guess > number:
        return '<h1 style="color:purple">Too high, try again!</h1>' \
            '<img src="https://media1.giphy.com/media/hWm5wAsxYdl8N2MlFh/200.webp">'
    else:
        return '<h1 style="color:green">You found me!</h1>' \
            '<img src="https://media1.giphy.com/media/ZaoNH308FHz7a/200.webp">'
    

if __name__ == '__main__':
    app.run(debug=True)