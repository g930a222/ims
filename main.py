import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from student_master import StudentMaster
from imsgkc.employee_master import EmployeeMaster
from imsgkc.course_master import CourseMaster
from imsgkc.batch_master import BatchMaster
from imsgkc.fees_receipt import FeesReceipt
import mysql.connector
import string
import secrets

# Sample user credentials and roles (username: (password, role))
USER_DATA = {
    "admin": ("admin123", "admin"),
    "user1": ("password1", "user1"),
    "user2": ("password2", "user2")
}
# Define roles and their corresponding permissions
ROLES = {
    "admin": ["view_dashboard", "manage_students", "manage_employees", "manage_courses", "manage_batches",
              "manage_fees"],
    "user1": ["view_dashboard"]  # Add or update roles here
}


class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("600x400")

        # Load and resize background image
        bg_image = Image.open("../images/bg.jpeg").resize((600, 500))
        self.bg_image = ImageTk.PhotoImage(bg_image)

        # Calculate the x and y coordinates to center the window
        x = (master.winfo_screenwidth() - 600) // 2
        y = (master.winfo_screenheight() - 500) // 2
        self.master.geometry(f"+{x}+{y}")

        # Place the background image on the login window
        bg_label = tk.Label(master, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Username label and entry with user icon
        self.user_icon = ImageTk.PhotoImage(Image.open("../images/user.png").resize((20, 20)))
        self.username_label = tk.Label(master, text="Username:", bg="white", image=self.user_icon, compound="left")
        self.username_label.place(relx=0.5, rely=0.4, anchor="center")
        self.username_entry = tk.Entry(master)
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")

        # Password label and entry with password icon
        self.password_icon = ImageTk.PhotoImage(Image.open("../images/password.png").resize((20, 20)))
        self.password_label = tk.Label(master, text="Password:", bg="white", image=self.password_icon, compound="left")
        self.password_label.place(relx=0.5, rely=0.55, anchor="center")
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.place(relx=0.5, rely=0.6, anchor="center")

        # Login button with login icon
        self.login_icon = ImageTk.PhotoImage(Image.open("../images/login.png").resize((15, 15)))
        self.login_button = tk.Button(master, text="Login", command=self.login, bg="white", image=self.login_icon,
                                      compound="left")
        self.login_button.place(relx=0.5, rely=0.7, anchor="center")

        self.reset_icon = ImageTk.PhotoImage(Image.open("../images/reset_icon.png").resize((15, 15)))
        self.reset_button = tk.Button(master, text="Reset Password", command=self.open_reset_password_window,
                                      bg="white", image=self.reset_icon, compound="left")
        self.reset_button.place(relx=0.5, rely=0.77, anchor="center")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in USER_DATA:
            stored_password, role = USER_DATA[username]
            if password == stored_password:
                self.master.destroy()
                Dashboard(username, role)
            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            messagebox.showerror("Error", "User not found")

    def generate_new_password(self, length=8):
        alphabet = string.ascii_letters + string.digits
        new_password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return new_password

    def reset_password(self):
        username = self.username_entry.get()

        if username in USER_DATA:
            new_password = self.generate_new_password()
            USER_DATA[username] = (new_password, USER_DATA[username][1])
            messagebox.showinfo("Password Reset", f"New password for {username}: {new_password}")
        else:
            messagebox.showerror("Error", "User not found")

    def open_reset_password_window(self):
        self.new_win = tk.Toplevel(self.master)
        self.new_obj = ResetPasswordWindow(self.new_win, self.generate_new_password())


class Dashboard:
    def __init__(self, username, role):
        self.root = tk.Tk()
        self.root.title("Dashboard")
        IMS(self.root, username, role)
        self.root.mainloop()


class IMS:
    def __init__(self, master, username, role):
        self.master = master
        self.master.geometry('1360x700+0+0')
        self.master.title("INSTITUTE MANAGEMENT SYSTEM")

        # ======title=====
        title = tk.Label(master, text="Institute management system", font=("goudy old style ", 30, "bold"),
                         bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1)

        # ==========Menu frame ====
        M_frame = tk.LabelFrame(master, text="Menus", font=("goudy old style ", 15), bg="brown")
        M_frame.place(x=10, y=70, width=1355, height=540)
        if "manage_password" in ROLES[role]:
            self.create_button_with_label(M_frame, "Reset Password", self.password_img, "Reset Your Password",
                                          self.open_reset_password_window, x=900, y=210)

        # Load icon images
        student_img = Image.open("../images/student_icon.png").resize((100, 100))
        self.student_img = ImageTk.PhotoImage(student_img)
        employee_img = Image.open("../images/employee_icon.png").resize((100, 100))
        self.employee_img = ImageTk.PhotoImage(employee_img)
        course_img = Image.open("../images/course_icon.png").resize((100, 100))
        self.course_img = ImageTk.PhotoImage(course_img)
        batch_img = Image.open("../images/batch_icon.png").resize((100, 100))
        self.batch_img = ImageTk.PhotoImage(batch_img)
        fees_img = Image.open("../images/fees.png").resize((100, 100))
        self.fees_img = ImageTk.PhotoImage(fees_img)
        logout_img = Image.open("../images/logout.png").resize((30, 30))
        self.logout_img = ImageTk.PhotoImage(logout_img)
        exit_img = Image.open("../images/exit_png.png").resize((20, 20))
        self.exit_img = ImageTk.PhotoImage(exit_img)

        # Create buttons with labels based on user's role
        self.create_button_with_label(M_frame, "Students", self.student_img, "Total Students: \n[0]",
                                       self.open_student_window, x=20, y=5)
        if "manage_employees" in ROLES[role]:
            self.create_button_with_label(M_frame, "Employee", self.employee_img, "Total Employees: \n[0]",
                                           self.open_employee_window, x=240, y=5)
        if "manage_courses" in ROLES[role]:
            self.create_button_with_label(M_frame, "Course", self.course_img, "Total Courses: \n[0]",
                                           self.open_course_window, x=460, y=5)
        if "manage_batches" in ROLES[role]:
            self.create_button_with_label(M_frame, "Batch", self.batch_img, "Total Batches: \n[0]",
                                          self.open_batch_window, x=680, y=5)
            # Create label objects for counts
            self.student_label = tk.Label(M_frame, text="Total Students:", font=("goudy old style ", 12), bg="white")
            self.student_label.place(x=20, y=205, width=200, height=40)

            self.employee_label = tk.Label(M_frame, text="Total Employees:", font=("goudy old style ", 12), bg="white")
            self.employee_label.place(x=240, y=205, width=200, height=40)

            self.course_label = tk.Label(M_frame, text="Total Courses:", font=("goudy old style ", 12), bg="white")
            self.course_label.place(x=460, y=205, width=200, height=40)

            self.batch_label = tk.Label(M_frame, text="Total Batches:", font=("goudy old style ", 12), bg="white")
            self.batch_label.place(x=680, y=205, width=200, height=40)
        # ======= fees button======
        self.btn_fees = tk.Button(M_frame, text="Fees", image=self.fees_img, compound=tk.TOP,
                                  font=("goudy old style ", 15, "bold"),
                                  bg="#0b5377", fg="white", cursor="hand2", command=self.open_fees_window)
        self.btn_fees.place(x=900, y=5, width=200, height=200)

        # Logout button
        btn_logout = tk.Button(M_frame, text="Logout", image=self.logout_img, compound=tk.TOP,
                               font=("goudy old style ", 15, "bold"),
                               bg="#0b5377", fg="white", cursor="hand2", command=self.logout)
        btn_logout.place(x=1120, y=5, width=100, height=100)

        # Exit button
        btn_exit = tk.Button(M_frame, text="Exit", image=self.exit_img, compound=tk.TOP,
                             font=("goudy old style ", 15, "bold"),
                             bg="#0b5377", fg="white", cursor="hand2", command=self.exit_application)
        btn_exit.place(x=1120, y=108, width=100, height=100)
        # =======footer=====
        footer = tk.Label(master, text=" IMS--Institute management system  \n Contact :9022286039",
                          font=("goudy old style ", 15, "bold"),
                          bg="#033054", fg="white")
        footer.pack(side=tk.BOTTOM, fill=tk.X)


        self.fetch_and_update_counts()
        # Update details
        self.fetch_counts()

    def create_button_with_label(self, frame, text, image, label_text, command, x, y):
        button = tk.Button(frame, text=text, image=image, compound=tk.TOP, font=("goudy old style ", 15, "bold"),
                           bg="#0b5377", fg="white", cursor="hand2", command=command)
        button.place(x=x, y=y, width=200, height=200)

        label = tk.Label(frame, text=label_text, font=("goudy old style ", 12), bg="white")
        label.place(x=x, y=y + 200, width=200, height=40)

    def open_student_window(self):
        self.new_win = tk.Toplevel(self.master)
        self.new_obj = StudentMaster(self.new_win)

    def open_employee_window(self):
        self.new_win = tk.Toplevel(self.master)
        self.new_obj = EmployeeMaster(self.new_win)

    def open_batch_window(self):
        self.new_win = tk.Toplevel(self.master)
        self.new_obj = BatchMaster(self.new_win)

    def open_course_window(self):
        self.new_win = tk.Toplevel(self.master)
        self.new_obj = CourseMaster(self.new_win)

    def open_fees_window(self):
        self.new_win = tk.Toplevel(self.master)
        self.new_obj = FeesReceipt(self.new_win)

    def fetch_and_update_counts(self):
        # Fetch counts from the database
        counts = self.fetch_counts()
        if counts:
            self.student_label.config(text=f"Total Students: {counts['students']}")
            self.employee_label.config(text=f"Total Employees: {counts['employees']}")
            self.course_label.config(text=f"Total Courses: {counts['courses']}")
            self.batch_label.config(text=f"Total Batches: {counts['batches']}")

    def fetch_counts(self):
        try:
            # Connect to the database
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()

            # Fetch counts from the database
            cursor.execute("SELECT COUNT(*) FROM STUDENT_MASTER")
            student_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM EMPLOYEE_MASTER")
            employee_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM COURSE_MASTER")
            course_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM BATCH_MASTER")
            batch_count = cursor.fetchone()[0]

            return {
                "students": str(student_count),
                "employees": str(employee_count),
                "courses": str(course_count),
                "batches": str(batch_count)
            }

        except mysql.connector.Error as e:
            # Display error message using a messagebox
            messagebox.showerror("Error", f"Error occurred during fetch operation: {e}")

            # Log the exception
            print("Error occurred during fetch operation:", e)
            return None

    def update_counts_periodically(self):
        # Fetch and update counts
        self.fetch_and_update_counts()

        # Schedule the next update after 10 seconds
        self.master.after(100, self.update_counts_periodically)
    def logout(self):
        op = messagebox.askyesno("Logout","Do you want to logout", parent=self.master)
        if op:
            self.master.destroy()
            self.login_window = LoginWindow(tk.Tk())

    def open_reset_password_window(self):
        self.new_win = tk.Toplevel(self.master)
        self.new_obj = ResetPasswordWindow(self.new_win)

    def exit_application(self):
        op = messagebox.askyesno("Exit", "Do you want to exit?", parent=self.master)
        if op:
            self.master.destroy()
class ResetPasswordWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Reset Password")
        self.master.geometry("400x300")

        # Load and resize background image
        bg_image = Image.open("../images/bg.jpeg").resize((400, 300))
        self.bg_image = ImageTk.PhotoImage(bg_image)

        # Place the background image on the reset password window
        bg_label = tk.Label(master, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # New Password label and entry
        self.new_password_label = tk.Label(master, text="New Password:")
        self.new_password_label.place(relx=0.5, rely=0.4, anchor="center")
        self.new_password_entry = tk.Entry(master)
        self.new_password_entry.place(relx=0.5, rely=0.45, anchor="center")

        # Confirm Password label and entry
        self.confirm_password_label = tk.Label(master, text="Confirm Password:")
        self.confirm_password_label.place(relx=0.5, rely=0.55, anchor="center")
        self.confirm_password_entry = tk.Entry(master, show="*")
        self.confirm_password_entry.place(relx=0.5, rely=0.6, anchor="center")

        # Reset Password button
        self.reset_button = tk.Button(master, text="Reset Password", command=self.reset_password)
        self.reset_button.place(relx=0.5, rely=0.7, anchor="center")

    def __init__(self, master, generate_new_password):
        self.master = master
        self.master.title("Reset Password")
        self.master.geometry("400x300")

        # Load and resize background image
        bg_image = Image.open("../images/bg.jpeg").resize((400, 300))
        self.bg_image = ImageTk.PhotoImage(bg_image)

        # Place the background image on the reset password window
        bg_label = tk.Label(master, image=self.bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # New Password label and entry
        self.new_password_label = tk.Label(master, text="New Password:")
        self.new_password_label.place(relx=0.5, rely=0.4, anchor="center")
        self.new_password_entry = tk.Entry(master)
        self.new_password_entry.place(relx=0.5, rely=0.45, anchor="center")

        # Confirm Password label and entry
        self.confirm_password_label = tk.Label(master, text="Confirm Password:")
        self.confirm_password_label.place(relx=0.5, rely=0.55, anchor="center")
        self.confirm_password_entry = tk.Entry(master, show="*")
        self.confirm_password_entry.place(relx=0.5, rely=0.6, anchor="center")

        # Reset Password button
        self.reset_button = tk.Button(master, text="Reset Password", command=self.reset_password)
        self.reset_button.place(relx=0.5, rely=0.7, anchor="center")

    def reset_password(self):
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            # Update password in USER_DATA
            username = login_window.username_entry.get()
            if username in USER_DATA:
                USER_DATA[username] = (new_password, USER_DATA[username][1])
                messagebox.showinfo("Password Reset", "Password successfully reset")
            else:
                messagebox.showerror("Error", "User not found")



if __name__ == "__main__":
    master = tk.Tk()
    login_window = LoginWindow(master)
    master.mainloop()
