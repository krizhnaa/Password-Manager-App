from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
# window.minsize(width=200, height=200)
window.config(padx=20, pady=20)
window.title("Password Manager")

canvas = Canvas(height=200, width=200)
gui_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=gui_img)
canvas.grid(row=0, column=3)



window.mainloop()