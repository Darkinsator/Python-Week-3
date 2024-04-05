from customtkinter import *
import csv
import customtkinter
import tkinter as tk
class main():
    incrimented_Value = 0
    def __init__(self):
        self.root = CTk()
        self.root.title("Welcome to GeekForGeeks")
        self.root.geometry('600x450')
        self.email_signup = CTkEntry(self.root)
        self.password_signup1 = CTkEntry(self.root)
        self.password_signup2 = CTkEntry(self.root)
        self.email_signup.grid(row=1, column=1, padx=10, pady=10)
        self.password_signup1.grid(row=2, column=1, padx=10, pady=10)
        self.password_signup2.grid(row=3, column=1, padx=10, pady=10)

        self.lblemail = CTkLabel(self.root, text="Enter your email:")
        self.lblemail.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.lblupassword = CTkLabel(self.root, text="Enter your password:")
        self.lblupassword.grid(row = 2, column = 0, padx = 10, pady = 10)
        self.lblupassword2 = CTkLabel(self.root, text="Enter your password:")
        self.lblupassword2.grid(row = 3, column = 0, padx = 10, pady = 10)

        def loggedin():
            self.top = CTkToplevel()
            self.top.title("Log in")
            self.top.geometry('600x450')
            self.lblemaillog = CTkLabel(self.top, text="Enter your email:")
            self.lblemaillog.grid(row=1, column=0, padx=10, pady=10)
            self.lblupasswordlog = CTkLabel(self.top, text="Enter your password:")
            self.lblupasswordlog.grid(row=2, column=0, padx=10, pady=10)
            global email_login
            global password_login
            self.email_login = CTkEntry(self.top)
            self.password_login = CTkEntry(self.top)
            self.email_login.grid(row=1, column=1, padx=10, pady=10)
            self.password_login.grid(row=2, column=1, padx=10, pady=10)
            def login():
                global email
                self.email = self.email_login.get()
                self.password = self.password_login.get()
                with open("users.csv", mode="r") as f:
                    reader = csv.reader(f, delimiter=",")
                    for row in reader:
                        if row == [self.email, self.password]:
                            print("You logged in!")
                            mainmenu()
                            return True
                print("Please try again")
                return False
            self.btnlog = CTkButton(self.top, text="Click me", fg_color="red", command=login)
            # set Button grid
            self.btnlog.grid(column=1, row=0)
            self.root.withdraw()

        def register():
            with open("users.csv", mode="a", newline="") as f:
                writer = csv.writer(f, delimiter=",")
                self.email = self.email_signup.get()
                self.password = self.password_signup1.get()
                self.password2 = self.password_signup2.get()
                if self.password == self.password2:
                    writer.writerow([self.email, self.password])
                    print("Registration is successful!")
                    loggedin()
                else:
                    print("Please try again")

        btn = CTkButton(self.root, text="Click me", fg_color="red", command=register)
        # set Button grid
        btn.grid(column=1, row=4)
        btn_account = CTkButton(self.root, text="Already have an account?", command=loggedin)
        btn_account.grid(column=2, row=4)

        def mainmenu():
            self.menu = CTkToplevel()
            self.menu.title("Main menu")
            self.menu.geometry('600x450')
            def addgroupmenu():
                self.addgroups = CTkToplevel()
                self.addgroups.title("Add Group")
                self.addgroups.geometry('600x450')
                self.lblgroupname = CTkLabel(self.addgroups, text="Enter your groups name:")
                self.lblgroupname.grid(row=1, column=0, padx=10, pady=10)
                self.group_name = CTkEntry(self.addgroups)
                self.group_name.grid(row=1, column=1, padx=10, pady=10)
                def addgroup():
                    with open("groups.csv", mode="a", newline="") as f:
                        writer = csv.writer(f, delimiter=",")
                        global group
                        self.group = self.group_name.get()
                        writer.writerow([self.email, self.group])
                        print("Group added successfully!")
                        def addlearners():

                            self.lbllearnername = CTkLabel(self.addgroups, text="Enter your learner name:")
                            self.lbllearnername.grid(row=1, column=0, padx=10, pady=10)
                            self.learner_name = CTkEntry(self.addgroups)
                            self.learner_name.grid(row=1, column=1, padx=10, pady=10)
                            def addlearner():
                                with open("learner.csv", mode="a", newline="") as f:
                                    writer = csv.writer(f, delimiter=",")
                                    global learner
                                    self.learner = self.learner_name.get()
                                    writer.writerow([self.email, self.group, self.learner])
                                    self.learner_name.delete(0, END)
                                    print("learner added successfully!")
                            def addmarks():
                                def submit_marks():
                                    # Get marks input and learner names
                                    marks = [entry.get() for entry in marks_entries]


                                    # Write marks to marks.csv
                                    with open('marks.csv', 'a', newline='') as file:
                                        writer = csv.writer(file)
                                        for name, mark in zip(learner_names, marks):
                                            writer.writerow([self.email, self.group, name, mark])

                                def create_text_boxes():
                                    global marks_entries
                                    marks_entries = []
                                    for i, name in enumerate(learner_names):

                                        tk.Label(self.addmarks, text=name).grid(row=i + 1, column=0)
                                        self.entry = CTkEntry(self.addmarks)
                                        self.entry.grid(row=i + 1, column=1)
                                        marks_entries.append(self.entry)

                                def filter_learner_data(email, group):
                                    with open('learner.csv', 'r') as file:
                                        reader = csv.reader(file)
                                        learner_data = [row for row in reader if row[0] == email and row[1] == group]
                                    return learner_data

                                # Get email and group of the current user (example values)
                                current_user_email = self.email
                                current_user_group = self.group

                                # Filter learner data based on user email and group
                                learner_data = filter_learner_data(current_user_email, current_user_group)




                                # Tkinter setup
                                self.addmarks = CTkToplevel()
                                self.addmarks.title("Add Marks")
                                self.addmarks.geometry('600x450')

                                # Create text boxes for marks

                                learner_names = [row[2] for row in learner_data]
                                create_text_boxes()

                                # Submit button
                                self.submit_button = CTkButton(self.addmarks, text="Submit Marks", command=submit_marks)
                                self.submit_button.grid(row=len(learner_names) + 1, column=0, columnspan=2)

                            self.btn_submit_learner = CTkButton(self.addgroups, text="Add learner", fg_color="red", command=addlearner)
                            self.btn_submit_learner.grid(column=1, row=0)

                            self.btn_view_learners = CTkButton(self.addgroups, text="View learners", fg_color="red", command=addmarks)
                            self.btn_view_learners.grid(column=2, row=0)

                        addlearners()
                self.btn_submit_group = CTkButton(self.addgroups, text="Add group", fg_color="red", command=addgroup)
                self.btn_submit_group.grid(column=1, row=0)
            self.btn_group_choose = CTkButton(self.menu, text="Add group", fg_color="red", command=addgroupmenu)
            self.btn_group_choose.grid(column=1, row=0)
            #btn_group_existing = Button(menu, text="Choose existing group", fg="red", command=choosegroupmenu)
            #btn_group_existing.grid(column=1, row=0)
        #Execute Tkinter
        self.root.mainloop()
main()