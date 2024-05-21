import csv
import re
from tkinter import messagebox
from customtkinter import *
from PIL import ImageTk, Image

class Main:
    def __init__(self):
        self.root = CTk()
        self.root.title("Welcome to Marking Program")
        self.root.geometry('900x600')
        self.root.config(bg="gray")

        # Load and resize image
        self.image = Image.open("MARKOHOLIC.jpg")
        self.image = self.image.resize((300, 250))
        self.photo = ImageTk.PhotoImage(self.image)

        # Frame setup
        self.current_frame = None
        self.setup_initial_screen()

        self.root.mainloop()

    def clear_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

    def setup_initial_screen(self):
        self.clear_frame()
        self.current_frame = CTkFrame(master=self.root, fg_color="gray")
        self.current_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Canvas for image
        self.canvas = CTkCanvas(self.current_frame, width=self.image.width, height=self.image.height, bg="gray", highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2, pady=10)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)

        # Signup entries
        self.email_signup = CTkEntry(self.current_frame, bg_color="white")
        self.password_signup1 = CTkEntry(self.current_frame, show="*", bg_color="white")
        self.password_signup2 = CTkEntry(self.current_frame, show="*", bg_color="white")

        # Signup labels
        self.lblemail = CTkLabel(self.current_frame, text="Enter your email:", bg_color="gray")
        self.lblupassword = CTkLabel(self.current_frame, text="Enter your password:", bg_color="gray")
        self.lblupassword2 = CTkLabel(self.current_frame, text="Confirm your password:", bg_color="gray")

        # Positioning signup fields
        self.lblemail.grid(row=1, column=0, padx=10, pady=10)
        self.email_signup.grid(row=1, column=1, padx=10, pady=10)
        self.lblupassword.grid(row=2, column=0, padx=10, pady=10)
        self.password_signup1.grid(row=2, column=1, padx=10, pady=10)
        self.lblupassword2.grid(row=3, column=0, padx=10, pady=10)
        self.password_signup2.grid(row=3, column=1, padx=10, pady=10)

        # Register and Login buttons
        self.btn_register = CTkButton(self.current_frame, text="Register", fg_color="red", command=self.register)
        self.btn_register.grid(column=0, row=4, pady=10)
        self.btn_account = CTkButton(self.current_frame, text="Already have an account?", command=self.loggedin, bg_color="gray")
        self.btn_account.grid(column=1, row=4, pady=10)

    def loggedin(self):
        self.clear_frame()
        self.current_frame = CTkFrame(master=self.root, fg_color="gray")
        self.current_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.setup_image(self.current_frame)

        self.lblemaillog = CTkLabel(self.current_frame, text="Enter your email:", bg_color="gray")
        self.lblupasswordlog = CTkLabel(self.current_frame, text="Enter your password:", bg_color="gray")

        self.email_login = CTkEntry(self.current_frame, bg_color="white")
        self.password_login = CTkEntry(self.current_frame, show="*", bg_color="white")

        self.lblemaillog.grid(row=1, column=0, padx=10, pady=10)
        self.email_login.grid(row=1, column=1, padx=10, pady=10)
        self.lblupasswordlog.grid(row=2, column=0, padx=10, pady=10)
        self.password_login.grid(row=2, column=1, padx=10, pady=10)

        self.btnlog = CTkButton(self.current_frame, text="Login", fg_color="red", command=self.login)
        self.btnlog.grid(column=0, row=3, columnspan=2, pady=10)

    def setup_image(self, frame):
        canvas = CTkCanvas(frame, width=self.image.width, height=self.image.height, bg="gray", highlightthickness=0)
        canvas.grid(row=0, column=0, columnspan=2, pady=10)
        canvas.create_image(0, 0, anchor="nw", image=self.photo)

    def login(self):
        email = self.email_login.get()
        password = self.password_login.get()
        with open("users.csv", mode="r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                if row == [email, password]:
                    print("You logged in!")
                    self.email = email
                    self.mainmenu()
                    return True
        messagebox.showerror("Error", "Please enter a valid email address.")
        print("Please try again")
        return False

    def register(self):
        email = self.email_signup.get()
        password = self.password_signup1.get()
        password2 = self.password_signup2.get()

        if not re.match(r"[^@]+@gmail\.com", email):
            messagebox.showerror("Error", "Please enter a valid Gmail address.")
            return

        if password == password2:
            with open("users.csv", mode="a", newline="") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerow([email, password])
                print("Registration is successful!")
                self.loggedin()
        else:
            messagebox.showerror("Error", "Passwords do not match")

    def mainmenu(self):
        self.clear_frame()
        self.current_frame = CTkFrame(master=self.root, fg_color="gray")
        self.current_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.setup_image(self.current_frame)

        self.lbl_welcome = CTkLabel(self.current_frame, text="WELCOME TO THE MARKOHOLIC GRADING SYSTEM", bg_color="gray")
        self.lbl_welcome.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.btn_add_group = CTkButton(self.current_frame, text="Add group", fg_color="red", command=self.addgroupmenu)
        self.btn_view_groups = CTkButton(self.current_frame, text="View groups", fg_color="red", command=self.view_groups)

        self.btn_add_group.grid(column=0, row=1, pady=10)
        self.btn_view_groups.grid(column=1, row=1, pady=10)

    def load_groups(self):
        with open('groups.csv', 'r') as file:
            reader = csv.reader(file)
            groups = [row[1] for row in reader if row[0] == self.email]
        return groups

    def view_group_marks(self, group):
        def calculate_learner_average(learner_marks):
            total_marks = sum(learner_marks)
            num_subjects = len(learner_marks)
            return total_marks / num_subjects if num_subjects > 0 else 0

        def calculate_group_average(group_marks):
            total_marks = sum(sum(marks) for marks in group_marks.values())
            num_learners = sum(len(marks) for marks in group_marks.values())
            return total_marks / num_learners if num_learners > 0 else 0

        def display_marks():
            # Read marks from marks.csv
            with open('marks.csv', 'r') as file:
                reader = csv.reader(file)
                marks_data = [row for row in reader if row[1] == group]

            learner_marks = {}
            for row in marks_data:
                learner = row[2]
                if learner not in learner_marks:
                    learner_marks[learner] = [int(row[i]) for i in range(3, len(row))]
                else:
                    learner_marks[learner].extend([int(row[i]) for i in range(3, len(row))])

            self.clear_frame()
            self.current_frame = CTkFrame(master=self.root, fg_color="gray")
            self.current_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

            lbl_group = CTkLabel(self.current_frame, text=f"Group: {group}", bg_color="gray")
            lbl_group.grid(row=0, column=0, padx=10, pady=10)

            # Display learner marks
            row_index = 1
            for learner, marks in learner_marks.items():
                CTkLabel(self.current_frame, text=learner, bg_color="gray").grid(row=row_index, column=0, padx=10, pady=5)
                for i, mark in enumerate(marks):
                    CTkLabel(self.current_frame, text=mark, bg_color="gray").grid(row=row_index, column=i+1, padx=10, pady=5)
                average_mark = calculate_learner_average(marks)
                CTkLabel(self.current_frame, text=f"{average_mark:.2f}", bg_color="gray").grid(row=row_index, column=len(marks)+1, padx=10, pady=5)
                row_index += 1

            # Calculate and display group average
            group_average = calculate_group_average(learner_marks.values())
            CTkLabel(self.current_frame, text="Group Average", bg_color="gray").grid(row=row_index, column=0, padx=10, pady=5)
            CTkLabel(self.current_frame, text=f"{group_average:.2f}", bg_color="gray").grid(row=row_index, column=1, padx=10, pady=5)

        display_marks()

    def view_groups(self):
        self.clear_frame()
        self.current_frame = CTkFrame(master=self.root, fg_color="gray")
        self.current_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.setup_image(self.current_frame)

        groups = self.load_groups()
        for i, g in enumerate(groups):
            lbl_group = CTkLabel(self.current_frame, text=g, bg_color="gray")
            lbl_group.grid(row=i, column=0, padx=10, pady=10)
            btn_view_marks = CTkButton(self.current_frame, text="View Marks", fg_color="red", command=lambda group=g: self.view_group_marks(group))
            btn_view_marks.grid(row=i, column=1, padx=10, pady=10)

    def addgroupmenu(self):
        self.clear_frame()
        self.current_frame = CTkFrame(master=self.root, fg_color="gray")
        self.current_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.setup_image(self.current_frame)

        self.group_name = CTkEntry(self.current_frame, bg_color="white")
        self.lblgroup = CTkLabel(self.current_frame, text="Enter the group name:", bg_color="gray")
        self.lblgroup.grid(row=0, column=0, padx=10, pady=10)
        self.group_name.grid(row=0, column=1, padx=10, pady=10)

        self.btn_group = CTkButton(self.current_frame, text="Add Group", fg_color="red", command=self.addgroup)
        self.btn_group.grid(row=1, column=0, columnspan=2, pady=10)

    def addgroup(self):
        group = self.group_name.get()
        with open("groups.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([self.email, group])
            print("Group added successfully!")

        self.addlearner_menu(group)

    def addlearner_menu(self, group):
        self.clear_frame()
        self.current_frame = CTkFrame(master=self.root, fg_color="gray")
        self.current_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.setup_image(self.current_frame)

        self.learner_name = CTkEntry(self.current_frame, bg_color="white")
        lbl_learner = CTkLabel(self.current_frame, text="Enter the learner's name:", bg_color="gray")
        lbl_learner.grid(row=0, column=0, padx=10, pady=10)
        self.learner_name.grid(row=0, column=1, padx=10, pady=10)

        btn_add_learner = CTkButton(self.current_frame, text="Add learner", fg_color="red", command=lambda: self.addlearner(group))
        btn_add_learner.grid(row=1, column=0, columnspan=2, pady=10)

        btn_view_learners = CTkButton(self.current_frame, text="View learners", fg_color="red", command=lambda: self.addmarks(group))
        btn_view_learners.grid(row=2, column=0, columnspan=2, pady=10)

    def addlearner(self, group):
        learner = self.learner_name.get()
        with open("learner.csv", mode="a", newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow([self.email, group, learner])
            self.learner_name.delete(0, END)
            print("Learner added successfully!")

    def addmarks(self, group):
        def submit_marks():
            marks = [[entry.get() for entry in subject_entries] for subject_entries in marks_entries]
            with open('marks.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                for i, name in enumerate(learner_names):
                    writer.writerow([self.email, group, name] + marks[i])
            messagebox.showinfo("Marks info:", "MARKS SUBMITTED")
            self.view_groups()

        def create_text_boxes():
            marks_entries = []
            subjects = ["Mathematics", "English", "Afrikaans", "Geography", "Biology"]
            for i, name in enumerate(learner_names):
                lbl_name = CTkLabel(tmp_Frame, text=name, bg_color="gray")
                lbl_name.grid(row=i + 1, column=0, padx=10, pady=10)
                entries = []
                for j, subject in enumerate(subjects):
                    entry = CTkEntry(tmp_Frame, bg_color="white")
                    entry.insert(0, subject)  # Insert subject hint as placeholder text
                    entry.bind("<FocusIn>", lambda e, placeholder=subject: self.clear_placeholder(e, placeholder))  # Clear placeholder on focus
                    entry.bind("<FocusOut>", lambda e, placeholder=subject: self.restore_placeholder(e, placeholder))  # Restore placeholder on focus out
                    entry.grid(row=i + 1, column=j * 2 + 1, padx=10, pady=10)
                    entries.append(entry)
                marks_entries.append(entries)
            return marks_entries

        def filter_learner_data(email, group):
            with open('learner.csv', 'r') as file:
                reader = csv.reader(file)
                learner_data = [row for row in reader if row[0] == email and row[1] == group]
            return learner_data

        learner_data = filter_learner_data(self.email, group)
        learner_names = [row[2] for row in learner_data]

        self.clear_frame()
        self.current_frame = CTkFrame(master=self.root, fg_color="gray")
        self.current_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        tmp_Frame = CTkFrame(master=self.current_frame, fg_color="gray")
        tmp_Frame.grid(row=0, column=0, padx=10, pady=10)

        marks_entries = create_text_boxes()

        self.submit_button = CTkButton(tmp_Frame, text="Submit Marks", command=submit_marks)
        self.submit_button.grid(row=len(learner_names) + 1, column=0, columnspan=6, pady=10)

        btn_view_groups = CTkButton(tmp_Frame, text="View groups", fg_color="red", command=self.view_groups)
        btn_view_groups.grid(row=len(learner_names) + 2, column=0, columnspan=6, pady=10)

    def clear_placeholder(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, "end")
            event.widget.config(fg_color="black")

    def restore_placeholder(self, event, placeholder):
        if event.widget.get() == "":
            event.widget.insert(0, placeholder)
            event.widget.config(fg_color="gray")

Main()