import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pymongo
import os

# connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["emp_db"]
employee = db["employee"]

# function to insert EMPLOYEE data into MongoDB
def insert_employe(empid, name, age, designation, contact, address, photo):
     employe = {"empid":empid,
               "name": name,
               "age": age,
               "designation":designation,
               "contact":contact,
               "address":address,
               "photo": photo}
    employee.insert_one(employe)
    messagebox.showinfo("SUCCESS", "EMPLOYEE DATA INSERTED SUCCESSFULLY!")




# function to handle photo selection
def select_photo():
    photo_path = filedialog.askopenfilename()
    photo_path_var.set(photo_path)

# function to handle form submission
def submit_form():
    empid = empid_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    designation = designation_entry.get()
    contact = contact_entry.get()
    address = address_entry.get()
    photo = photo_path_var.get()
    if not empid or not name or not age or not designation or not contact or not address or not photo:
        messagebox.showwarning("ERROR", "PLEASE FILL IN ALL FIELDS!")
        return
    insert_employe(empid, name, age, designation, contact, address, photo)

# create the main window
root = tk.Tk()
root.title("EMPLOYEE ID DATA")

# create the form widgets

empid_label = tk.Label(root, text="EMP. ID:")
empid_label.grid(row=0, column=0, padx=5, pady=5)
empid_entry = tk.Entry(root)
empid_entry.grid(row=0, column=1, padx=5, pady=5)

name_label = tk.Label(root, text="NAME:")
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=5, pady=5)

age_label = tk.Label(root, text="AGE:")
age_label.grid(row=2, column=0, padx=5, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=5, pady=5)

designation_label = tk.Label(root, text="DESIGNATION:")
designation_label.grid(row=3, column=0, padx=5, pady=5)
designation_entry = tk.Entry(root)
designation_entry.grid(row=3, column=1, padx=5, pady=5)

contact_label = tk.Label(root, text="CONTACT:")
contact_label.grid(row=4, column=0, padx=5, pady=5)
contact_entry = tk.Entry(root)
contact_entry.grid(row=4, column=1, padx=5, pady=5)

address_label = tk.Label(root, text="ADDRESS:")
address_label.grid(row=5, column=0, padx=5, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=5, column=1, padx=5, pady=5)


photo_label = tk.Label(root, text="PHOTO:")
photo_label.grid(row=6, column=0, padx=5, pady=5)
photo_path_var = tk.StringVar()
photo_path_var.set("")
photo_path_entry = tk.Entry(root, textvariable=photo_path_var)
photo_path_entry.grid(row=6, column=1, padx=5, pady=5)
photo_button = tk.Button(root, text="Select Photo", command=select_photo)
photo_button.grid(row=6, column=2, padx=5, pady=5)

submit_button = tk.Button(root, text="INSERT", command=submit_form)
submit_button.grid(row=8, column=1, padx=5, pady=5)

 

root.mainloop()
