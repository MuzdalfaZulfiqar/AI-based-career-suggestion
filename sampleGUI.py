import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Assuming the Career class and career_graph dictionary are already defined

# Function to display career options based on user input
def recommend_career():
    # Capture user input for academic level and program
    name = entry_name.get()
    academic_level = academic_level_var.get()
    program = program_var.get()

    # Validate input (check if required fields are filled)
    if not name or academic_level == "Select" or program == "Select":
        messagebox.showerror("Input Error", "Please fill in all fields")
        return

    # Determine the education level
    if academic_level == "Intermediate":
        education = program
    elif academic_level == "A level":
        education = program

    # Career recommendation logic (simplified)
    recommended_careers = []
    for career_name, career in career_graph.items():
        if education in career.preReq:
            recommended_careers.append(career_name)

    # Display results in the GUI
    if recommended_careers:
        result_label.config(text=f"Recommended Careers for {name}:\n" + "\n".join(recommended_careers))
    else:
        result_label.config(text=f"No careers found for {name}.")


# Initialize the main Tkinter window
root = tk.Tk()
root.title("Career Recommendation System")

# Create input fields for user information
label_name = tk.Label(root, text="Enter your name:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_academic_level = tk.Label(root, text="Select your Academic Level:")
label_academic_level.grid(row=1, column=0, padx=10, pady=5, sticky="w")

academic_level_var = ttk.Combobox(root, values=["Select", "Intermediate", "A level"], state="readonly", width=27)
academic_level_var.set("Select")
academic_level_var.grid(row=1, column=1, padx=10, pady=5)

label_program = tk.Label(root, text="Select your Program:")
label_program.grid(row=2, column=0, padx=10, pady=5, sticky="w")

program_var = ttk.Combobox(root, values=["Select", "Pre-Medical", "Pre-Engineering", "ICS", "FA"], state="readonly",
                           width=27)
program_var.set("Select")
program_var.grid(row=2, column=1, padx=10, pady=5)

# Button to trigger career recommendation
recommend_button = tk.Button(root, text="Recommend Career", command=recommend_career)
recommend_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display the recommended careers
result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Run the Tkinter event loop
root.mainloop()
