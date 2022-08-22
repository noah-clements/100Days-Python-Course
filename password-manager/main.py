from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [str(random.randint(0, 9)) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    # print(password)
    pyperclip.copy(password)

    #clear old password
    passwd_input.delete(0, END)
    passwd_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = user_input.get()
    passwd = passwd_input.get()
    new_data = {
        website: {
            "email": email,
            "password": passwd
        }
    }

    # Check to make sure the fields have been filled in
    # MacOS does not honor title for messagebox
    if not len(website) or not len(email) or not len(passwd):
        messagebox.showerror(title="", message="Don't leave any fields empty")
        return

    try:
        with open("data.json","r") as f:
            data = json.load(f)
            data.update(new_data)
    except (FileNotFoundError, json.JSONDecodeError):
        data = new_data
    finally:
        with open("data.json","w") as f:        
            json.dump(data, f, indent=4)
            print(data)

    website_input.delete(0, END)
    passwd_input.delete(0, END)
    website_input.focus()

# ---------------------------- SEARCH FOR SAVED PASSWORD ------------------------------- #
def find_passwd():
    website = website_input.get()
    try:
        with open("data.json","r") as f:
            data = json.load(f)
            login_info = data[website]
    except FileNotFoundError:
        messagebox.showerror(title="", message="No Data File Found")
    except (KeyError, json.JSONDecodeError):
        messagebox.showerror(title="", message="No details for the website exist.")
    else:
        password = login_info['password']
        messagebox.showinfo(title="", message=f"Website: {website}\n" +
                            f"Username/email: {login_info['email']}\n" +
                            f"Password: {password}")
        #clear old password
        passwd_input.delete(0, END)
        passwd_input.insert(0, password)
        pyperclip.copy(password)
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_lbl = Label(text="Website:")
website_lbl.grid(row=1, column=0)
website_input = Entry(width=21)
website_input.grid(row=1, column=1, sticky=EW)
website_input.focus()
search_btn = Button(text="Search", command=find_passwd)
search_btn.grid(row=1, column=2, sticky=EW)

user_lbl = Label(text="Email/Username:")
user_lbl.grid(column=0, row=2)
user_input = Entry(width=35)
user_input.grid(column=1, row=2, columnspan=2, sticky=EW)
user_input.insert(0, "noahclements@gmail.com")

passwd_lbl = Label(text="Password:")
passwd_lbl.grid(column=0, row=3)
passwd_input = Entry(width=21)
passwd_input.grid(column=1, row=3, sticky=W)
passwd_btn = Button(text="Generate Password", command=generate_password)
passwd_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
