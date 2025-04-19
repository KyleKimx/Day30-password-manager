from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
global website
global email
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list =[random.choice(letters) for _ in range(nr_letters)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += symbols_list
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += numbers_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_enter.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_enter.get()
    email = email_enter.get()
    password = password_enter.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="field empty")
    else:
        try:
            with open("data.jason", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
                #Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.jason", "w") as data_file:
                #First writing data
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.jason", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
                website_enter.delete(0, END)
                password_enter.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
# HOW CAN I USE VARIABLE FROM OTHER FUNCTION // 3: 30
def find_password():
    website = website_enter.get()
    try:
        with open ("data.jason") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)
w = Canvas(window, width=200, height=200)
w.grid(row=0, column=1)
image = PhotoImage(file="logo.png")
w.create_image(100,100, image=image)

website_title = Label(window, text="Website:")
website_title.grid(row=1, column=0)

website_enter = Entry(width=21)
website_enter.grid(row=1, column=1, columnspan=1)
website_enter.focus()

email_title = Label(window, text="Email/Username:")
email_title.grid(row=2, column=0)

email_enter = Entry(width=35)
email_enter.grid(row=2, column=1, columnspan=2)
email_enter.insert(0, "kyle@gmail.com")

password_title = Label(window, text="Password:")
password_title.grid(row=3, column=0)

password_enter = Entry(width=19)
password_enter.grid(row=3, column=1)

search_button = Button(text="Search", width= 10, command=find_password)
search_button.grid(row=1, column=2)

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)


add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)







window.mainloop()