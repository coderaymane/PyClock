import tkinter as tk
from time import strftime

# 1- Create the main window:
root = tk.Tk()
root.title("Digital Clock")

# 2- Configure the clock's display:
label = tk.Label(root, font=("Arial", 75), background="black", foreground="lime")
label.pack(anchor="center")

# 3- Function to update time:
def update_time():
    current_time = strftime("%H:%M:%S") # Get the current time
    label.config(text=current_time) # Update the label
    label.after(1000, update_time) # Call the function again after one second

# 4- Start updating time:
update_time()

# 5- Run the application:
root.mainloop()