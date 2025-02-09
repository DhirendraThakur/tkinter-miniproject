import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox


# Function to create a connection to the database
def create_connection():
    con = sqlite3.connect('cities.db')  # Connect to the database
    cur = con.cursor()  # Create a cursor object to execute SQL queries

    #Create the cities table if it doesn't already exist
    cur.execute('''CREATE TABLE IF NOT EXISTS cities_table (
                        city_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city_name TEXT NOT NULL)''')
    con.commit()
    return con, cur

# Function to insert a new city into the db
def add_city():
    
    new_city = input_city.get()  # Get the city name from the entry widget
    if new_city:  # Check if the city name isn't empty
        cur.execute("INSERT INTO cities_table (city_name) VALUES (?)", (new_city,))
        con.commit()
        input_city.delete(0, tk.END)  # Entry box cleared after inserting names
        messagebox.showinfo("City added", f" '{new_city}' added!")

        #Ato-refresh city lists after adding a new city
        
    else:
        messagebox.showwarning("Oops!", "Enter a city's name")


#  Function that displays all the cities from the db(cities.db)
def display_city():
    cur.execute("SELECT city_name FROM cities_table")  # Query to fetch all cities
    city_records = cur.fetchall()  # Fetch all records from the result
    
    city_display.delete("1.0", tk.END)  # Clear the text widget before displaying the cities
    #city_display.insert(tk.END, "== city List  ===\n")  #Title addition 
    
    for city_name, in city_records:   #Loop through the records and insert them into the text widget
        city_display.insert(tk.END, f"-{city_name}\n")  # Insert the city name

# Connection and cursor initialization
con, cur = create_connection()

# GUI window creation
app_window = tk.Tk()
app_window.title("City List")


# Running the tkinter GUI with window size and placing it at the center of the screen
app_window.geometry("500x400")
app_window.configure(bg="#f0f8ff")  # Soft blue background
app_window.resizable(False, False)
app_window.update_idletasks()
app_window.eval('tk::PlaceWindow . center')


# Frame to keep the widgets organized
frame = tk.Frame(app_window, padx=15, pady=15, bg="lightblue") # Frame with padding and background color
frame.grid(padx=10, pady=10)


# Label to display the list of cities
label_cities = tk.Label(frame, text="Cities Details:", font=("Arial	", 16, "bold"), bg="Black", fg="LightBlue")
label_cities.grid(row=0, column=0, columnspan=3, pady=(4, 11), sticky="n")


# Scrollbar for the text widget
scrollbar = tk.Scrollbar(frame)
scrollbar.grid(row=1, column=2, sticky="nsw")

# Text widget to display cities with scrollbar
city_display = tk.Text(frame, width=40, height=12, wrap="word", yscrollcommand=scrollbar.set)
city_display.grid(row=1, column=0, columnspan=2, pady=5)

# Configure the scrollbar to work with the text widget
scrollbar.config(command=city_display.yview)

# Label and Entry widget to add a new city
label_addcity = tk.Label(frame, text="Enter a New City:", font=("Arial", 10,"bold" ), bg="white")
label_addcity.grid(row=2, column=0, sticky="e", padx=5, pady=5)

input_city = ttk.Entry(frame, width=30)
input_city.grid(row=2, column=1, padx=5, pady=5)

# Add city name to the database with the button
add_button = ttk.Button(frame, text="Add City",  command=add_city)
add_button.grid(row=1, column=3, columnspan=2, padx=5, pady=(0,80), sticky="ew")

# Display cities from the database with the button
display_button = ttk.Button(frame, text="Show Cities", command=display_city)
display_button.grid(row=1, column=3, columnspan=2, padx=5, pady=(0), sticky="ew")

# Database connection closed when the application window is closed
#When window is closed, Database connection is closed with the function on_closing
def on_closing():
    con.close()
    app_window.destroy()


#Close event binding
app_window.protocol("WM_DELETE_WINDOW", on_closing)

app_window.mainloop()  # Run the tkinter main loop