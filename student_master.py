import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector



class StudentMaster:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1365x800+0+0')
        self.master.title("STUDENT MANAGEMENT SYSTEM")
        self.master.focus_force()
        # ======title=====
        title = tk.Label(master, text="STUDENT MANAGEMENT SYSTEM", font=("goudy old style ", 30, "bold"),
                         bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1)

        # ======= variables =====
        self.ID = tk.IntVar()
        self.Name = tk.StringVar()
        self.Education = tk.StringVar()
        self.C_ID = tk.IntVar()
        self.Course_Name = tk.StringVar()
        self.Course_Fee = tk.IntVar()
        self.Emp_ID = tk.IntVar()
        self.Employee_Name = tk.StringVar()
        self.Batch_ID = tk.IntVar()
        self.Batch_Name = tk.StringVar()
        self.Mobile_No = tk.StringVar()
        self.Parent_No = tk.StringVar()
        self.Discount = tk.IntVar()
        self.Remark = tk.StringVar()

        # ===search variable ==

        self.search_in = tk.StringVar()
        self.search_entry = tk.StringVar()
        # ========= detail frame ===========
        detail_frame = tk.LabelFrame(self.master, text="Enter Details:", bd=10,
                                     font=('Arial Black', 12), bg="light gray",
                                     relief=tk.GROOVE)
        detail_frame.place(x=0, y=65, width=450, height=615)

        # labels
        tk.Label(detail_frame, text="ID:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=0, column=0, sticky="e")

        tk.Label(detail_frame, text="Name:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=1, column=0, sticky="e")

        tk.Label(detail_frame, text="Education:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=2, column=0, sticky="e")

        tk.Label(detail_frame, text="Course ID:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=3, column=0, sticky="e")

        tk.Label(detail_frame, text="Course Name:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=4, column=0, sticky="e")

        tk.Label(detail_frame, text="Course Fees:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=5, column=0, sticky="e")

        tk.Label(detail_frame, text="Employee ID:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=6, column=0, sticky="e")

        tk.Label(detail_frame, text="Employee Name:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=7, column=0, sticky="e")

        tk.Label(detail_frame, text="Batch ID:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=8, column=0, sticky="e")

        tk.Label(detail_frame, text="Batch Name:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=9, column=0, sticky="e")

        tk.Label(detail_frame, text="Mobile No:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=10, column=0, sticky="e")

        tk.Label(detail_frame, text="Parent No:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=11, column=0, sticky="e")

        tk.Label(detail_frame, text="Discount:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=12, column=0, sticky="e")

        tk.Label(detail_frame, text="Remark:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=13, column=0, sticky="e")

        # Entries
        detail_frame.id_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.ID)
        detail_frame.id_entry.grid(row=0, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.name_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Name)
        detail_frame.name_entry.grid(row=1, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.education_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Education)
        detail_frame.education_entry.grid(row=2, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.course_id_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.C_ID)
        detail_frame.course_id_entry.grid(row=3, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.course_name_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Course_Name)
        detail_frame.course_name_entry.grid(row=4, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.course_fees_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Course_Fee)
        detail_frame.course_fees_entry.grid(row=5, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.employee_id_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Emp_ID)
        detail_frame.employee_id_entry.grid(row=6, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.employee_name_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Employee_Name)
        detail_frame.employee_name_entry.grid(row=7, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.batch_id_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Batch_ID)
        detail_frame.batch_id_entry.grid(row=8, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.batch_name_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Batch_Name)
        detail_frame.batch_name_entry.grid(row=9, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.mobile_no_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Mobile_No)
        detail_frame.mobile_no_entry.grid(row=10, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.parent_no_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Parent_No)
        detail_frame.parent_no_entry.grid(row=11, column=1,padx=3, pady=3, sticky="ew")

        detail_frame.discount_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Discount)
        detail_frame.discount_entry.grid(row=12, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.remark_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Remark)
        detail_frame.remark_entry.grid(row=13, column=1,  padx=3, pady=3,sticky="ew")

        # ======= button frame=======

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

        # =========data frame============
        data_frame = tk.Frame(self.master, bd=12, bg="light gray", relief=tk.GROOVE)
        data_frame.place(x=465, y=65, width=900, height=600)

        # =========search frame========

        search_frame = tk.Frame(data_frame, bg="light gray", bd=7, relief=tk.GROOVE)
        search_frame.pack(side=tk.TOP, fill=tk.X)

        search_lbl = tk.Label(search_frame, text="Search", bg="light gray", font=("arial", 14))
        search_lbl.grid(row=0, column=0)

        search_in = ttk.Combobox(search_frame, textvariable = self.search_in,font=("arial", 13), state="readonly")
        search_in["values"] = ("ID", "Name", "Education", "Batch Name", "Course Name", "Mobile No")
        search_in.grid(row=0, column=1, padx=10, pady=3)

        search_in_entry = tk.Entry(search_frame,textvariable=self.search_entry, font=('Arial Black', 12), bd=5, relief=tk.GROOVE)
        search_in_entry.grid(row=0, column=2, padx=10, pady=3)

        search_btn = tk.Button(search_frame, text="Search",command=self.search_data, font=("arial", 14), bd=5, width=10, bg="light gray")
        search_btn.grid(row=0, column=3, padx=10, pady=3)

        show_all_btn = tk.Button(search_frame, text="Show All", font=("arial", 14), bd=5, width=10, bg="light gray")
        show_all_btn.grid(row=0, column=4, padx=10, pady=3)
        show_all_btn.config(command=self.show_all_data)

        # ==========database frame==============
        view_frame = tk.Frame(data_frame, bd=11, relief=tk.GROOVE)
        view_frame.pack(fill=tk.BOTH, expand=True)

        # ============scroll bar===============
        y_scroll = tk.Scrollbar(view_frame, orient=tk.VERTICAL)
        x_scroll = tk.Scrollbar(view_frame, orient=tk.HORIZONTAL)

        self.student_master = ttk.Treeview(view_frame, columns=("ID:", "Name:", "Education:",
                                                                "C ID:", "Course Name:",
                                                                "Course Fees:",
                                                                "Emp ID:", "Employee Name:", "Batch ID:",
                                                                "Batch Name:",
                                                                "Mobile No:",
                                                                "Parent No:", "Discount:", "Remark:"),
                                           yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        y_scroll.config(command=self.student_master.yview)
        x_scroll.config(command=self.student_master.xview)

        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.student_master.heading("#1", text="ID")
        self.student_master.heading("#2", text="Name")
        self.student_master.heading("#3", text="Education")
        self.student_master.heading("#4", text="C ID")
        self.student_master.heading("#5", text="Course Name")
        self.student_master.heading("#6", text="Course Fees")
        self.student_master.heading("#7", text="Emp ID")
        self.student_master.heading("#8", text="Employee Name")
        self.student_master.heading("#9", text="Batch ID")
        self.student_master.heading("#10", text="Batch Name")
        self.student_master.heading("#11", text="Mobile No")
        self.student_master.heading("#12", text="Parent No")
        self.student_master.heading("#13", text="Discount")
        self.student_master.heading("#14", text="Remark")

        self.student_master['show'] = "headings"

        self.student_master.column("#1", width=150)
        self.student_master.column("#2", width=150)
        self.student_master.column("#3", width=150)
        self.student_master.column("#4", width=150)
        self.student_master.column("#5", width=150)
        self.student_master.column("#6", width=150)
        self.student_master.column("#7", width=150)
        self.student_master.column("#8", width=150)
        self.student_master.column("#9", width=150)
        self.student_master.column("#10", width=150)
        self.student_master.column("#11", width=150)
        self.student_master.column("#12", width=150)
        self.student_master.column("#13", width=150)
        self.student_master.column("#14", width=150)

        self.student_master.pack(fill=tk.BOTH, expand=True)
        self.fetch_data()

        self.student_master.bind('<<TreeviewSelect>>',self.on_treeview_select)
    # functions of database

    def fetch_data(self):
        db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
        mycursor = db.cursor()
        sql = "SELECT * FROM  STUDENT_MASTER"
        mycursor.execute(sql)
        rows = mycursor.fetchall()

        if len(rows) != 0:
            self.student_master.delete(*self.student_master.get_children())
            for row in rows:
                self.student_master.insert("", tk.END, values=row)
            db.commit()
        db.close()

    def insert_data(self):
        try:
            # Retrieve data from entry fields
            id_val = self.ID.get()
            name_val = self.Name.get()
            education_val = self.Education.get()
            c_id_val = self.C_ID.get()
            course_name_val = self.Course_Name.get()
            course_fee_val = self.Course_Fee.get()
            emp_id_val = self.Emp_ID.get()
            employee_name_val = self.Employee_Name.get()
            batch_id_val = self.Batch_ID.get()
            batch_name_val = self.Batch_Name.get()
            mobile_no_val = self.Mobile_No.get()
            parent_no_val = self.Parent_No.get()
            discount_val = self.Discount.get()
            remark_val = self.Remark.get()

        # Insert data into the database
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()
            sql = ("INSERT INTO STUDENT_MASTER (S_ID, S_NAME, EDUCATION, C_ID, COURSE_NAME, COURSE_FEES, "
               "E_ID, EMP_NAME, B_ID, BATCH_NAME, MOB_NO, PARENT_NO, DISCOUNT, REMARK) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            val = (id_val, name_val, education_val, c_id_val, course_name_val, course_fee_val, emp_id_val,
               employee_name_val, batch_id_val, batch_name_val, mobile_no_val, parent_no_val, discount_val, remark_val)
            cursor.execute(sql, val)
            db.commit()
            db.close()

        # Refresh Treeview
            self.fetch_data()

        # Clear entry fields
            self.clear_fields()

        except Exception as e:
         # Display error message using a messagebox
            messagebox.showerror("Error", f"Error occurred during insert operation: {e}")

        # Log the exception
            print("Error occurred during insert operation:", e)

        # Refresh Treeview
        self.fetch_data()
        # Clear entry fields
        self.clear_fields()

    # Refresh Treeview
        self.fetch_data()

    def update_data(self):
        try:

            # Retrieve data from entry fields
            id_val = self.ID.get()
            name_val = self.Name.get()
            education_val = self.Education.get()
            c_id_val = self.C_ID.get()
            course_name_val = self.Course_Name.get()
            course_fee_val = self.Course_Fee.get()
            emp_id_val = self.Emp_ID.get()
            employee_name_val = self.Employee_Name.get()
            batch_id_val = self.Batch_ID.get()
            batch_name_val = self.Batch_Name.get()
            mobile_no_val = self.Mobile_No.get()
            parent_no_val = self.Parent_No.get()
            discount_val = self.Discount.get()
            remark_val = self.Remark.get()

            # Connect to the database
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()

            # Update data in the database
            sql = ("UPDATE STUDENT_MASTER SET S_NAME=%s, EDUCATION=%s, C_ID=%s, COURSE_NAME=%s, COURSE_FEES=%s, "
                   "E_ID=%s, EMP_NAME=%s, B_ID=%s, BATCH_NAME=%s, MOB_NO=%s, PARENT_NO=%s, DISCOUNT=%s, REMARK=%s "
                   "WHERE S_ID=%s")

            val = (name_val, education_val, c_id_val, course_name_val, course_fee_val, emp_id_val,
                   employee_name_val, batch_id_val, batch_name_val, mobile_no_val, parent_no_val, discount_val,
                   remark_val, id_val)

            cursor.execute(sql, val)
            db.commit()
            db.close()

            # Refresh Treeview
            self.fetch_data()

            # Clear entry fields
            self.clear_fields()
        except Exception as e:
            # Display error message
            messagebox.showerror("Error", "An error occurred during update operation:\n{}".format(e))

        # Log the exception
        # print("Error occurred during update operation:", e)
        # Refresh Treeview
        self.fetch_data()

    def delete_data(self):
        try:
            # Get the selected item from the Treeview
            selected_item = self.student_master.focus()
            if selected_item:
                # Retrieve the ID of the selected item
                item_id = self.student_master.item(selected_item)['values'][0]

                # Display a confirmation message box
                confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
                if confirm:
                    # Delete the record from the database
                    db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
                    cursor = db.cursor()
                    sql = "DELETE FROM STUDENT_MASTER WHERE S_ID = %s"
                    cursor.execute(sql, (item_id,))
                    db.commit()
                    db.close()

                    # Refresh Treeview
                    self.fetch_data()
                    # Show a success message box
                    messagebox.showinfo("Success", "Record deleted successfully")

            else:
                messagebox.showwarning("Warning", "Please select a record to delete")

        except Exception as e:
            # Display error message using a messagebox
            messagebox.showerror("Error", f"Error occurred during delete operation: {e}")

            # Log the exception
            print("Error occurred during delete operation:", e)

            # Refresh Treeview
            self.fetch_data()

    def clear_fields(self):
        # Clear all entry fields
        self.ID.set(0)
        self.Name.set('')
        self.Education.set('')
        self.C_ID.set(0)
        self.Course_Name.set('')
        self.Course_Fee.set(0)
        self.Emp_ID.set(0)
        self.Employee_Name.set('')
        self.Batch_ID.set(0)
        self.Batch_Name.set('')
        self.Mobile_No.set('')
        self.Parent_No.set('')
        self.Discount.set(0)
        self.Remark.set('')
        # Clear other fields similarly

    def show_all_data(self):
        # Fetch all records from the database
        # Update the Treeview with the fetched records
        self.fetch_data()

    def search_data(self):
        # Get the selected search criteria and search keyword
        search_criteria = self.search_in.get()
        keyword = self.search_entry.get()

        # Connect to the database
        db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
        cursor = db.cursor()

        # Execute the search query based on the selected criteria
        if search_criteria == "ID":
            sql = "SELECT * FROM STUDENT_MASTER WHERE S_ID LIKE %s"
        elif search_criteria == "Name":
            sql = "SELECT * FROM STUDENT_MASTER WHERE S_NAME LIKE %s"
        elif search_criteria == "Education":
            sql = "SELECT * FROM STUDENT_MASTER WHERE EDUCATION LIKE %s"
        elif search_criteria == "Batch Name":
            sql = "SELECT * FROM STUDENT_MASTER WHERE BATCH_NAME LIKE %s"
        elif search_criteria == "Course Name":
            sql = "SELECT * FROM STUDENT_MASTER WHERE COURSE_NAME LIKE %s"
        elif search_criteria == "Mobile No":
            sql = "SELECT * FROM STUDENT_MASTER WHERE MOB_NO LIKE %s"
        else:
            # Handle the case when an invalid search criteria is selected
            messagebox.showwarning("Invalid Search Criteria", "Please select a valid search criteria")
            db.close()
            return

        # Execute the query with the keyword
        cursor.execute(sql, ('%' + keyword + '%',))
        rows = cursor.fetchall()

        # Update the Treeview with the search results
        if len(rows) != 0:
            self.student_master.delete(*self.student_master.get_children())
            for row in rows:
                self.student_master.insert("", tk.END, values=row)
            db.commit()
        else:
            # If no matching records are found, display a message
            messagebox.shomasterfo("No Results", "No matching records found")

        # Close the database connection
        db.close()

    def on_treeview_select(self, event):
        # Get the selected item
        selected_item = self.student_master.focus()

        # Get the values of the selected item
        values = self.student_master.item(selected_item, 'values')
        # Check if values has enough elements
        if len(values) >= 13:
            self.ID.set(values[0])
            self.Name.set(values[1])
            self.Education.set(values[2])
            self.C_ID.set(values[3])
            self.Course_Name.set(values[4])
            self.Course_Fee.set(values[5])
            self.Emp_ID.set(values[6])
            self.Employee_Name.set(values[7])
            self.Batch_ID.set(values[8])
            self.Batch_Name.set(values[9])
            self.Mobile_No.set(values[10])
            self.Parent_No.set(values[11])
            self.Discount.set(values[12])
            self.Remark.set(values[13])
        else:
            # Handle the case when the selected item doesn't have enough values
            # Clear all entry fields or take appropriate action
            self.clear_fields()



if __name__ == "__main__":
    master = tk.Tk()
    dashboard =StudentMaster(master)
    master.mainloop()
