from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_pass():
    web_inp = web_field.get()
    mail_inp = mail_field.get()
    pass_inp = pass_field.get()
    txt_file = open("dat.txt", 'a')
    txt_file.write(f"{web_inp} | {mail_inp} | {pass_inp}" + "\n")
    txt_file.close()

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
mail_field.insert(0, "@gmail.com")
mail_field.grid(row=2, column=1, columnspan=2)


pass_lbl = Label()
pass_lbl.config(text="Password: ")
pass_lbl.grid(row=3, column=0)

pass_field = Entry(width=22)
pass_field.grid(row=3, column=1)


gnrt_btn = Button()
gnrt_btn.config(text="Generate Password")
gnrt_btn.grid(row=3, column=2)

add_btn = Button(width=34)
add_btn.config(text="Add", command=add_pass)
add_btn.grid(row=4, column=1, columnspan=2)










window.mainloop()