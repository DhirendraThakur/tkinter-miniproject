import tkinter as tk
from User import add_user  # Import function from User.py
from sqlite_GUI import display_city # Import function from sqlite_GUI
import database

# root = tk.Tk()
# root.title("Main Window")

# def open_window():
#     add_user(root)  # Call function from User.py
    
def open_window():
    add_user(frame, database)
    
# ✅ Function for "Cities" Button
def open_cities():
    add_city(frame, database)  # Calls cities form
    
app_window = tk.Tk()
app_window.title("Dashboard")


# Running the tkinter GUI with window size and placing it at the center of the screen
app_window.geometry("500x400")
app_window.configure(bg="#f0f8ff")  # Soft blue background
app_window.resizable(False, False)
app_window.update_idletasks()
app_window.eval('tk::PlaceWindow . center')


# Frame to keep the widgets organized
frame = tk.Frame(app_window, padx=15, pady=15, bg="lightblue") # Frame with padding and background color
frame.grid(padx=10, pady=10)

button = tk.Button(frame, text="Sign Up", command=open_window)
button.pack(pady=20)

button = tk.Button(frame, text="View Data", command=open_window)
button.pack(padx=20)

button = tk.Button(frame, text="Cities", command=open_cities)
button.pack(padx=20)

# Database connection closed when the application window is closed
#When window is closed, Database connection is closed with the function on_closing
def on_closing():
    # con.close()
    app_window.destroy()


#Close event binding
app_window.protocol("WM_DELETE_WINDOW", on_closing)

app_window.mainloop()  