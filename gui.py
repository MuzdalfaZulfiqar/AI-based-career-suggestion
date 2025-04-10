import tkinter as tk
from tkinter import ttk, messagebox
from idlelib.multicall import expand_substates


# Your career data should be defined here, or import it if it's in a separate file

class CareerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Career Path Recommendation")
        self.root.geometry("600x600")

        # Title label
        ttk.Label(root, text="Career Path Recommendation", font=("Arial", 16)).pack(pady=10)

        # Name entry
        ttk.Label(root, text="Enter your name:").pack()
        self.name_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.name_var).pack()

        # Academic Level dropdown
        ttk.Label(root, text="Select your Academic Level:").pack()
        self.academic_level = tk.StringVar()
        academic_options = ["Intermediate", "A level"]
        self.academic_dropdown = ttk.Combobox(root, textvariable=self.academic_level, values=academic_options,
                                              state="readonly")
        self.academic_dropdown.pack()

        # Program dropdown, updated based on academic level
        ttk.Label(root, text="Select your Program:").pack()
        self.program_var = tk.StringVar()
        self.program_dropdown = ttk.Combobox(root, textvariable=self.program_var, state="readonly")
        self.program_dropdown.pack()

        # Bind event to update program options
        self.academic_dropdown.bind("<<ComboboxSelected>>", self.update_program_options)

        # Skills checkboxes
        ttk.Label(root, text="Select your Interests/Preferred Skills:").pack(pady=10)
        self.skills_vars = {}
        skills_list = ["Technology", "Computer", "Medical", "Communication", "Chemistry", "Physics", "Mathematics",
                       "Critical Thinking",
                       "Python", "Statistics", "Documentation", "Critical Analysis", "Argumentative", "Politics",
                       "Excel",
                       "Data Visualization", "Network Security", "Cryptography", "Risk Management", "Business Acumen",
                       "Project Management", "Strategic Planning", "Communication", "Medical Knowledge", "Patient Care"]

        skills_frame = ttk.Frame(root)
        skills_frame.pack()
        for skill in skills_list:
            var = tk.BooleanVar()
            cb = ttk.Checkbutton(skills_frame, text=skill, variable=var)
            cb.pack(anchor="w")
            self.skills_vars[skill] = var

        # Submit button
        ttk.Button(root, text="Submit", command=self.show_careers).pack(pady=20)

        # Results area
        self.result_text = tk.Text(root, height=10, wrap="word")
        self.result_text.pack(pady=10)

    def update_program_options(self, event):
        if self.academic_level.get() == "Intermediate":
            self.program_dropdown["values"] = ["Pre-medical", "Pre-Engineering", "ICS", "FA"]
        elif self.academic_level.get() == "A level":
            self.program_dropdown["values"] = ["Biology Major", "Engineering Major", "Computer Science Major"]

    def show_careers(self):
        name = self.name_var.get()
        academic_level = self.academic_level.get()
        program = self.program_var.get()
        selected_skills = [skill for skill, var in self.skills_vars.items() if var.get()]

        if not name or not academic_level or not program or not selected_skills:
            messagebox.showwarning("Incomplete Information", "Please fill in all the fields.")
            return

        # Determine eligible careers based on selected criteria (simplified version)
        eligible_careers = []
        for career in career_graph.values():
            if any(skill in career.skills for skill in selected_skills) and program in career.preReq:
                eligible_careers.append(career.name)

        self.result_text.delete(1.0, tk.END)
        if eligible_careers:
            self.result_text.insert(tk.END, "Recommended Careers:\n" + "\n".join(eligible_careers))
        else:
            self.result_text.insert(tk.END,
                                    "No careers match your criteria. Try selecting different skills or program.")


# Run the GUI
root = tk.Tk()
app = CareerGUI(root)
root.mainloop()
