import tkinter as tk

from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ExpenseTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        # Initialize data structures
        self.expenses = []
        self.categories = set()

        # Create widgets
        self.label_amount = tk.Label(master, text="Amount:")
        self.entry_amount = tk.Entry(master)
        self.label_category = tk.Label(master, text="Category:")
        self.combo_category = ttk.Combobox(master, values=list(self.categories))
        self.label_notes = tk.Label(master, text="Notes:")
        self.entry_notes = tk.Entry(master)
        self.button_add_expense = tk.Button(master, text="Add Expense", command=self.add_expense)
        self.button_view_chart = tk.Button(master, text="View Spending Chart", command=self.view_spending_chart)

        # Place widgets using grid layout
        self.label_amount.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_amount.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.label_category.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.combo_category.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.label_notes.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_notes.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        self.button_add_expense.grid(row=3, column=0, columnspan=2, pady=10)
        self.button_view_chart.grid(row=4, column=0, columnspan=2, pady=10)

    def add_expense(self):
        amount = self.entry_amount.get()
        category = self.combo_category.get()
        notes = self.entry_notes.get()

        if amount and category:
            try:
                amount = float(amount)
                self.expenses.append({"amount": amount, "category": category, "notes": notes})
                self.categories.add(category)
                self.update_category_combobox()
                messagebox.showinfo("Expense Added", "Expense added successfully.")
                self.clear_entries()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid amount.")
        else:
            messagebox.showwarning("Missing Information", "Please enter both amount and category.")

    def update_category_combobox(self):
        self.combo_category["values"] = list(self.categories)

    def clear_entries(self):
        self.entry_amount.delete(0, tk.END)
        self.combo_category.set("")
        self.entry_notes.delete(0, tk.END)

    def view_spending_chart(self):
        if self.expenses:
            category_totals = {category: 0 for category in self.categories}

            for expense in self.expenses:
                category_totals[expense["category"]] += expense["amount"]

            labels = list(category_totals.keys())
            values = list(category_totals.values())

            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            plt.title("Spending Patterns")
            plt.show()
        else:
            messagebox.showinfo("No Data", "No expense data available.")

# Create the main application window
root = tk.Tk()
app = ExpenseTracker(root)

# Run the application
root.mainloop()
