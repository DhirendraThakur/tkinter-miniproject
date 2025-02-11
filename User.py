import tkinter as tk

def add_user(frame, database):
     # Create a popup window inside the main application
    for widget in frame.winfo_children():
        widget.destroy()
    # add_user.title("Sign Up Window")
    # add_user.geometry("300x200")

    # Add content to the existing frame
    tk.Label(frame, text="User Name:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    username_field = tk.Entry(frame)
    username_field.pack(pady=5)

    tk.Label(frame, text="Address:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    address_field = tk.Entry(frame)
    address_field.pack(pady=5)

    tk.Label(frame, text="Email:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    email_field = tk.Entry(frame)
    email_field.pack(pady=5)

    tk.Label(frame, text="Password:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    password_field = tk.Entry(frame, show="*")
    password_field.pack(pady=5)
    

    tk.Button(frame, text="Submit", command=lambda: submit_data(frame, database, username_field, address_field, email_field, password_field)).pack(pady=10)
    
    # Example function for form submission
def submit_data(frame, database, username, address, email, password):
    username = username.get()
    address = address.get()
    email = email.get()
    password = password.get()
    
    if username and address and email and password:
        database.insert_user(username, address, email, password)
    # You can add database saving logic here
        for widget in frame.winfo_children():
            widget.destroy()  # Clear frame after submission
        tk.Label(frame, text="User Added Successfully!", font=("Arial", 14), bg="lightblue").pack(pady=10)
    else:
        
        tk.Label(frame, text="Please fill all the area!", font=("Arial", 14), bg="lightblue").pack(pady=10)