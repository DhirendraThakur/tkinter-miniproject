import tkinter as tk
from tkinter import ttk
from User import add_user  # Import function from User.py
from sqlite_GUI import display_city # Import function from sqlite_GUI
import database

# root = tk.Tk()
# root.title("Main Window")

# def open_window():
#     add_user(root)  # Call function from User.py
    

# Creating main Windows (Dashboard)    
app_window = tk.Tk()
app_window.title("Dashboard")
# Running the tkinter GUI with window size and placing it at the center of the screen
app_window.geometry("500x400")
app_window.configure(bg="#66f7ff")  # Soft blue background
app_window.resizable(False, False)
app_window.update_idletasks()
app_window.eval('tk::PlaceWindow . center')

def open_window():
    add_user(frame, database)
    
# ✅ Function for "Cities" Button
def open_cities():
    add_city(frame, database)  # Calls cities form

# Creating Stylish Header for Dashboard
header_label = tk.Label( app_window, text="Welcome to the Dashboard", font=("Arial", 16, "bold"), fg="White", bg= "#0073e6", padx=20, pady=10)
header_label.pack(fill="x")

# Frame to keep the widgets organized
frame = tk.Frame(app_window, bg="white", bd=5, relief="ridge") # Frame with padding and background color
frame.pack(pady=30, padx=20, fill="both", expand=True)

#updated button style
style= ttk.Style()
style.configure("tButton", font= ("Arial, 12"), padding=10)
style.map("TButton", foreground=[("active", "gray")], background=[("active","lightgray")])

# button with hover effect
def on_enter(e):
    e.widget.config(background="#005bb5", foreground="White")

def on_leave(e):
    e.widget.config(background="white", foreground="black")

button = tk.Button(frame, text="📝 Sign Up",font=("Arial", 12, "bold"), width=20, bg="white", fg= "black", command=open_window)
button.pack(pady=20)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

button = tk.Button(frame, text="📊 View Data", font=("Arial", 12, "bold"), width=20, bg="white", fg= "black", command=open_window)
button.pack(pady=20)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

button = tk.Button(frame, text=" Cities", font=("Arial", 12, "bold"), width=20, bg="white", fg= "black", command=open_cities)
button.pack(pady=20)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

# Database connection closed when the application window is closed
#When window is closed, Database connection is closed with the function on_closing
def on_closing():
    # con.close()
    app_window.destroy()


#Close event binding
app_window.protocol("WM_DELETE_WINDOW", on_closing)

app_window.mainloop()  