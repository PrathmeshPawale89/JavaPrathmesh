import tkinter as tk
from tkinter import ttk, messagebox

class EmployeePerformanceExpertSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Performance Expert System")
        self.geometry("900x600")
        
        # Style configuration
        style = ttk.Style(self)
        style.theme_use("clam")
        
        self.employee_records = []
        self.setup_ui()
        
    def setup_ui(self):
        # -----------------------------
        # INPUT SECTION (Left / Top)
        # -----------------------------
        input_frame = ttk.LabelFrame(self, text="Evaluate New Employee", padding="15")
        input_frame.pack(fill="x", padx=15, pady=10)
        
        # Name Entry
        ttk.Label(input_frame, text="Employee Name:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.name_var = tk.StringVar()
        name_entry = ttk.Entry(input_frame, textvariable=self.name_var, width=30)
        name_entry.grid(row=0, column=1, sticky="w", pady=5, padx=10)
        
        # Rating Spinboxes
        scores_frame = ttk.Frame(input_frame)
        scores_frame.grid(row=1, column=0, columnspan=2, pady=10, sticky="w")
        
        attributes = [
            ("Quality of Work", "quality"),
            ("Punctuality & Attendance", "punctuality"),
            ("Teamwork & Communication", "teamwork"),
            ("Initiative & Problem Solving", "initiative")
        ]
        
        self.score_vars = {}
        for i, (label_text, key) in enumerate(attributes):
            ttk.Label(scores_frame, text=f"{label_text} (1-10):").grid(row=i, column=0, sticky="w", pady=5, padx=(0, 10))
            var = tk.IntVar(value=5) # Default score is 5
            spinbox = ttk.Spinbox(scores_frame, from_=1, to=10, textvariable=var, width=5, state="readonly")
            spinbox.grid(row=i, column=1, sticky="w", pady=5)
            self.score_vars[key] = var
            
        # Submit Button
        evaluate_btn = ttk.Button(input_frame, text="Evaluate & Save to Records", command=self.run_inference)
        evaluate_btn.grid(row=2, column=0, columnspan=2, pady=(15, 0))
        
        # -----------------------------
        # OUTPUT SECTION (Table)
        # -----------------------------
        table_frame = ttk.LabelFrame(self, text="Employee Knowledge Base Records", padding="15")
        table_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
        # Treeview (Table) setup
        columns = ("Name", "Quality", "Punctuality", "Teamwork", "Initiative", "Average", "Rating")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
        
        # Define Headings and Column widths
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "Name":
                self.tree.column(col, width=180, anchor="w")
            elif col == "Rating":
                self.tree.column(col, width=120, anchor="center")
            else:
                self.tree.column(col, width=90, anchor="center")
        
        # Scrollbar mapping
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
    def run_inference(self):
        """Inference Engine: Processes the inputs, applies the rules, and stores the facts."""
        name = self.name_var.get().strip()
        if not name:
            messagebox.showerror("Input Error", "Please enter an employee name before evaluating.")
            return
            
        # Gather facts
        q = self.score_vars["quality"].get()
        p = self.score_vars["punctuality"].get()
        t = self.score_vars["teamwork"].get()
        i = self.score_vars["initiative"].get()
        
        # Calculate heuristics
        avg_score = (q + p + t + i) / 4
        
        # --- KNOWLEDGE BASE (Rules) ---
        if avg_score >= 8.5 and q >= 9 and p >= 8 and t >= 8 and i >= 8:
            rating = "Outstanding"
        elif avg_score >= 7.5 and q >= 8:
            rating = "Excellent"
        elif avg_score >= 6 and q >= 6:
            rating = "Good"
        elif avg_score >= 4:
            rating = "Average"
        else:
            rating = "Poor"
            
        # Save deduced facts
        facts = {
            'name': name,
            'quality': q,
            'punctuality': p,
            'teamwork': t,
            'initiative': i,
            'average': avg_score,
            'rating': rating
        }
        
        # Store in systemic memory
        self.employee_records.append(facts)
        
        # Insert into Visual Table
        self.tree.insert("", "end", values=(
            facts['name'], 
            facts['quality'], 
            facts['punctuality'], 
            facts['teamwork'], 
            facts['initiative'], 
            f"{facts['average']:.2f}", 
            facts['rating']
        ))
        
        # Reset the form for the next employee
        self.name_var.set("")
        for var in self.score_vars.values():
            var.set(5) # Reset sliders to default
            
        # Notify User
        messagebox.showinfo("Inference Complete", f"{name} has been evaluated successfully.\n\nDeducted Rating: {rating}")

if __name__ == "__main__":
    app = EmployeePerformanceExpertSystem()
    app.mainloop()
