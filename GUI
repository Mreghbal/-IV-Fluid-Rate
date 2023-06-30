import tkinter as tk
from tkinter import messagebox

def calculate_iv_fluid_rate():
    try:
        # Get user input for weight, age, drop factor, infusion time, blood loss, and maintenance rate
        weight = float(weight_entry.get())
        age = int(age_entry.get())
        drop_factor = int(drop_factor_entry.get())
        infusion_time = int(infusion_time_entry.get())
        blood_loss = float(blood_loss_entry.get())
        maintenance_rate = float(maintenance_rate_entry.get())

        # Calculate IV fluid rate
        iv_rate_ml_h, drops_per_min = iv_fluid_rate(weight, age, drop_factor, infusion_time, blood_loss, maintenance_rate)

        # Show the calculated values in a message box
        result_text = "IV Fluid Rate: {} mL/h\nDrops per Minute: {} drops/min".format(iv_rate_ml_h, drops_per_min)
        messagebox.showinfo("IV Fluid Rate Calculation", result_text)

    except ValueError:
        messagebox.showerror("Error", "Invalid input!")

def iv_fluid_rate(weight, age, drop_factor, infusion_time, blood_loss, maintenance_rate):
    # Perform the calculations as before (same code as in the original script)
    weight_g = weight * 1000
    infusion_volume_ml = weight_g * 0.03 + blood_loss
    maintenance_volume_ml = weight * maintenance_rate * infusion_time / 60
    total_volume_ml = infusion_volume_ml + maintenance_volume_ml
    infusion_time_h = infusion_time / 60
    iv_rate_ml_h = total_volume_ml / infusion_time_h
    drops_per_min = iv_rate_ml_h * drop_factor / 60
    
    return iv_rate_ml_h, drops_per_min

# Create the main window
window = tk.Tk()
window.title("IV Fluid Rate Calculator")

# Create labels and entry fields for weight, age, drop factor, infusion time, blood loss, and maintenance rate
weight_label = tk.Label(window, text="Weight (in kg):")
weight_label.pack()
weight_entry = tk.Entry(window)
weight_entry.pack()

age_label = tk.Label(window, text="Age (in years):")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

drop_factor_label = tk.Label(window, text="Drop Factor (drops/mL):")
drop_factor_label.pack()
drop_factor_entry = tk.Entry(window)
drop_factor_entry.pack()

infusion_time_label = tk.Label(window, text="Infusion Time (in minutes):")
infusion_time_label.pack()
infusion_time_entry = tk.Entry(window)
infusion_time_entry.pack()

blood_loss_label = tk.Label(window, text="Blood Loss (in mL):")
blood_loss_label.pack()
blood_loss_entry = tk.Entry(window)
blood_loss_entry.pack()

maintenance_rate_label = tk.Label(window, text="Maintenance Rate (mL/kg/h):")
maintenance_rate_label.pack()
maintenance_rate_entry = tk.Entry(window)
maintenance_rate_entry.pack()

# Create a button to calculate the IV fluid rate
calculate_button = tk.Button(window, text="Calculate", command=calculate_iv_fluid_rate)
calculate_button.pack()

# Run the GUI event loop
window.mainloop()
