from customtkinter import *
import csv
import customtkinter
import tkinter as tk
class main():
    incrimented_Value = 0
    def __init__(self):
        self.root = CTk()
        self.root.title("Welcome to GeekForGeeks")
        self.root.geometry('500x200')
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
            self.top.geometry('350x200')
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
                            self.learner_page = CTkToplevel()
                            self.learner_page.title("Add title")
                            self.learner_page.geometry('600x450')
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
                                marklist = []
                                self.marks_page = CTkToplevel()
                                self.marks_page.title("Marks page")
                                self.marks_page.geometry('600x450')





                                self.lbllearnername = CTkLabel(self.marks_page, text="Enter your learners mark:")
                                self.lbllearnername.grid(row=1, column=0, padx=10, pady=10)
                                self.learner_name = CTkEntry(self.marks_page)
                                self.learner_name.grid(row=1, column=1, padx=10, pady=10)



                                self.label2 = CTkLabel(master=self.marks_page, text="Enter your learners mark", width=300, bg_color="black")
                                self.label2.grid(row=0, column=1, sticky=tk.W + tk.E)


                                marklist[0] = CTkEntry(master=self.marks_page, placeholder_text="VALUE: ")
                                marklist[0].grid(row=0, column=2, sticky=tk.W + tk.E)
                                fieldnames = ['email', 'group', 'learner']
                                with open("learner.csv", encoding="utf8") as f:
                                    csv_reader = csv.DictReader(f, fieldnames)
                                    next(csv_reader)
                                    for line in csv_reader:
                                        if line['email'] == self.email:
                                            #print(f"Your email is {line['email']} and you are in group {line['group']} as a learner.")
                                            # Print the learners related to the logged-in user
                                            #print(f"Learner: {line['learner']}")
                                            def add_Boops():
                                                # Make input_BoX into an array
                                                # Figure out why incrimented_Value no incriement
                                                self.incrimented_Value += 1
                                                self.label2 = CTkLabel(master=self.marks_page, text="PIET 2.0", width=300,
                                                                  bg_color="black")
                                                self.label2.grid(row=self.incrimented_Value, column=1, sticky=tk.W + tk.E)
                                                marklist[self.incrimented_Value] = CTkEntry(master=self.marks_page, placeholder_text="VALUE: ")
                                                marklist[self.incrimented_Value].grid(row=self.incrimented_Value, column=2, sticky=tk.W + tk.E)
                                            add_Boops()

                                def submitmarks():
                                    with open("marks.csv", 'a', newline='') as file:
                                        # Create a CSV writer object
                                        writer = csv.writer(file)
                                        # Iterate over the list and write each row to the CSV file
                                        for row in marklist:
                                            writer.writerow(row)

                                self.btn_view_learners = CTkButton(self.marks_page, text="Marking", fg_color="red", command=submitmarks)
                                self.btn_view_learners.grid(column=2, row=0)
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