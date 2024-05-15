import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from PIL import ImageTk, Image

class EmployeeMaster:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1365x800+0+0')
        self.master.title("EMPLOYEE MANAGEMENT SYSTEM")

        # ======title=====
        title = tk.Label(master, text="EMPLOYEE MANAGEMENT SYSTEM", font=("goudy old style ", 30, "bold"),
                         bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1)
        # variable
        self.E_ID = tk.IntVar()
        self.EMP_Name = tk.StringVar()
        self.Education = tk.StringVar()
        self.C_ID = tk.IntVar()
        self.Course_Name = tk.StringVar()
        self.Course_Fees = tk.StringVar()
        self.Aadhar_Number = tk.StringVar()
        self.Mob_No = tk.StringVar()
        self.total_employees = tk.StringVar()
        self.total_employees.set("Total Employees: 0")
        self.search_in_c = tk.StringVar()
        self.search_in_entry = tk.StringVar()
        # ==========detail frame=====
        detail_frame = tk.LabelFrame(master, text="Enter Details:", bd=10,
                                     font=('Arial Black', 12), bg="light gray",
                                     relief=tk.GROOVE)
        detail_frame.place(x=0, y=65, width=450, height=615)

        # ============labels==========
        tk.Label(detail_frame, text="Employee ID:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=0, column=0, sticky="e")

        tk.Label(detail_frame, text="Employee Name:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=1, column=0, sticky="e")

        tk.Label(detail_frame, text="Education:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=2, column=0, sticky="e")

        tk.Label(detail_frame, text="Course ID:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=3, column=0, sticky="e")

        tk.Label(detail_frame, text="Course Name:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=4, column=0, sticky="e")
        tk.Label(detail_frame, text="Course Fees:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=5, column=0, sticky="e")

        tk.Label(detail_frame, text="Aadhar Number:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=6, column=0, sticky="e")

        tk.Label(detail_frame, text="Mobile Number:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=7, column=0, sticky="e")

        # ========== Entries ========
        detail_frame.employee_id_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.E_ID)
        detail_frame.employee_id_entry.grid(row=0, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.employee_name_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.EMP_Name)
        detail_frame.employee_name_entry.grid(row=1, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.education_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Education)
        detail_frame.education_entry.grid(row=2, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.course_id_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.C_ID)
        detail_frame.course_id_entry.grid(row=3, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.course_name_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Course_Name)
        detail_frame.course_name_entry.grid(row=4, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.course_fees_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Course_Fees)
        detail_frame.course_fees_entry.grid(row=5, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.aadhar_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Aadhar_Number)
        detail_frame.aadhar_entry.grid(row=6, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.mobile_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Mob_No)
        detail_frame.mobile_entry.grid(row=7, column=1, padx=3, pady=3, sticky="ew")

        # ===========button frame=========self.
        btn_frame = tk.Frame(detail_frame, bg="light gray", bd=10, relief=tk.GROOVE)
        btn_frame.place(x=0, y=465, width=430, height=120)

        insert_btn = tk.Button(btn_frame, text="Add", bd=4, font=('Arial Black', 12), width=17)
        insert_btn.grid(row=0, column=0, padx=2, pady=3)
        insert_btn.config(command=self.insert_data)

        update_btn = tk.Button(btn_frame, text="Edit", bd=4, font=('Arial Black', 12), width=17)
        update_btn.grid(row=0, column=1, padx=2, pady=3)
        update_btn.config(command=self.update_data)

        delete_btn = tk.Button(btn_frame, text="Delete", bd=4, font=('Arial Black', 12), width=17)
        delete_btn.grid(row=1, column=0, padx=2, pady=3)
        delete_btn.config(command=self.delete_data)

        clear_btn = tk.Button(btn_frame, text="Clear", bd=4, font=('Arial Black', 12), width=17)
        clear_btn.grid(row=1, column=1, padx=2, pady=3)
        clear_btn.config(command=self.clear_fields)

        # data frame
        data_frame = tk.Frame(master, bd=12, bg="light gray", relief=tk.GROOVE)
        data_frame.place(x=465, y=65, width=900, height=600)

        # search frame

        search_frame = tk.Frame(data_frame, bg="light gray", bd=7, relief=tk.GROOVE)
        search_frame.pack(side=tk.TOP, fill=tk.X)

        search_lbl = tk.Label(search_frame, text="Search", bg="light gray", font=("arial", 14))
        search_lbl.grid(row=0, column=0)

        search_in = ttk.Combobox(search_frame, textvariable=self.search_in_c, font=("arial", 13), state="readonly")
        search_in["values"] = ("Employee ID", "Employee Name", "Course Name", "Aadhar Number", "Mobile Number")
        search_in.grid(row=0, column=1, padx=10, pady=3)

        search_in_entry = tk.Entry(search_frame, textvariable=self.search_in_entry, font=('Arial Black', 12), bd=5,
                                   relief=tk.GROOVE)
        search_in_entry.grid(row=0, column=2, padx=10, pady=3)

        search_btn = tk.Button(search_frame, text="Search", font=('Arial Black', 12), bd=4, width=10)
        search_btn.grid(row=0, column=3, padx=10, pady=3)
        search_btn.config(command=self.search_data)

        show_all_btn = tk.Button(search_frame, text="Show All", font=('Arial Black', 12), bd=4, width=10)
        show_all_btn.grid(row=0, column=4, padx=10, pady=3)
        show_all_btn.config(command=self.fetch_data)

        # data view frame
        view_frame = tk.Frame(data_frame, bg="light gray", bd=10, relief=tk.GROOVE)
        view_frame.place(x=10, y=70, width=870, height=500)

        scroll_x = tk.Scrollbar(view_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(view_frame, orient=tk.VERTICAL)

        self.employee_master = ttk.Treeview(view_frame, columns=("Employee ID", "Employee Name", "Education",
                                                                 "Course ID", "Course Name", "Course Fees", "Aadhar Number",
                                                                 "Mobile Number"),
                                            xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x.config(command=self.employee_master.xview)
        scroll_y.config(command=self.employee_master.yview)

        self.employee_master.heading("Employee ID", text="Employee ID")
        self.employee_master.heading("Employee Name", text="Employee Name")
        self.employee_master.heading("Education", text="Education")
        self.employee_master.heading("Course ID", text="Course ID")
        self.employee_master.heading("Course Name", text="Course Name")
        self.employee_master.heading("Course Fees", text="Course Fees")
        self.employee_master.heading("Aadhar Number", text="Aadhar Number")
        self.employee_master.heading("Mobile Number", text="Mobile Number")

        self.employee_master['show'] = 'headings'

        self.employee_master.column("Employee ID", width=100)
        self.employee_master.column("Employee Name", width=200)
        self.employee_master.column("Education", width=100)
        self.employee_master.column("Course ID", width=100)
        self.employee_master.column("Course Name", width=150)
        self.employee_master.column("Course Fees", width=150)
        self.employee_master.column("Aadhar Number", width=150)
        self.employee_master.column("Mobile Number", width=100)

        self.employee_master.pack(fill=tk.BOTH, expand=1)

        self.employee_master.bind('<<TreeviewSelect>>', self.on_treeview_select)

        self.fetch_data()

    # functions of database
    def fetch_data(self):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            mycursor = db.cursor()
            sql = "SELECT * FROM  EMPLOYEE_MASTER"
            mycursor.execute(sql)
            rows = mycursor.fetchall()
            if len(rows) != 0:
                self.employee_master.delete(*self.employee_master.get_children())
                for row in rows:
                    self.employee_master.insert("", tk.END, values=row)
                db.commit()
            db.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred while fetching data: {e}")

    def insert_data(self):
        try:
            e_id_val = self.E_ID.get()
            emp_name_val = self.EMP_Name.get()
            education_val = self.Education.get()
            c_id_val = self.C_ID.get()
            course_name_val = self.Course_Name.get()
            course_fees_val = self.Course_Fees.get()
            aadhar_number_val = self.Aadhar_Number.get()
            mob_no_val = self.Mob_No.get()

            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()
            sql = (
                "INSERT INTO EMPLOYEE_MASTER (E_ID, EMP_NAME, EDUCATION, C_ID, COURSE_NAME, COURSE_FEES, AADHAR_NUMBER, MOB_NO) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")

            val = (e_id_val, emp_name_val, education_val, c_id_val, course_name_val, course_fees_val,
                   aadhar_number_val, mob_no_val)
            cursor.execute(sql, val)
            db.commit()
            db.close()

            self.fetch_data()
            self.clear_fields()

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred during insert operation: {e}")

    def update_data(self):
        try:
            e_id_val = self.E_ID.get()
            emp_name_val = self.EMP_Name.get()
            education_val = self.Education.get()
            c_id_val = self.C_ID.get()
            course_name_val = self.Course_Name.get()
            course_fees_val = self.Course_Fees.get()
            aadhar_number_val = self.Aadhar_Number.get()
            mob_no_val = self.Mob_No.get()

            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()

            sql = ("UPDATE EMPLOYEE_MASTER SET EMP_NAME=%s, EDUCATION=%s, C_ID=%s, COURSE_NAME=%s, COURSE_FEES=%s "
                   "AADHAR_NUMBER=%s, MOB_NO=%s WHERE E_ID=%s")

            val = (emp_name_val, education_val, c_id_val, course_name_val,course_fees_val, aadhar_number_val, mob_no_val, e_id_val)

            cursor.execute(sql, val)
            db.commit()
            db.close()

            self.fetch_data()
            self.clear_fields()

        except Exception as e:
            messagebox.showerror("Error", "An error occurred during update operation:\n{}".format(e))

    def delete_data(self):
        try:
            selected_item = self.employee_master.focus()
            if selected_item:
                item_id = self.employee_master.item(selected_item)['values'][0]

                confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
                if confirm:
                    db = mysql.connector.connect(host="localhost", user="root", password="gc@425508",
                                                 database='master_db')
                    cursor = db.cursor()
                    sql = "DELETE FROM EMPLOYEE_MASTER WHERE E_ID = %s"
                    cursor.execute(sql, (item_id,))
                    db.commit()
                    db.close()

                    self.fetch_data()

                    messagebox.showinfo("Success", "Record deleted successfully")
            else:
                messagebox.showwarning("Warning", "Please select a record to delete")

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred during delete operation: {e}")

    def clear_fields(self):
        self.E_ID.set(0)
        self.EMP_Name.set('')
        self.Education.set('')
        self.C_ID.set(0)
        self.Course_Name.set('')
        self.Course_Fees.set(0)
        self.Aadhar_Number.set('')
        self.Mob_No.set('')

    def search_data(self):
        try:
            search_criteria = self.search_in_c.get()
            keyword = self.search_in_entry.get()

            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()

            if search_criteria == "Employee ID":
                sql = "SELECT * FROM EMPLOYEE_MASTER WHERE E_ID LIKE %s"
            elif search_criteria == "Employee Name":
                sql = "SELECT * FROM EMPLOYEE_MASTER WHERE EMP_NAME LIKE %s"
            elif search_criteria == "Course Name":
                sql = "SELECT * FROM EMPLOYEE_MASTER WHERE COURSE_NAME LIKE %s"
            elif search_criteria == "Aadhar Number":
                sql = "SELECT * FROM EMPLOYEE_MASTER WHERE AADHAR_NUMBER LIKE %s"
            elif search_criteria == "Mobile Number":
                sql = "SELECT * FROM EMPLOYEE_MASTER WHERE MOB_NO LIKE %s"
            else:
                messagebox.showwarning("Invalid Search Criteria", "Please select a valid search criteria")
                db.close()
                return

            cursor.execute(sql, ('%' + keyword + '%',))
            rows = cursor.fetchall()

            if len(rows) != 0:
                self.employee_master.delete(*self.employee_master.get_children())
                for row in rows:
                    self.employee_master.insert("", tk.END, values=row)
                db.commit()
            else:
                messagebox.shomasterfo("No Results", "No matching records found")

            db.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred during search operation: {e}")

    def on_treeview_select(self, event=None):
        selected_item = self.employee_master.focus()
        values = self.employee_master.item(selected_item, 'values')

        if len(values) >= 8:
            self.E_ID.set(values[0])
            self.EMP_Name.set(values[1])
            self.Education.set(values[2])
            self.C_ID.set(values[3])
            self.Course_Name.set(values[4])
            self.Course_Fees.set(values[5])
            self.Aadhar_Number.set(values[6])
            self.Mob_No.set(values[7])
        else:
            self.clear_fields()

    def update_total_employees_label(self):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()
            sql = "SELECT COUNT(*) FROM EMPLOYEE_MASTER"
            cursor.execute(sql)
            total = cursor.fetchone()[0]
            self.total_employees.set(f"Total Employees: {total}")
            db.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred while fetching total employees: {e}")


if __name__ == "__main__":
    master = tk.Tk()
    dashboard = EmployeeMaster(master)
    master.mainloop()
