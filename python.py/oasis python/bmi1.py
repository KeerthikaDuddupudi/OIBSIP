import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = weight_entry.get()
        height = height_entry.get()

        if not weight or not height:
            messagebox.showerror("Input Error", "Both weight and height must be provided.")
            result_label.config(text="", fg="black") 
            return
        
        weight = float(weight)
        height = float(height)

        if height <= 0:
            messagebox.showerror("Input Error", "Height must be greater than zero.")
            result_label.config(text="", fg="black")  
            return
        
        bmi = weight / height ** 2
        
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Healthy weight"
        else:
            category = "Overweight"
        
        result_label.config(text=f"Your BMI is {bmi:.2f}\nCategory: {category}", fg="black")
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")
        result_label.config(text="", fg="black")  # Clear previous result

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("700x700") 
root.config(bg="lightblue")

heading_label = tk.Label(root, text="BMI CALCULATOR", font=("Helvetica", 50, "bold"), bg="lightblue")
heading_label.pack(pady=10)

bmi_guide = (
    "BMI Weight Guide:\n\n" 
    "Underweight = less than 18.5\n"
    "Healthy weight = Between 18.5 and 25\n"
    "Overweight = Greater than 25"
)

guide_box = tk.Text(root, height=6, width=50, wrap=tk.WORD, borderwidth=3, relief="solid", bg="lightyellow", font=("Helvetica", 14))
guide_box.insert(tk.END, "BMI Category (Weight Guide):\n", "heading")  
guide_box.insert(tk.END, "\n") 
guide_box.insert(tk.END, "Underweight = less than 18.5\n"
                         "Healthy weight: Between 18.5 and 25\n"
                         "Overweight = Greater than 25")
guide_box.config(state=tk.DISABLED)

guide_box.tag_add("heading", "1.0", "1.end")
guide_box.tag_configure("heading", font=("Helvetica", 15, "bold"))

guide_box.pack(pady=40)

weight_label = tk.Label(root, text="Enter your weight (kg):", font=("Helvetica", 14), bg="#468cfd")
weight_label.pack(pady=5)
weight_entry = tk.Entry(root, font=("Helvetica", 14), width=15, bg="white")
weight_entry.pack(pady=5)

height_label = tk.Label(root, text="Enter your height (meters):", font=("Helvetica", 14), bg="#468cfd")
height_label.pack(pady=5)
height_entry = tk.Entry(root, font=("Helvetica", 14), width=15, bg="white")
height_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi, font=("Helvetica", 14), bg="#5fd3f0")
calculate_button.pack(pady=30)

result_label = tk.Label(root, text="", font=("normal", 18), bg="lightblue")
result_label.pack(pady=10)

root.mainloop()
