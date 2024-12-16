
# Import the necessary modules of Python
from tkinter import *   # GUI library
from tkinter import messagebox as mg, simpledialog as sm   # For dialog boxes

# Constants for GUI styling
BG_GRAY = "#ABB2B9"  # Button background color
BG_COLOR = "#17202A"  # Chat background color
TEXT_COLOR = "#EAECEE"  # Text color
FONT = "Helvetica 14"  # Default font style
FONT_BOLD = "Helvetica 13 bold"  # Bold font style

def extract_data(data="12,12"):
    """Extracts integers from a comma-separated string."""
    lis = data.split(",")  # Split input string by commas
    new = []
    for i in lis:
        try:
            new.append(int(i))  # Convert each item to an integer
        except ValueError:
            # Handle invalid input
            mg.showerror("Input Error", "Please enter valid comma-separated numbers.")
            return []
    return new

def send():
    """Handles user input, processes grades, and displays results."""
    # Initialize grade counters
    A1 = A = B = C = D = E = F = 0

    # Get user input
    user_input = e.get()
    print(f"User input: {user_input}")

    # Clear the text area if "clear" command is given
    if user_input.lower() == "clear":
        txt.delete('1.0', END)
        e.delete(0, END)
        return

    # Prompt user for maximum marks
    try:
        max_marks = sm.askinteger("Aitchz Grade Calculator", "Enter the Maximum Marks:")
        if max_marks is None:  # Handle cancel
            return
    except ValueError:
        mg.showerror("Input Error", "Please enter a valid integer for maximum marks.")
        return

    # Display user input
    txt.insert(END, "\nYou: " + user_input)

    # Extract data from input
    new = extract_data(user_input)
    if not new:  # Exit if input is invalid
        return

    present_students = len(new)  # Number of students

    # Grade calculation loop
    for i in new:
        if i > max_marks:
            e.delete(0, END)
            mg.showerror("Aitchz Grade Calculator", f"Number cannot be greater than {max_marks}.")
            txt.insert(END, "\nCal: Error found. This data was not processed. Try again.")
            txt.insert(END, "\n-------------------------------------------------END---------------------------------------------------")
            return
        elif i >= max_marks * 0.8:
            A1 += 1
        elif i >= max_marks * 0.7:
            A += 1
        elif i >= max_marks * 0.6:
            B += 1
        elif i >= max_marks * 0.5:
            C += 1
        elif i >= max_marks * 0.4:
            D += 1
        elif i >= max_marks * 0.33:
            E += 1
        else:
            F += 1

    # GPA calculation
    GPA = ((A1 * 6) + (A * 5) + (B * 4) + (C * 3) + (D * 2) + E) / present_students

    # Display results
    txt.insert(END, f"\nCal: A+ = {A1}, A = {A}, B = {B}, C = {C}, D = {D}, E = {E}, Fail = {F}, GPA = {GPA:.2f}")
    txt.insert(END, "\n-------------------------------------------------END-----------------------------------------------------")

    # Clear the input field
    e.delete(0, END)

def call(event):
    """Triggers the send function when the Enter key is pressed."""
    send()
    print(f"Key pressed: {event.keysym}")

# Create GUI for the chatbot
root = Tk()
root.title("Aitchz Grade Calculator")
root.geometry("670x620")  # Set window size
root.resizable(False, False)  # Disable resizing

# Add title label
label1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Aitchz Grade Calculator", font=FONT_BOLD, pady=10, width=20, height=1)
label1.grid(row=0)

# Add text area for displaying conversation
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

# Scrollbar for text area
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
scrollbar.config(command=txt.yview)
txt.config(yscrollcommand=scrollbar.set)

# Entry widget for user input
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

# Send button
send_button = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send)
send_button.grid(row=2, column=1)

# Bind the Enter key to the call function
root.bind("<Return>", call)

# Display welcome message
mg.showinfo("Aitchz Grade Calculator", "Welcome to Aitchz Grade Calculator developed by Aitchz.")

# Run the GUI application
root.mainloop()
