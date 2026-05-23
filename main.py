from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# List to store student data
students = []


# Function to Add Student
def add_student():
    student_id = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()

    if student_id == "" or name == "" or age == "" or course == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    students.append([student_id, name, age, course])

    tree.insert("", END, values=(student_id, name, age, course))

    clear_fields()

    messagebox.showinfo("Success", "Student Added Successfully!")


# Function to Clear Input Fields
def clear_fields():
    entry_id.delete(0, END)
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_course.delete(0, END)


# Function to Delete Student
def delete_student():
    selected_item = tree.selection()

    if not selected_item:
        messagebox.showwarning("Warning", "Please select a student")
        return

    tree.delete(selected_item)

    messagebox.showinfo("Success", "Student Deleted Successfully!")


# Main Window
root = Tk()
root.title("Student Management System")
root.geometry("700x500")
root.config(bg="lightblue")


# Title
title = Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 18, "bold"),
    bg="lightblue",
    fg="darkblue"
)
title.pack(pady=10)


# Frame for Inputs
frame = Frame(root, bg="lightblue")
frame.pack(pady=10)


# Student ID
label_id = Label(frame, text="Student ID", font=("Arial", 12), bg="lightblue")
label_id.grid(row=0, column=0, padx=10, pady=10)

entry_id = Entry(frame, font=("Arial", 12))
entry_id.grid(row=0, column=1, padx=10)


# Name
label_name = Label(frame, text="Name", font=("Arial", 12), bg="lightblue")
label_name.grid(row=1, column=0, padx=10, pady=10)

entry_name = Entry(frame, font=("Arial", 12))
entry_name.grid(row=1, column=1, padx=10)


# Age
label_age = Label(frame, text="Age", font=("Arial", 12), bg="lightblue")
label_age.grid(row=2, column=0, padx=10, pady=10)

entry_age = Entry(frame, font=("Arial", 12))
entry_age.grid(row=2, column=1, padx=10)


# Course
label_course = Label(frame, text="Course", font=("Arial", 12), bg="lightblue")
label_course.grid(row=3, column=0, padx=10, pady=10)

entry_course = Entry(frame, font=("Arial", 12))
entry_course.grid(row=3, column=1, padx=10)


# Buttons
button_frame = Frame(root, bg="lightblue")
button_frame.pack(pady=10)


add_button = Button(
    button_frame,
    text="Add Student",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=add_student
)
add_button.grid(row=0, column=0, padx=10)


delete_button = Button(
    button_frame,
    text="Delete Student",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    command=delete_student
)
delete_button.grid(row=0, column=1, padx=10)


clear_button = Button(
    button_frame,
    text="Clear Fields",
    font=("Arial", 12, "bold"),
    bg="purple",
    fg="white",
    command=clear_fields
)
clear_button.grid(row=0, column=2, padx=10)


# Table for Student Records
tree = ttk.Treeview(root, columns=("ID", "Name", "Age", "Course"), show="headings")

tree.heading("ID", text="Student ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Course", text="Course")

tree.column("ID", width=100)
tree.column("Name", width=150)
tree.column("Age", width=100)
tree.column("Course", width=150)

tree.pack(pady=20, fill=BOTH, expand=True)


# Run Application
root.mainloop()

