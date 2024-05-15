import tkinter as tk
from tkinter import ttk,messagebox
import mysql.connector


class BatchMaster:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1365x800+0+0')
        self.master.title("BATCH MANAGEMENT SYSTEM")

        # ======title=====
        title = tk.Label(master, text="BATCH MANAGEMENT SYSTEM", font=("goudy old style ", 30, "bold"),
                         bg="#033054", fg="white")
        title.place(x=0, y=0, relwidth=1)

        # ============= Initialize other variables-=======
        self.B_ID = tk.IntVar()
        self.BATCH_Name = tk.StringVar()
        self.START_Time = tk.StringVar()
        self.END_Time = tk.StringVar()
        self.search_in_batch_c = tk.StringVar()
        self.search_in_batch_entry = tk.StringVar()
        self.total_batches = tk.StringVar()
        self.total_batches.set("Total Batches: 0")

        # =====================detail frame===============
        self.detail_frame = tk.LabelFrame(master, text="Enter Details:", bd=10,
                                          font=('Arial Black', 12), bg="light gray",
                                          relief=tk.GROOVE)
        self.detail_frame.place(x=0, y=65, width=450, height=615)

        # =============labels================
        tk.Label(self.detail_frame, text="Batch ID:", font=('Arial Black', 12),
                 bg="light gray").grid(row=0, column=0, sticky="e")

        tk.Label(self.detail_frame, text="Batch Name:", font=('Arial Black', 12),
                 bg="light gray").grid(row=1, column=0, sticky="e")

        tk.Label(self.detail_frame, text="Start Time:", font=('Arial Black', 12),
                 bg="light gray").grid(row=2, column=0, sticky="e")

        tk.Label(self.detail_frame, text="End Time:", font=('Arial Black', 12),
                 bg="light gray").grid(row=3, column=0, sticky="e")

        # ============Entries===========
        self.detail_frame.batch_id_entry = tk.Entry(self.detail_frame, font=('Arial Black', 12), textvariable=self.B_ID)
        self.detail_frame.batch_id_entry.grid(row=0, column=1, padx=3, pady=3, sticky="ew")

        self.detail_frame.batch_name_entry = tk.Entry(self.detail_frame, font=('Arial Black', 12), textvariable=self.BATCH_Name)
        self.detail_frame.batch_name_entry.grid(row=1, column=1, padx=3, pady=3, sticky="ew")

        # Create the combo boxes for start time
        self.detail_frame.start_time_hours_combo = ttk.Combobox(self.detail_frame, values=[str(i).zfill(2) for i in range(1, 13)],
                                                           font=('Arial Black', 12), state="readonly", width=6)
        self.detail_frame.start_time_hours_combo.grid(row=2, column=1, padx=(3, 2), pady=3, sticky="w")

        self.detail_frame.start_time_minutes_combo = ttk.Combobox(self.detail_frame,
                                                             values=[str(i).zfill(2) for i in range(0, 60, 5)],
                                                             font=('Arial Black', 12), state="readonly", width=4)
        self.detail_frame.start_time_minutes_combo.grid(row=2, column=1, padx=(110, 4), pady=3, sticky="wn")

        self.detail_frame.start_time_ampm_combo = ttk.Combobox(self.detail_frame, values=["AM", "PM"], font=('Arial Black', 12),
                                                          state="readonly", width=3)
        self.detail_frame.start_time_ampm_combo.grid(row=2, column=1, padx=(190, 2), pady=3, sticky="news")

        # Create the combo boxes for end time
        self.detail_frame.end_time_hours_combo = ttk.Combobox(self.detail_frame, values=[str(i).zfill(2) for i in range(1, 13)],
                                                         font=('Arial Black', 12), state="readonly", width=6)
        self.detail_frame.end_time_hours_combo.grid(row=3, column=1, padx=(3, 2), pady=3, sticky="w")

        self.detail_frame.end_time_minutes_combo = ttk.Combobox(self.detail_frame,
                                                           values=[str(i).zfill(2) for i in range(0, 60, 5)],
                                                           font=('Arial Black', 12), state="readonly", width=4)
        self.detail_frame.end_time_minutes_combo.grid(row=3, column=1, padx=(110, 2), pady=3, sticky="w")

        self.detail_frame.end_time_ampm_combo = ttk.Combobox(self.detail_frame, values=["AM", "PM"], font=('Arial Black', 12),
                                                        state="readonly", width=3)
        self.detail_frame.end_time_ampm_combo.grid(row=3, column=1, padx=(190, 3), pady=3, sticky="w")
        # ============ button frame==========
        btn_frame = tk.Frame(self.detail_frame, bg="light gray", bd=10, relief=tk.GROOVE)
        btn_frame.place(x=0, y=215, width=430, height=120)

        insert_btn = tk.Button(btn_frame, text="Add", bd=4, font=('Arial Black', 12), width=17)
        insert_btn.grid(row=0, column=0, padx=2, pady=3)
        insert_btn.config(command=self.insert_batch_data)

        update_btn = tk.Button(btn_frame, text="Edit", bd=4, font=('Arial Black', 12), width=17)
        update_btn.grid(row=0, column=1, padx=2, pady=3)
        update_btn.config(command=self.update_batch_data)

        delete_btn = tk.Button(btn_frame, text="Delete", bd=4, font=('Arial Black', 12), width=17)
        delete_btn.grid(row=1, column=0, padx=2, pady=3)
        delete_btn.config(command=self.delete_batch_data)

        clear_btn = tk.Button(btn_frame, text="Clear", bd=4, font=('Arial Black', 12), width=17)
        clear_btn.grid(row=1, column=1, padx=2, pady=3)
        clear_btn.config(command=self.clear_batch_fields)

    # =========== data view frame=========
        data_frame = tk.Frame(master, bd=12, bg="light gray", relief=tk.GROOVE)
        data_frame.place(x=465, y=65, width=900, height=600)

        # ======= Search frame============
        search_frame_batch = tk.Frame(data_frame, bg="light gray", bd=7, relief=tk.GROOVE)
        search_frame_batch.pack(side=tk.TOP, fill=tk.X)

        # =============Search Label=========
        search_lbl_batch = tk.Label(search_frame_batch, text="Search", bg="light gray", font=("arial", 14))
        search_lbl_batch.grid(row=0, column=0, padx=10, pady=5)

        # ==========Search In Combobox===========

        search_in_batch = ttk.Combobox(search_frame_batch, textvariable=self.search_in_batch_c, font=("arial", 13),
                                       state="readonly")
        search_in_batch["values"] = ("Batch ID", "Batch Name", "Start Time", "End Time")
        search_in_batch.grid(row=0, column=1, padx=10, pady=5)

        # ==============Search Entry==============
        search_in_entry_batch = tk.Entry(search_frame_batch, textvariable=self.search_in_batch_entry,
                                         font=('Arial Black', 12), bd=5, relief=tk.GROOVE)
        search_in_entry_batch.grid(row=0, column=2, padx=10, pady=5)

        # ===============Search Button==============
        search_btn_batch = tk.Button(search_frame_batch, text="Search", font=('Arial Black', 12), bd=4, width=10)
        search_btn_batch.grid(row=0, column=3, padx=10, pady=5)
        search_btn_batch.config(command=self.search_batch_data)

        # ================== Show All Button================
        show_all_btn_batch = tk.Button(search_frame_batch, text="Show All", font=('Arial Black', 12), bd=4, width=10)
        show_all_btn_batch.grid(row=0, column=4, padx=10, pady=5)
        show_all_btn_batch.config(command=self.fetch_batch_data)

        # ===========data view frame for batch=============
        view_frame = tk.Frame(data_frame, bg="light gray", bd=10, relief=tk.GROOVE)
        view_frame.place(x=10, y=70, width=870, height=500)

        scroll_x = tk.Scrollbar(view_frame, orient=tk.HORIZONTAL)
        scroll_y = tk.Scrollbar(view_frame, orient=tk.VERTICAL)

        self.batch_master = ttk.Treeview(view_frame, columns=("Batch ID", "Batch Name", "Start Time", "End Time"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x.config(command=self.batch_master.xview)
        scroll_y.config(command=self.batch_master.yview)

        self.batch_master.heading("Batch ID", text="Batch ID")
        self.batch_master.heading("Batch Name", text="Batch Name")
        self.batch_master.heading("Start Time", text="Start Time")
        self.batch_master.heading("End Time", text="End Time")

        self.batch_master['show'] = 'headings'

        self.batch_master.column("Batch ID", width=100)
        self.batch_master.column("Batch Name", width=200)
        self.batch_master.column("Start Time", width=200)
        self.batch_master.column("End Time", width=200)

        self.batch_master.pack(fill=tk.BOTH, expand=1)

        self.batch_master.bind('<<TreeviewSelect>>', self.on_batch_treeview_select)
        self.fetch_batch_data()
    # functions of database

    def fetch_batch_data(self):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            mycursor = db.cursor()
            sql = "SELECT * FROM BATCH_MASTER"
            mycursor.execute(sql)
            rows = mycursor.fetchall()
            if len(rows) != 0:
                self.batch_master.delete(*self.batch_master.get_children())
                for row in rows:
                    self.batch_master.insert("", tk.END, values=row)
                db.commit()
            db.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred while fetching data: {e}")

    def insert_batch_data(self):
        try:
            b_id_val = self.B_ID.get()
            batch_name_val = self.BATCH_Name.get()
            start_time_hour_val = self.detail_frame.start_time_hours_combo.get()
            start_time_minute_val = self.detail_frame.start_time_minutes_combo.get()
            start_time_ampm_val = self.detail_frame.start_time_ampm_combo.get()
            end_time_hour_val = self.detail_frame.end_time_hours_combo.get()
            end_time_minute_val = self.detail_frame.end_time_minutes_combo.get()
            end_time_ampm_val = self.detail_frame.end_time_ampm_combo.get()

            start_time_val = f"{start_time_hour_val}:{start_time_minute_val} {start_time_ampm_val}"
            end_time_val = f"{end_time_hour_val}:{end_time_minute_val} {end_time_ampm_val}"

            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()
            sql = "INSERT INTO BATCH_MASTER (B_ID, BATCH_NAME, START_TIME, END_TIME) VALUES (%s, %s, %s, %s)"
            val = (b_id_val, batch_name_val, start_time_val, end_time_val)
            cursor.execute(sql, val)
            db.commit()
            db.close()

            self.fetch_batch_data()
            self.clear_batch_fields()

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred during insert operation: {e}")
    def update_batch_data(self):
        try:
            b_id_val = self.B_ID.get()
            batch_name_val = self.BATCH_Name.get()
            start_time_hour_val = self.detail_frame.start_time_hours_combo.get()
            start_time_minute_val = self.detail_frame.start_time_minutes_combo.get()
            start_time_ampm_val = self.detail_frame.start_time_ampm_combo.get()
            end_time_hour_val = self.detail_frame.end_time_hours_combo.get()
            end_time_minute_val = self.detail_frame.end_time_minutes_combo.get()
            end_time_ampm_val = self.detail_frame.end_time_ampm_combo.get()

            start_time_val = f"{start_time_hour_val}:{start_time_minute_val} {start_time_ampm_val}"
            end_time_val = f"{end_time_hour_val}:{end_time_minute_val} {end_time_ampm_val}"

            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()

            sql = "UPDATE BATCH_MASTER SET BATCH_NAME=%s, START_TIME=%s, END_TIME=%s WHERE B_ID=%s"

            val = (batch_name_val, start_time_val, end_time_val, b_id_val)

            cursor.execute(sql, val)
            db.commit()
            db.close()

            self.fetch_batch_data()
            self.clear_batch_fields()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during update operation:\n{e}")

    def delete_batch_data(self):
        try:
            selected_item = self.batch_master.focus()
            if selected_item:
                item_id = self.batch_master.item(selected_item)['values'][0]

                confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record?")
                if confirm:
                    db = mysql.connector.connect(host="localhost",
                                                 user="root",
                                                 password="gc@425508",
                                                 database='master_db')
                    cursor = db.cursor()
                    sql = "DELETE FROM BATCH_MASTER WHERE B_ID = %s"
                    cursor.execute(sql, (item_id,))
                    db.commit()
                    db.close()

                    self.fetch_batch_data()

                    messagebox.showinfo("Success", "Record deleted successfully")
            else:
                messagebox.showwarning("Warning", "Please select a record to delete")

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred during delete operation: {e}")

    def search_batch_data(self):
        try:
            search_criteria = self.search_in_batch_c.get()
            keyword = self.search_in_batch_entry.get()

            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()

            if search_criteria == "Batch ID":
                sql = "SELECT * FROM BATCH_MASTER WHERE B_ID LIKE %s"
            elif search_criteria == "Batch Name":
                sql = "SELECT * FROM BATCH_MASTER WHERE BATCH_NAME LIKE %s"
            elif search_criteria == "Start Time":
                sql = "SELECT * FROM BATCH_MASTER WHERE START_TIME LIKE %s"
            elif search_criteria == "End Time":
                sql = "SELECT * FROM BATCH_MASTER WHERE END_TIME LIKE %s"
            else:
                messagebox.showwarning("Invalid Search Criteria", "Please select a valid search criteria")
                db.close()
                return

            cursor.execute(sql, ('%' + keyword + '%',))
            rows = cursor.fetchall()

            if len(rows) != 0:
                self.batch_master.delete(*self.batch_master.get_children())
                for row in rows:
                    self.batch_master.insert("", tk.END, values=row)
                db.commit()
            else:
                messagebox.showinfo("No Results", "No matching records found")

            db.close()

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred during search operation: {e}")

    def clear_batch_fields(self):
        self.B_ID.set(0)
        self.BATCH_Name.set('')
        self.START_Time.set('')
        self.END_Time.set('')

    def on_batch_treeview_select(self, event=None):
        selected_item = self.batch_master.focus()
        values = self.batch_master.item(selected_item, 'values')

        if values:
            self.B_ID.set(values[0])
            self.BATCH_Name.set(values[1])
            self.START_Time.set(values[2])
            self.END_Time.set(values[3])

            # Split the start time and end time into hours, minutes, and AM/PM
            start_time_parts = values[2].split()
            end_time_parts = values[3].split()

            # Set values for start time combo boxes
            start_time_hours, start_time_minutes = start_time_parts[0].split(':')
            self.detail_frame.start_time_hours_combo.set(start_time_hours)
            self.detail_frame.start_time_minutes_combo.set(start_time_minutes)
            self.detail_frame.start_time_ampm_combo.set(start_time_parts[1])

            # Set values for end time combo boxes
            end_time_hours, end_time_minutes = end_time_parts[0].split(':')
            self.detail_frame.end_time_hours_combo.set(end_time_hours)
            self.detail_frame.end_time_minutes_combo.set(end_time_minutes)
            self.detail_frame.end_time_ampm_combo.set(end_time_parts[1])
        else:
            self.clear_batch_fields()

    def update_total_batches_label(self):
        try:
            db = mysql.connector.connect(host="localhost", user="root", password="gc@425508", database='master_db')
            cursor = db.cursor()
            sql = "SELECT COUNT(*) FROM BATCH_MASTER"
            cursor.execute(sql)
            total = cursor.fetchone()[0]
            self.total_batches.set(f"Total Batches: {total}")
            db.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred while fetching total batches: {e}")


if __name__ == "__main__":
    master = tk.Tk()
    dashboard = BatchMaster(master)
    master.mainloop()
