from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    pass_field.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_field.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    web_inp = web_field.get()
    mail_inp = mail_field.get()
    pass_inp = pass_field.get()
    is_ok = True
    data_list = { web_inp: {
        "Mail": mail_inp,
        "Password": pass_inp
    }}

    if web_inp == "" or pass_inp == "" or mail_inp == "@gmail.com":
        messagebox.showerror(title="Empty", message="You left some fields empty")
        is_ok = False

    if is_ok:
        with open("data.json", 'r') as data_file:
            try:
                data = json.load(data_file)
            except:
                with open("data.json", "w") as data_file:
                    json.dump(data_list, data_file, indent=4)
            else:
                data.update(data_list)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
                print("Updated Successfully")
        web_field.delete(0, END)
        mail_field.delete(0, mail_field.index("end") - 17)
        pass_field.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
# window.minsize(width=200, height=200)
window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(height=200, width=200)
gui_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=gui_img)
canvas.grid(row=0, column=1)

web_lbl = Label()
web_lbl.config(text="Website: ")
web_lbl.grid(row=1, column=0)

web_field = Entry(width=40)
web_field.focus()
web_field.grid(row=1, column=1, columnspan=2)


mail_lbl = Label()
mail_lbl.config(text="Email/Username: ")
mail_lbl.grid(row=2, column=0)

mail_field = Entry(width=40)
mail_field.insert(0, "lololol@gmail.com")
mail_field.grid(row=2, column=1, columnspan=2)


pass_lbl = Label()
pass_lbl.config(text="Password: ")
pass_lbl.grid(row=3, column=0)

pass_field = Entry(width=22)
pass_field.grid(row=3, column=1)


gnrt_btn = Button()
gnrt_btn.config(text="Generate Password", command=generate_pass)
gnrt_btn.grid(row=3, column=2)

add_btn = Button(width=34)
add_btn.config(text="Add", command=add_pass)
add_btn.grid(row=4, column=1, columnspan=2)










window.mainloop()