import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import ttk,messagebox
import mysql.connector


class FeesReceipt:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1365x800+0+0')
        self.master.title("FEES MANAGEMENT SYSTEM")

        # ======title=====
        title = tk.Label(master, text="FEES MANAGEMENT SYSTEM", font=("goudy old style ", 30, "bold"),
                         bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1)
        # ============variable=============
        self.F_ID= tk.IntVar()
        self.S_ID = tk.IntVar()
        self.S_NAME = tk.StringVar()
        self.C_ID = tk.IntVar()
        self.COURSE_NAME = tk.StringVar()
        self.COURSE_FEES = tk.StringVar()
        self.FEES_RECEIVED = tk.DoubleVar()
        self.REMAINING_FEES = tk.DoubleVar()
        self.RECEIPT_DATE = tk.StringVar()
        # ===search variable ==

        self.search_in = tk.StringVar()
        self.search_entry = tk.StringVar()
        # ============detail frame=======
        detail_frame = tk.LabelFrame(master, text="Enter Receipt Details:", bd=10,
                                     font=('Arial Black', 12), bg="light gray",
                                     relief=tk.GROOVE)
        detail_frame.place(x=0, y=65, width=450, height=615)

        # =========labels================
        tk.Label(detail_frame, text="F ID:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=0, column=0, sticky="e")

        tk.Label(detail_frame, text="Student ID:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=1, column=0, sticky="e")

        tk.Label(detail_frame, text="Student Name:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=2, column=0, sticky="e")

        tk.Label(detail_frame, text="Course ID:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=3, column=0, sticky="e")

        tk.Label(detail_frame, text="Course Name:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=4, column=0, sticky="e")

        tk.Label(detail_frame, text="Course Fees:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=5, column=0, sticky="e")

        tk.Label(detail_frame, text="Fees Received:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=6, column=0, sticky="e")

        tk.Label(detail_frame, text="Remaining Fees:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=7, column=0, sticky="e")

        tk.Label(detail_frame, text="Receipt Date:", font=('Arial Black', 12),
                 bg="light gray", ).grid(row=8, column=0, sticky="e")

        # =======Entries=======
        detail_frame.f_id_entry = tk.Entry(detail_frame, font=('Arial Black', 12),
                                           textvariable=self.F_ID)
        detail_frame.f_id_entry.grid(row=0, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.s_id_entry = tk.Entry(detail_frame, font=('Arial Black', 12),
                                           textvariable=self.S_ID)
        detail_frame.s_id_entry.grid(row=1, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.s_name_entry = tk.Entry(detail_frame, font=('Arial Black', 12),
                                             textvariable=self.S_NAME)
        detail_frame.s_name_entry.grid(row=2, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.c_id_entry = tk.Entry(detail_frame, font=('Arial Black', 12),
                                           textvariable=self.C_ID)
        detail_frame.c_id_entry.grid(row=3, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.course_name_entry = tk.Entry(detail_frame, font=('Arial Black', 12),
                                                  textvariable=self.COURSE_NAME)
        detail_frame.course_name_entry.grid(row=4, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.course_fees_entry = tk.Entry(detail_frame, font=('Arial Black', 12),
                                                  textvariable=self.COURSE_FEES)
        detail_frame.course_fees_entry.grid(row=5, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.fees_received_entry = tk.Entry(detail_frame, font=('Arial Black', 12),
                                                    textvariable=self.FEES_RECEIVED)
        detail_frame.fees_received_entry.grid(row=6, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.remaining_fees_entry = tk.Entry(detail_frame, font=('Arial Black', 12),
                                                     textvariable=self.REMAINING_FEES)
        detail_frame.remaining_fees_entry.grid(row=7, column=1, padx=3, pady=3, sticky="ew")

        detail_frame.receipt_date_entry = tk.Entry(detail_frame, font=('Arial Black', 12),
                                                   textvariable=self.RECEIPT_DATE)
        detail_frame.receipt_date_entry.grid(row=8, column=1, padx=3, pady=3, sticky="ew")

        # Bind button clicks to functions

        # button frame
        btn_frame = tk.Frame(detail_frame, bg="light gray", bd=10, relief=tk.GROOVE)
        btn_frame.place(x=0, y=320, width=430, height=169)

        insert_btn = tk.Button(btn_frame, command=self.insert_data, text="Add", bd=4,
                               font=('Arial Black', 12), width=17)
        insert_btn.grid(row=0, column=0, padx=2, pady=3)

        update_btn = tk.Button(btn_frame, command=self.update_data, text="Edit", bd=4,
                               font=('Arial Black', 12), width=17)
        update_btn.grid(row=0, column=1, padx=2, pady=3)

        delete_btn = tk.Button(btn_frame, command=self.delete_data, text="Delete", bd=4,
                               font=('Arial Black', 12), width=17)
        delete_btn.grid(row=1, column=0, padx=2, pady=3)

        clear_btn = tk.Button(btn_frame, command=self.clear_fields, text="Clear", bd=4,
                              font=('Arial Black', 12), width=17)
        clear_btn.grid(row=1, column=1, padx=2, pady=3)

        # Button for printing receipt
        print_btn = tk.Button(btn_frame, text="Pdf Receipt", bd=3, font=('Arial Black', 12), width=17)
        print_btn.grid(row=2, column=0, padx=2, pady=4)
        print_btn.config(command=self.pdf_print_receipt)
        print_btn = tk.Button(btn_frame, text="Print Receipt", bd=3, font=('Arial Black', 12), width=17)
        print_btn.grid(row=2, column=1, padx=2, pady=4)
        print_btn.config(command=self.print_receipt)

        # data frame
        data_frame = tk.Frame(master, bd=12, bg="light gray", relief=tk.GROOVE)
        data_frame.place(x=465, y=65, width=900, height=600)

        # search frame
        search_frame = tk.Frame(data_frame, bg="light gray", bd=7, relief=tk.GROOVE)
        search_frame.pack(side=tk.TOP, fill=tk.X)

        search_lbl = tk.Label(search_frame, text="Search", bg="light gray", font=("arial", 14))
        search_lbl.grid(row=0, column=0)

        search_in = ttk.Combobox(search_frame, textvariable=self.search_in,
                                 font=("arial", 13), state="readonly")
        search_in["values"] = ("F ID", "Student ID", "Student Name", "Course ID", "Course Name")
        search_in.grid(row=0, column=1, padx=10, pady=3)

        search_in_entry = tk.Entry(search_frame, textvariable=self.search_entry,
                                   font=('Arial Black', 12), bd=5, relief=tk.GROOVE)
        search_in_entry.grid(row=0, column=2, padx=10, pady=3)

        search_btn = tk.Button(search_frame,command=self.search_data, text="Search",
                               font=("arial", 14), bd=5, width=10, bg="light gray")
        search_btn.grid(row=0, column=3, padx=10, pady=3)
        show_all_btn = tk.Button(search_frame, text="Show All",
                                 font=("arial", 14), bd=5, width=10, bg="light gray")
        show_all_btn.grid(row=0, column=4, padx=10, pady=3)

        # database frame
        main_frame = tk.Frame(data_frame, bd=11, relief=tk.GROOVE)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # scroll bar
        y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
        x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

        self.fees_receipt = ttk.Treeview(main_frame, columns=("F ID", "Student ID", "Student Name",
                                                              "Course ID", "Course Name","Course Fees",
                                                              "Fees Received", "Remaining Fees", "Receipt Date"),
                                          yscrollcommand=y_scroll.set,
                                          xscrollcommand=x_scroll.set)

        y_scroll.config(command=self.fees_receipt.yview)
        x_scroll.config(command=self.fees_receipt.xview)

        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        self.fees_receipt.heading("#1", text="F ID")
        self.fees_receipt.heading("#2", text="Student ID")
        self.fees_receipt.heading("#3", text="Student Name")
        self.fees_receipt.heading("#4", text="Course ID")
        self.fees_receipt.heading("#5", text="Course Name")
        self.fees_receipt.heading("#6", text="Course Fees")
        self.fees_receipt.heading("#7", text="Fees Received")
        self.fees_receipt.heading("#8", text="Remaining Fees")
        self.fees_receipt.heading("#9", text="Receipt Date")

        self.fees_receipt['show'] = "headings"

        self.fees_receipt.column("#1", width=150)
        self.fees_receipt.column("#2", width=150)
        self.fees_receipt.column("#3", width=150)
        self.fees_receipt.column("#4", width=150)
        self.fees_receipt.column("#5", width=150)
        self.fees_receipt.column("#6", width=150)
        self.fees_receipt.column("#7", width=150)
        self.fees_receipt.column("#8", width=150)
        self.fees_receipt.column("#9", width=150)

        # Adjust column widths here if needed

        self.fees_receipt.pack(fill=tk.BOTH, expand=True)
        self.fetch_data()

        self.fees_receipt.bind('<<TreeviewSelect>>', self.on_fees_receipt_treeview_select)
# functions of database

    def fetch_data(self):
        db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
        mycursor = db.cursor()
        sql = "SELECT * FROM FEES_RECEIPT"
        mycursor.execute(sql)
        rows = mycursor.fetchall()
        if len(rows) != 0:
            self.fees_receipt.delete(*self.fees_receipt.get_children())
            for row in rows:
                self.fees_receipt.insert("", tk.END, values=row)
            db.commit()
        db.close()

    def insert_data(self):
        try:
            # Retrieve data from entry fields
            f_id_val = self.F_ID.get()
            s_id_val = self.S_ID.get()
            s_name_val = self.S_NAME.get()
            c_id_val = self.C_ID.get()
            course_name_val = self.COURSE_NAME.get()
            course_fees_val = self.COURSE_FEES.get()
            fees_received_val = self.FEES_RECEIVED.get()
            remaining_fees_val = self.REMAINING_FEES.get()
            receipt_date_val = self.RECEIPT_DATE.get()

            # Insert data into the database
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()
            sql = """INSERT INTO FEES_RECEIPT (F_ID, S_ID, S_NAME, C_ID, COURSE_NAME,COURSE_FEES, FEES_RECEIVED, REMAINING_FEES, RECEIPT_DATE) 
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""  # Adjusted SQL query with correct number of placeholders
            val = (f_id_val, s_id_val, s_name_val, c_id_val, course_name_val, course_fees_val,fees_received_val,
                   remaining_fees_val, receipt_date_val)
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

    def update_data(self):
        try:
            # Retrieve data from entry fields
            f_id_val = self.F_ID.get()
            s_id_val = self.S_ID.get()
            s_name_val = self.S_NAME.get()
            c_id_val = self.C_ID.get()
            course_name_val = self.COURSE_NAME.get()
            course_fees_val = self.COURSE_FEES.get()
            fees_received_val = self.FEES_RECEIVED.get()
            remaining_fees_val = self.REMAINING_FEES.get()
            receipt_date_val = self.RECEIPT_DATE.get()

            # Connect to the database
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()

            # Update data in the database
            sql = ("UPDATE FEES_RECEIPT SET F_ID=%s, S_ID=%s, S_NAME=%s, C_ID=%s, COURSE_NAME=%s,COURSE_FEES=%s, "
                   "FEES_RECEIVED=%s, "
                   "REMAINING_FEES=%s, RECEIPT_DATE=%s WHERE F_ID=%s")

            val = (f_id_val, s_id_val, s_name_val, c_id_val, course_name_val, course_fees_val,fees_received_val,
                   remaining_fees_val, receipt_date_val)

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
            print("Error occurred during update operation:", e)

    def delete_data(self):
        try:
            # Get the selected item from the Treeview
            selected_item = self.fees_receipt.focus()
            if selected_item:
                # Retrieve the ID of the selected item
                item_id = self.fees_receipt.item(selected_item)['values'][0]

                # Display a confirmation message box
                confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
                if confirm:
                    # Delete the record from the database
                    db = mysql.connector.connect(host="localhost", user="root",
                                                 password="gc@425508", database='master_db')
                    cursor = db.cursor()
                    sql = "DELETE FROM FEES_RECEIPT WHERE F_ID = %s"
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

    def clear_fields(self):
        # Clear all entry fields
        self.F_ID.set(0)
        self.S_ID.set(0)
        self.S_NAME.set('')
        self.C_ID.set(0)
        self.COURSE_NAME.set('')
        self.COURSE_FEES.set(0)
        self.FEES_RECEIVED.set(0)
        self.REMAINING_FEES.set(0)
        self.RECEIPT_DATE.set('')
        # Clear other fields similarly

    def show_all_data(self):
        # Fetch all records from the database
        # Update the Treeview with the fetched records
        self.fetch_data()

    def search_data(self):
        try:
            # Get the selected search criteria and search keyword
            search_criteria = self.search_in.get()
            keyword = self.search_entry.get()

            # Print search criteria and keyword for debugging
            print("Search Criteria:", search_criteria)
            print("Keyword:", keyword)

            # Connect to the database
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            mycursor = db.cursor()

            # Execute the search query based on the selected criteria
            if search_criteria == "F ID":
                sql = "SELECT * FROM FEES_RECEIPT WHERE F_ID LIKE %s"
            elif search_criteria == "Student ID":
                sql = "SELECT * FROM FEES_RECEIPT WHERE S_ID LIKE %s"
            elif search_criteria == "Student Name":
                sql = "SELECT * FROM FEES_RECEIPT WHERE S_NAME LIKE %s"
            elif search_criteria == "Course ID":
                sql = "SELECT * FROM FEES_RECEIPT WHERE C_ID LIKE %s"
            elif search_criteria == "Course Name":
                sql = "SELECT * FROM FEES_RECEIPT WHERE COURSE_NAME LIKE %s"

            # Print SQL query for debugging
            print("SQL Query:", sql)

            # Execute the query with the keyword
            mycursor.execute(sql, ('%' + keyword + '%',))
            rows = mycursor.fetchall()

            # Update the Treeview with the search results
            if len(rows) != 0:
                self.fees_receipt.delete(*self.fees_receipt.get_children())
                for row in rows:
                    self.fees_receipt.insert("", tk.END, values=row)
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

    def pdf_print_receipt(self):
        try:
            # Get the selected item from the Treeview
            selected_item = self.fees_receipt.focus()
            if selected_item:
                # Retrieve the values of the selected item
                values = self.fees_receipt.item(selected_item, 'values')

                # Create a PDF document
                pdf_file = f"receipt_{values[0]}.pdf"  # Using the receipt ID as the filename
                c = canvas.Canvas(pdf_file, pagesize=letter)

                # Set up the receipt content
                receipt_content = [
                         f"OMKAR IT SOLUTION",
                            "",
                         f"Receipt",
                          "",
                         f"F ID : {values[0]}",
                         f"Student ID: {values[1]}",
                         f"Student Name: {values[2]}",
                         f"Course ID: {values[3]}",
                         f"Course Name: {values[4]}",
                         f"Course Fees: {values[5]}",
                         f"Fees Received: {values[6]}",
                         f"Remaining Fees: {values[7]}",
                         f"Receipt Date: {values[8]}"
                ]

                # Set the starting y-coordinate for drawing text
                y = 650

                # Draw the receipt content on the PDF canvas
                for line in receipt_content:
                    c.drawString(150, y, line)
                    y -= 20  # Adjust y-coordinate for next line

                # Save the PDF
                c.save()

                # Show a success message
                messagebox.showinfo("Success", f"Receipt saved as '{pdf_file}'")

            else:
                # If no item is selected, show a warning message
                messagebox.showwarning("Warning", "Please select a record to print")

        except Exception as e:
            # Display error message using a messagebox
            messagebox.showerror("Error", f"Error occurred while printing receipt: {e}")

    def print_receipt(self):
        try:
            # Get the selected item from the Treeview
            selected_item = self.fees_receipt.focus()
            if selected_item:
                # Retrieve the values of the selected item
                values = self.fees_receipt.item(selected_item, 'values')

                # Create the receipt content
                receipt_content = [
                    f"Receipt",
                    "",
                    f"F ID : {values[0]}",
                    f"Student ID: {values[1]}",
                    f"Student Name: {values[2]}",
                    f"Course ID: {values[3]}",
                    f"Course Name: {values[4]}",
                    f"Course Fees: {values[5]}",
                    f"Fees Received: {values[6]}",
                    f"Remaining Fees: {values[7]}",
                    f"Receipt Date: {values[8]}"
                ]

                # Print each line of the receipt content on a separate line
                for line in receipt_content:
                    print(line)

            else:
                # If no item is selected, show a warning message
                messagebox.showwarning("Warning", "Please select a record to print")

        except Exception as e:
            # Display error message using a messagebox
            messagebox.showerror("Error", f"Error occurred while printing receipt: {e}")

    def on_fees_receipt_treeview_select(self, event):
        # Get the selected item
        selected_item = self.fees_receipt.focus()

        # Get the values of the selected item
        values = self.fees_receipt.item(selected_item, 'values')

        # Check if values has enough elements
        if len(values) >= 9:
            # Update entry fields with selected values
            self.F_ID.set(values[0])
            self.S_ID.set(values[1])
            self.S_NAME.set(values[2])
            self.C_ID.set(values[3])
            self.COURSE_NAME.set(values[4])
            self.COURSE_FEES.set(values[5])
            self.FEES_RECEIVED.set(values[6])
            self.REMAINING_FEES.set(values[7])
            self.RECEIPT_DATE.set(values[8])
        else:
            # Handle the case when the selected item doesn't have enough values
            # Clear all entry fields or take appropriate action
            self.clear_fields()


if __name__ == "__main__":
    master = tk.Tk()
    dashboard = FeesReceipt(master)
    master.mainloop()
