from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Times New Roman", 15, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pw_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_let = [random.choice(letters) for _ in range(random.randint(8, 10))]
    pw_sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    pw_num = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = pw_sym + pw_let + pw_num

    random.shuffle(password_list)
    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def proper_len(site, uname, pw):
    if len(site) * len(uname) * len(pw) == 0:
        return False
    else:
        return True


def default_set():
    entry_website.delete(0, END)
    entry_password.delete(0, END)
    entry_website.focus()


def check_data():
    site = entry_website.get().title()
    uname = entry_email_uname.get()
    pw = entry_password.get()
    if proper_len(site, uname, pw):
        is_ok = messagebox.askokcancel(message=f"For the {site} website",
                                       detail=f"These are the details entered: \n"
                                              f"Email: {uname} \nPassword: {pw} \nIs it ok to save?")
        if is_ok:
            new_data = {
                site: {
                    "email": uname,
                    "password": pw,
                }
            }
            try:
                append_data(new_data)
            except FileNotFoundError:
                initiate_data(new_data)
            finally:
                default_set()
    else:
        messagebox.showwarning(message="Oops", detail="Please don't leave any fields empty!")


def initiate_data(new_data):
    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)


def append_data(new_data):
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        data.update(new_data)
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)


# ---------------------- SEARCHING FUNCTIONALITY ------------------------- #
def search_site_info():
    site = entry_website.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        site_info = data[site]
        messagebox.showinfo(message=site, detail=f"Email: {site_info['email']}"
                                                 f"\nPassword: {site_info['password']}")
    except KeyError:
        messagebox.showinfo(message=site, detail="This site hasn't been entered to the system.")
    except FileNotFoundError:
        messagebox.showinfo(message="Error", detail="No Data File Found.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", bg="white", fg="black", font=FONT, takefocus=True)
label_website.grid(column=0, row=1)

entry_website = Entry(bg="white", fg="black", highlightbackground="white", insertbackground="black")
entry_website.grid(column=1, row=1, sticky="EW")
entry_website.focus()

label_email_uname = Label(text="Email/Username:", bg="white", fg="black", font=FONT)
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry(bg="white", fg="black", highlightbackground="white", insertbackground="black")
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_uname.insert(0, "odulsuzkisafilm@gmail.com")

label_password = Label(text="Password:", bg="white", fg="black", font=FONT)
label_password.grid(column=0, row=3)

entry_password = Entry(bg="white", fg="black", highlightbackground="white", insertbackground="black")
entry_password.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password", highlightbackground="white", command=pw_gen)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, highlightbackground="white", command=check_data)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

search = Button(text="Search", highlightbackground="white", command=search_site_info)
search.grid(column=2, row=1, sticky="EW")

window.mainloop()
