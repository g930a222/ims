import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector
from PIL import ImageTk, Image

class CourseMaster:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1365x800+0+0')
        self.master.title("COURSE MANAGEMENT SYSTEM")

        # ======title=====
        title = tk.Label(master, text="COURSE MANAGEMENT SYSTEM", font=("goudy old style ", 30, "bold"),
                         bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1)
        self.C_ID = tk.IntVar()
        self.Course_Name = tk.StringVar()
        self.Course_Fees = tk.StringVar()
        self.Duration_Year = tk.IntVar()
        self.Duration_Month = tk.IntVar()
        # ===search variable ==

        self.search_in = tk.StringVar()
        self.search_entry = tk.StringVar()
        # Detail Frame
        detail_frame = tk.LabelFrame(master, text="Enter Details:", bd=10,
                                     font=('Arial Black', 12), bg="light gray",
                                     relief=tk.GROOVE)
        detail_frame.place(x=0, y=65, width=450, height=615)

        # Labels
        tk.Label(detail_frame, text="Course ID:", font=('Arial Black', 12),
                 bg="light gray").grid(row=0, column=0, sticky="e")
        tk.Label(detail_frame, text="Course Name:", font=('Arial Black', 12),
                 bg="light gray").grid(row=1, column=0, sticky="e")
        tk.Label(detail_frame, text="Course Fees :", font=('Arial Black', 12),
                 bg="light gray").grid(row=2, column=0, sticky="e")
        tk.Label(detail_frame, text="Duration (Years):", font=('Arial Black', 12),
                 bg="light gray").grid(row=3, column=0, sticky="e")
        tk.Label(detail_frame, text="Duration (Months):", font=('Arial Black', 12),
                 bg="light gray").grid(row=4, column=0, sticky="e")

        # Entries
        detail_frame.course_id_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.C_ID)
        detail_frame.course_id_entry.grid(row=0, column=1, padx=3, pady=3, sticky="ew")
        detail_frame.course_name_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Course_Name)
        detail_frame.course_name_entry.grid(row=1, column=1, padx=3, pady=3, sticky="ew")
        detail_frame.course_fees_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Course_Fees)
        detail_frame.course_fees_entry.grid(row=2, column=1, padx=3, pady=3, sticky="ew")
        detail_frame.duration_year_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Duration_Year)
        detail_frame.duration_year_entry.grid(row=3, column=1, padx=3, pady=3, sticky="ew")
        detail_frame.duration_month_entry = tk.Entry(detail_frame, font=('Arial Black', 12), textvariable=self.Duration_Month)
        detail_frame.duration_month_entry.grid(row=4, column=1, padx=3, pady=3, sticky="ew")

        # Button Frame
        btn_frame = tk.Frame(detail_frame, bg="light gray", bd=10, relief=tk.GROOVE)
        btn_frame.place(x=0, y=230, width=430, height=120)

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

        # Data Frame
        data_frame = tk.Frame(master, bd=12, bg="light gray", relief=tk.GROOVE)
        data_frame.place(x=465, y=65, width=900, height=600)

        # Search Frame
        search_frame = tk.Frame(data_frame, bg="light gray", bd=7, relief=tk.GROOVE)
        search_frame.pack(side=tk.TOP, fill=tk.X)

        search_lbl = tk.Label(search_frame, text="Search", bg="light gray", font=("Arial", 14))
        search_lbl.grid(row=0, column=0)

        search_in = ttk.Combobox(search_frame, textvariable=self.search_in, font=("Arial", 13), state="readonly")
        search_in["values"] = ("Course ID", "Course Name")
        search_in.grid(row=0, column=1, padx=10, pady=3)

        search_in_entry = tk.Entry(search_frame, textvariable=self.search_entry, font=('Arial Black', 12), bd=5,
                                   relief=tk.GROOVE)
        search_in_entry.grid(row=0, column=2, padx=10, pady=3)

        search_btn = tk.Button(search_frame, text="Search", command=self.search_data, font=("Arial", 14), bd=5,
                               width=10, bg="light gray")
        search_btn.grid(row=0, column=3, padx=10, pady=3)

        showall_btn = tk.Button(search_frame, text="Show all", command=self.show_all_data, font=("Arial", 14), bd=5,
                                width=10, bg="light gray")
        showall_btn.grid(row=0, column=4, padx=10, pady=3)

        # Main Frame
        main_frame = tk.Frame(data_frame, bd=11, relief=tk.GROOVE)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Scroll Bars
        y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
        x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

        # Treeview
        self.course_master = ttk.Treeview(main_frame, columns=("Course ID", "Course Name", "Course Fees",
                                                               "Duration (Years)", "Duration (Months)"),
                                          yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        y_scroll.config(command=self.course_master.yview)
        x_scroll.config(command=self.course_master.xview)

        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.course_master.heading("Course ID", text="Course ID")
        self.course_master.heading("Course Name", text="Course Name")
        self.course_master.heading("Course Fees", text="Course Fees")
        self.course_master.heading("Duration (Years)", text="Duration (Years)")
        self.course_master.heading("Duration (Months)", text="Duration (Months)")

        self.course_master['show'] = "headings"

        self.course_master.column("Course ID", width=200)
        self.course_master.column("Course Name", width=200)
        self.course_master.column("Course Fees", width=200)
        self.course_master.column("Duration (Years)", width=200)
        self.course_master.column("Duration (Months)", width=200)

        self.course_master.pack(fill=tk.BOTH, expand=True)

        self.course_master.bind('<<TreeviewSelect>>', self.on_treeview_select)

        # Fetch data initially
        self.fetch_data()

    def fetch_data(self):
        try:
            # Connect to the database
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()

            # Fetch data from the database
            sql = "SELECT * FROM COURSE_MASTER"
            cursor.execute(sql)
            rows = cursor.fetchall()

            # Clear existing data from the Treeview
            for row in self.course_master.get_children():
                self.course_master.delete(row)

            # Insert fetched data into the Treeview
            for row in rows:
                self.course_master.insert("", tk.END, values=row)

            # Commit and close the database connection
            db.commit()
            db.close()

        except Exception as e:
            # Display error message using a messagebox
            messagebox.showerror("Error", f"Error occurred during fetch operation: {e}")

            # Log the exception
            print("Error occurred during fetch operation:", e)

    def insert_data(self):
        try:
            # Retrieve data from entry fields
            c_id_val = self.C_ID.get()
            course_name_val = self.Course_Name.get()
            course_fees_val = self.Course_Fees.get()
            duration_year_val = self.Duration_Year.get()
            duration_month_val = self.Duration_Month.get()

            # Connect to the database
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()

            # Insert data into the database
            sql = ("INSERT INTO COURSE_MASTER (C_ID, COURSE_NAME, Course_Fees, DURATION_YEAR, DURATION_MONTH) "
                   "VALUES (%s, %s, %s,%s, %s)")
            val = (c_id_val, course_name_val,course_fees_val, duration_year_val, duration_month_val)
            cursor.execute(sql, val)

            # Commit and close the database connection
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

    def update_data(self):
        try:
            # Retrieve data from entry fields
            c_id_val = self.C_ID.get()
            course_name_val = self.Course_Name.get()
            course_fees_val=self.Course_Fees.get()
            duration_year_val = self.Duration_Year.get()
            duration_month_val = self.Duration_Month.get()

            # Connect to the database
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()

            # Update data in the database
            sql = ("UPDATE COURSE_MASTER SET COURSE_NAME=%s,COURSE_FEES=%s, DURATION_YEAR=%s, DURATION_MONTH=%s "
                   "WHERE C_ID=%s")
            val = (course_name_val,course_fees_val, duration_year_val, duration_month_val, c_id_val)
            cursor.execute(sql, val)

            # Commit and close the database connection
            db.commit()
            db.close()

            # Refresh Treeview
            self.fetch_data()

            # Clear entry fields
            self.clear_fields()

        except Exception as e:
            # Display error message using a messagebox
            messagebox.showerror("Error", f"Error occurred during update operation: {e}")

            # Log the exception
            print("Error occurred during update operation:", e)

    def delete_data(self):
        try:
            # Get the selected item from the Treeview
            selected_item = self.course_master.focus()
            if selected_item:
                # Retrieve the ID of the selected item
                item_id = self.course_master.item(selected_item)['values'][0]

                # Connect to the database
                db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
                cursor = db.cursor()

                # Delete the record from the database
                sql = "DELETE FROM COURSE_MASTER WHERE C_ID = %s"
                cursor.execute(sql, (item_id,))

                # Commit and close the database connection
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

    def clear_fields(self):
        # Clear all entry fields
        self.C_ID.set(0)
        self.Course_Name.set('')
        self.Course_Fees.set(0)
        self.Duration_Year.set(0)
        self.Duration_Month.set(0)

    def search_data(self):
        try:
            # Get the selected search criteria and search keyword
            search_criteria = self.search_in.get()
            keyword = self.search_entry.get()

            # Connect to the database
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()

            # Execute the search query based on the selected criteria
            if search_criteria == "Course ID":
                sql = "SELECT * FROM COURSE_MASTER WHERE C_ID LIKE %s"
            elif search_criteria == "Course Name":
                sql = "SELECT * FROM COURSE_MASTER WHERE COURSE_NAME LIKE %s"
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
                self.course_master.delete(*self.course_master.get_children())
                for row in rows:
                    self.course_master.insert("", tk.END, values=row)
                db.commit()
            else:
                # If no matching records are found, display a message
                messagebox.showinfo("No Results", "No matching records found")

            # Close the database connection
            db.close()

        except Exception as e:
            # Display error message using a messagebox
            messagebox.showerror("Error", f"Error occurred during search operation: {e}")

            # Log the exception
            print("Error occurred during search operation:", e)

    def show_all_data(self):
        # Fetch all records from the database
        self.fetch_data()

    def on_treeview_select(self, event):
        # Get the selected item
        selected_item = self.course_master.focus()

        # Get the values of the selected item
        values = self.course_master.item(selected_item, 'values')
    
        # Check if values has enough elements
        if len(values) >= 5:
            self.C_ID.set(values[0])
            self.Course_Name.set(values[1])
            self.Course_Fees.set(values[2])
            self.Duration_Year.set(values[3])
            self.Duration_Month.set(values[4])
        else:
            # Handle the case when the selected item doesn't have enough values
            # Clear all entry fields or take appropriate action
            self.clear_fields()



if __name__ == "__main__":
    master = tk.Tk()
    dashboard = CourseMaster(master)
    master.mainloop()