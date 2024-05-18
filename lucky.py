import tkinter as tk
import threading
import time
import random
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("CST 2024 Internatioal Students Hackathon Lucky Draw Program")

# Create a list of participants
def use_names():
    # Clear the participants_entry widget
    participants_entry.delete(0, tk.END)

    # Update the participants variable to an empty list
    global participants
    participants = []


# Create a list of participants in the range of 20 to 90
def use_random_numbers():
    # Generate random numbers between 20 to 120 for the number of participants
    global participants
    participants = list(range(random.randint(20, 90) + 1))

    # Update the participants_entry widget
    participants_entry.delete(0, tk.END)
    participants_entry.insert(0, ', '.join(map(str, participants)))
# Create a menu bar
menubar = tk.Menu(root)

# Create a menu item for using names
menubar.add_command(label="Use Names", command=use_names)

# Create a menu item for using random numbers
menubar.add_command(label="Use Random Numbers", command=use_random_numbers)

# Add the menu bar to the root window
root.config(menu=menubar)

# Set the window size
root.geometry("800x600")  # Replace with your desired dimensions

# Create a frame
frame = tk.Frame(root)
frame.pack(expand=True)

# Create a label for the winner
winner_label = tk.Label(frame, text="Winner(s): ", font=("Helvetica", 32))
winner_label.pack(pady=10)

# Create a label for the spinner
spinner_label = tk.Label(frame, text="", font=("Helvetica", 50))
spinner_label.pack(pady=10)

# Define colors for the spinner
spinner_colors = ["red", "blue", "green", "orange", "purple", "yellow"]


def spin():
    while spinner_label['text'] != "":
        for color in spinner_colors:
            spinner_label.config(fg=color)
            time.sleep(0.5)

# Create an entry to input the participants
participants_entry = tk.Entry(frame)
participants_entry.pack(pady=5)

#random numbers between 20 to 120 for the number of participants
participants = random.randint(20, 120)

# Create an entry to input the number of winners
winner_count_entry = tk.Entry(frame)
winner_count_entry.pack(pady=5)


# Define a function to calculate the winner
def calculate_winner():
    #stop spinner 
    spinner_label.config(text="")
    # Get the participants from the entry
    participants = participants_entry.get().split(',')

    # Remove leading and trailing whitespace from each name
    participants = [name.strip() for name in participants]

    # Get the number of winners
    winner_count_str = winner_count_entry.get()
    if not winner_count_str.isdigit():
        messagebox.showerror("Error", "Please enter a valid number of winners.")
        return
    winner_count = int(winner_count_str)

    # Check if the number of winners is larger than the number of participants
    if winner_count > len(participants):
        messagebox.showerror("Error", "The number of winners cannot be larger than the number of participants.")
        return

    # Calculate the winners
    winners = random.sample(participants, winner_count)

    # Update the winner label
    winner_label.config(text="Winner(s): " + ', '.join(winners))

    # Stop the spinner
    spinner_label.config(text="")



def select_winner():
    # Start the spinner
    spinner_label.config(text="Waiting for magic...")
    threading.Thread(target=spin, daemon=True).start()

    # Schedule the winner selection after a delay
    root.after(10000, calculate_winner)  # 2000 milliseconds = 2 seconds

# Create a button to select the winner
select_button = tk.Button(frame, text="Select Winner", command=select_winner, font=("Helvetica", 24), padx=10, pady=10)
select_button.pack(pady=10)

# Run the GUI
root.mainloop()