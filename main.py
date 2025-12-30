

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters=[random.choice(letters) for _ in range(nr_letters)]

    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]
    password_list=password_letters+password_symbols+password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)


    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    text=website_entry.get()
    text2=password_entry.get()
    text1=email_entry.get()
    if len(text)!=0 and len(text2)!=0:
        is_ok=messagebox.askokcancel(title=text, message=f"these are detail entered: \nEmail={text1} \nPasswors={text2}")
        if (is_ok==True):
            with open("data.txt", "a") as f:
                f.write(text+"|"+text1+"|"+text2)
                f.write("\n")
                website_entry.delete(0,END)
                password_entry.delete(0, END)
        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="oops", message="youve missed some info")







# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("password manager")
window.config(padx=20, pady=20)


canvas=Canvas(height=200, width=200,highlightthickness=0)
img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=1, column=1)

label=Label(text="website:", font=("arial", 16,"bold"))
label.grid(row=2,column=0)

label=Label(text="email/username:", font=("arial", 16,"bold"))
label.grid(row=3,column=0)

label=Label(text="password: ", font=("arial", 16,"bold"))
label.grid(row=4,column=0)

email_entry=Entry(width=35)
email_entry.insert(0,"suryaanshpoddar1@gmail.com" )
website_entry=Entry(width=35)
website_entry.grid(row=2, column=1, columnspan=2)
password_entry=Entry(width=21)
email_entry.grid(row=3, column=1, columnspan=2)

password_entry.grid(row=4, column=1)



generate_password_button= Button(text="Generate Password", command=generate)
generate_password_button.grid(row=4, column=2)
add_button=Button(text="add", width =36, command=save)
add_button.grid(row=5, column=1, columnspan=2)












window.mainloop()