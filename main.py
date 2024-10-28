import tkinter as tk
from tkinter import ttk, messagebox

class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        # Set a theme
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#800000')
        self.style.configure('TButton', background='#800000', font=('Arial', 10), foreground='black')
        self.style.configure('TLabel', background='#800000', font=('Arial', 16, 'bold'), foreground='black')
        self.style.configure('TitleLabel', background='#800000', font=('Arial', 16, 'bold'), foreground='white')
        self.style.configure('TEntry', font=('Arial', 12))
        self.style.configure('Treeview.Heading', font=('Arial', 12), foreground='black',
                             background='#800000')
        self.style.configure('Treeview', font=('Arial', 11))

        # Store student details
        self.id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.en_date_var = tk.StringVar()
        self.midterm_var = tk.StringVar()
        self.final_var = tk.StringVar()
        self.gpa_var = tk.StringVar()


        self.create_title_frame()
        self.create_student_records_frame()
        self.create_student_table_frame()

    def create_title_frame(self):
        title_frame = ttk.Frame(self.root, style='TFrame')
        title_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", pady=(10, 0))

        # Title label
        ttk.Label(title_frame)
        title_label = ttk.Label(title_frame, text="Student Management System", style='TLabel',foreground='white')
        title_label.grid(row=0, column=0, pady=10)
        title_frame.columnconfigure(0, weight=1)

    def create_student_records_frame(self):
        frame = ttk.Frame(self.root, padding=(10, 10, 10, 10), style='TFrame')
        frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Labels and entry widgets
        ttk.Label(frame, text="ID:", style='TLabel').grid(row=0, column=0, pady=5, sticky="w")
        ttk.Label(frame, text="Name:", style='TLabel').grid(row=1, column=0, pady=5, sticky="w")
        ttk.Label(frame, text="Gender:", style='TLabel').grid(row=2, column=0, pady=5, sticky="w")
        ttk.Label(frame, text="Age:", style='TLabel').grid(row=3, column=0, pady=5, sticky="w")
        ttk.Label(frame, text="En-date:", style='TLabel').grid(row=4, column=0, pady=5, sticky="w")
        ttk.Label(frame, text="Midterm:", style='TLabel').grid(row=5, column=0, pady=5, sticky="w")
        ttk.Label(frame, text="Final:", style='TLabel').grid(row=6, column=0, pady=5, sticky="w")
        ttk.Label(frame, text="GPA:", style='TLabel').grid(row=7, column=0, pady=5, sticky="w")

        ttk.Entry(frame, textvariable=self.id_var, style='TEntry').grid(row=0, column=1, pady=5, padx=5)
        ttk.Entry(frame, textvariable=self.name_var, style='TEntry').grid(row=1, column=1, pady=5, padx=5)
        ttk.Entry(frame, textvariable=self.gender_var, style='TEntry').grid(row=2, column=1, pady=5, padx=5)
        ttk.Entry(frame, textvariable=self.age_var, style='TEntry').grid(row=3, column=1, pady=5, padx=5)
        ttk.Entry(frame, textvariable=self.en_date_var, style='TEntry').grid(row=4, column=1, pady=5, padx=5)
        ttk.Entry(frame, textvariable=self.midterm_var, style='TEntry').grid(row=5, column=1, pady=5, padx=5)
        ttk.Entry(frame, textvariable=self.final_var, style='TEntry').grid(row=6, column=1, pady=5, padx=5)
        ttk.Entry(frame, textvariable=self.gpa_var, style='TEntry').grid(row=7, column=1, pady=5, padx=5)

        # Add Buttons
        ttk.Button(frame, text="Add", command=self.add_student, style='TButton').grid(row=8, column=0, pady=10)
        ttk.Button(frame, text="Update", command=self.update_student, style='TButton').grid(row=8, column=1, pady=10)

        ttk.Button(frame, text="Delete", command=self.delete_student, style='TButton').grid(row=9, column=0, pady=10)
        ttk.Button(frame, text="Calculate", command=self.calculate_gpa, style='TButton').grid(row=9, column=1, pady=10)

        ttk.Button(frame, text="Save", command=self.save_student, style='TButton').grid(row=10, column=0, pady=10)
        ttk.Button(frame, text="Clear", command=self.clear_fields, style='TButton').grid(row=10, column=1, pady=10)

    def create_student_table_frame(self):
        frame = ttk.Frame(self.root, padding=(10, 10, 10, 10), style='TFrame')
        frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Display student details
        columns = ("ID", "Name", "Gender", "Age", "En-date", "Midterm", "Final", "GPA")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", selectmode="browse", style='Treeview')

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=80)

        # Pack treeview
        self.tree.pack(fill="both", expand=1)

    def add_student(self):
        # Get input values
        student_data = (
            self.id_var.get(),
            self.name_var.get(),
            self.gender_var.get(),
            self.age_var.get(),
            self.en_date_var.get(),
            self.midterm_var.get(),
            self.final_var.get(),
            self.gpa_var.get()
        )

        # Validate inputs
        if not all(student_data):
            messagebox.showerror("Error", "Please enter all details")
            return

        # Add students to the table
        self.tree.insert("", "end", values=student_data)

        # Clear inputs
        self.clear_fields()

    def update_student(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showerror("Error", "Please select a student to update")
            return

        # Get input values
        student_data = (
            self.id_var.get(),
            self.name_var.get(),
            self.gender_var.get(),
            self.age_var.get(),
            self.en_date_var.get(),
            self.midterm_var.get(),
            self.final_var.get(),
            self.gpa_var.get()
        )

        # Validate inputs
        if not all(student_data):
            messagebox.showerror("Error", "Please enter all details")
            return

        # Update student's information in the table
        self.tree.item(selected_item, values=student_data)

        # Clear inputs
        self.clear_fields()

    def delete_student(self):
        selected_item = self.tree.selection()

        if not selected_item:
            messagebox.showerror("Error", "Please select a student to delete")
            return

        # Confirm deletion
        result = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this student?")
        if result:
            # Delete student's information from the table
            self.tree.delete(selected_item)

            # Clear inputs
            self.clear_fields()

    def calculate_gpa(self):
        # Implement GPA calculation
        messagebox.showinfo("GPA Calculation", "GPA calculation is not implemented yet")

    def save_student(self):
        # Implement saving logic
        messagebox.showinfo("Save", "Save functionality is not implemented yet")

    def clear_fields(self):
        # Clear inputs
        self.id_var.set("")
        self.name_var.set("")
        self.gender_var.set("")
        self.age_var.set("")
        self.en_date_var.set("")
        self.midterm_var.set("")
        self.final_var.set("")
        self.gpa_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)

    root.eval('tk::PlaceWindow . center')
    root.mainloop()
