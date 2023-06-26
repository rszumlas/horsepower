import tkinter as tk

import customtkinter as customtkinter


# Define the torque values corresponding to the horsepower figures
def create_torque_schema():
    torque_schema = []
    for rpm in range(0, 11001, 250):
        torque_schema.append([rpm, 0])
    return torque_schema

def hp_multiplier(rpm):
    if rpm <= 2000:
        return 0.00025 * rpm + 0.5
    elif rpm <= 8000:
        return 1
    elif rpm <= 10000:
        return 0.00005 * (rpm - 8000) + 1.0
    else:
        return 1.1

# Define a function to convert horsepower to torque using the mathematical formula
def convert_horsepower():
    torque_schema = create_torque_schema()

    # Calculate the torque values corresponding to the input horsepower using the formula
    matching_torque_values = []
    for rpm, torque in torque_schema:
        hp_entry_value = float(hp_entry.get())
        hp = hp_entry_value * hp_multiplier(rpm)
        if rpm == 0:
            calculated_torque = hp_entry_value * 10
        else:
            calculated_torque = (hp * 5252) / rpm
        matching_torque_values.append((rpm, int(calculated_torque)))

    # Update the torque output text widget with the matching torque values
    torque_output.delete(1.0, tk.END)
    for rpm, torque in matching_torque_values:
        formatted_str = "[{}, {}],\n".format(rpm, torque)
        torque_output.insert(tk.END, formatted_str)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def copy_text():
    """Copy the contents of the textbox to the clipboard."""
    root.clipboard_clear()
    root.clipboard_append(torque_output.get("1.0", "end"))

root = customtkinter.CTk()
root.geometry("500x500")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Create a label for horsepower input
hp_label = customtkinter.CTkLabel(master=frame, text="Enter desired brapapap amount:", font=("Roboto", 20))
hp_label.pack(padx=20, pady=10)

# Create a entry widget for horsepower input
hp_entry = customtkinter.CTkEntry(master=frame)
hp_entry.pack(padx=20, pady=10)

# Create a button to trigger the horsepower to torque conversion
convert_button = customtkinter.CTkButton(master=frame, text="Convert", command=convert_horsepower)
convert_button.pack(padx=20, pady=10)

# Create a label for torque output
torque_label = customtkinter.CTkLabel(master=frame, text="Corresponding torque values:", font=("Roboto", 20))
torque_label.pack(padx=20, pady=10)

# Create a text widget for torque output
torque_output = customtkinter.CTkTextbox(master=frame, font=("Roboto", 14))
torque_output.pack(padx=20, pady=10)

# Create a button to copy the contents of the textbox
copy_button = customtkinter.CTkButton(master=frame, text="Copy", command=copy_text)
copy_button.pack(padx=20, pady=10)

root.mainloop()