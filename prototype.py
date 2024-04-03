import csv
from tkinter import *





root = Tk()
root.title("Welcome to GeekForGeeks")
root.geometry('350x200')


email_signup = Entry(root)
password_signup1 = Entry(root)
password_signup2 = Entry(root)
email_signup.grid(row=1, column=1, padx=10, pady=10)
password_signup1.grid(row=2, column=1, padx=10, pady=10)
password_signup2.grid(row=3, column=1, padx=10, pady=10)



lblemail = Label(root, text="Enter your email:")
lblemail.grid(row = 1, column = 0, padx = 10, pady = 10)

lblupassword = Label(root, text="Enter your password:")
lblupassword.grid(row = 2, column = 0, padx = 10, pady = 10)

lblupassword2 = Label(root, text="Enter your password:")
lblupassword2.grid(row = 3, column = 0, padx = 10, pady = 10)

def register():
    with open("users.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        email = email_signup.get()
        password = password_signup1.get()
        password2 = password_signup2.get()
        if password == password2:
            writer.writerow([email, password])
            print("Registration is successful!")
            loggedin()
        else:
            print("Please try again")


def loggedin():
    top = Toplevel()
    top.title("Log in")
    top.geometry('350x200')

    lblemaillog = Label(top, text="Enter your email:")
    lblemaillog.grid(row=1, column=0, padx=10, pady=10)

    lblupasswordlog = Label(top, text="Enter your password:")
    lblupasswordlog.grid(row=2, column=0, padx=10, pady=10)
    global email_login
    global password_login

    email_login = Entry(top)

    password_login = Entry(top)
    email_login.grid(row=1, column=1, padx=10, pady=10)
    password_login.grid(row=2, column=1, padx=10, pady=10)

    def login():
        email = email_login.get()
        password = password_login.get()
        with open("users.csv", mode="r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if row == [email, password]:
                    print("You logged in!")
                    return True
        print("Please try again")
        return False

    btnlog = Button(top, text="Click me", fg="red", command=login)
    # set Button grid
    btnlog.grid(column=1, row=0)
    root.withdraw()



# function to display text when
# button is clicked





# button widget with red color text
# inside
btn = Button(root, text="Click me", fg="red", command=register)
# set Button grid
btn.grid(column=1, row=0)




# Execute Tkinter

root.mainloop()





register()
login()



