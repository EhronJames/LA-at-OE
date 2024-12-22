import tkinter as tk
from tkinter import messagebox

inventory = {}

windows = tk.Tk()
windows.title("LA #30 Inventory System")

screen_width = windows.winfo_screenwidth()
screen_height = windows.winfo_screenheight()
window_width = 600
window_height = 600
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
windows.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
windows.configure(bg="#282828")

font_style = ("Arial", 12)

inventory_frame = tk.Frame(windows, bg="#282828")
inventory_frame.pack(padx=20, pady=20, fill="both", expand=True)

action_frame = tk.Frame(windows, bg="#282828")
action_frame.pack(padx=20, pady=10, fill="both", expand=True)

button_style = {
    "bg": "#3c3c3c",
    "fg": "white",
    "font": ("Helvetica", 14, "bold"),
    "width": 25,
    "height": 2,
    "relief": "flat",
    "bd": 0
}

label_style = {
    "bg": "#282828",
    "fg": "white",
    "font": ("Arial", 14, "bold")
}

entry_style = {
    "font": ("Arial", 12),
    "width": 30
}

def clear_frame():
    for widget in action_frame.winfo_children():
        widget.destroy()

def hide_inventory():
    for widget in inventory_frame.winfo_children():
        widget.destroy()

def show_inventory():
    hide_inventory()
    inventory_label = tk.Label(inventory_frame, text="ITEMS IN THE INVENTORY:", **label_style)
    inventory_label.grid(row=0, column=0, pady=5, padx=10, columnspan=2, sticky="nsew")
    tk.Label(inventory_frame, text="Item", **label_style).grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    tk.Label(inventory_frame, text="Quantity", **label_style).grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
    for idx, (item, data) in enumerate(inventory.items()):
        item_label = tk.Label(inventory_frame, text=item, **label_style)
        item_label.grid(row=idx+2, column=0, padx=10, pady=3, sticky="nsew")
        quantity_label = tk.Label(inventory_frame, text=data['Quantity'], **label_style)
        quantity_label.grid(row=idx+2, column=1, padx=10, pady=3, sticky="nsew")
    inventory_frame.grid_columnconfigure(0, weight=1)
    inventory_frame.grid_columnconfigure(1, weight=1)

def is_valid_quantity(quantity):
    return quantity.isdigit()

def is_valid_item_name(char):
    return char.isalpha() or char.isspace()

def validate_item_name_input(input_str):
    return all(is_valid_item_name(c) for c in input_str)

def find_item_case_insensitive(item_name):
    for key in inventory.keys():
        if key.lower() == item_name.lower():
            return key
    return None

def add_function():
    clear_frame()

    def add_item():
        item_added = item_name_entry.get().strip()
        quantity_added = quantity_entry.get()
        if not item_added or not quantity_added:
            messagebox.showinfo("Input Error", "Please provide both item name and quantity.")
            return
        if not is_valid_quantity(quantity_added):
            messagebox.showinfo("Input Error", "Quantity must be a valid number.")
            return
        if find_item_case_insensitive(item_added):
            messagebox.showinfo("Item Exists", f"Item {item_added} already exists!")
        else:
            inventory[item_added] = {'Quantity': quantity_added}
            messagebox.showinfo("Item Added", f"Added Item: {item_added}")

    tk.Label(action_frame, text="Enter Item Name:", **label_style).pack(pady=5)
    item_name_entry = tk.Entry(action_frame, **entry_style, validate="key")
    item_name_entry.pack(pady=5)
    item_name_entry.configure(validatecommand=(windows.register(validate_item_name_input), "%P"))
    tk.Label(action_frame, text="Enter Quantity:", **label_style).pack(pady=5)
    quantity_entry = tk.Entry(action_frame, **entry_style)
    quantity_entry.pack(pady=5)
    tk.Button(action_frame, text="Add Item", command=add_item, **button_style).pack(pady=10)

def remove_function():
    clear_frame()

    def remove_item():
        item_input = item_name_entry.get().strip()
        found_item = find_item_case_insensitive(item_input)
        if found_item:
            del inventory[found_item]
            messagebox.showinfo("Item Removed", f"{found_item} is removed from the inventory!")
        else:
            messagebox.showinfo("Item Not Found", f"The item {item_input} was not found!")

    tk.Label(action_frame, text="Enter Item Name to Remove:", **label_style).pack(pady=5)
    item_name_entry = tk.Entry(action_frame, **entry_style, validate="key")
    item_name_entry.pack(pady=5)
    item_name_entry.configure(validatecommand=(windows.register(validate_item_name_input), "%P"))
    tk.Button(action_frame, text="Remove Item", command=remove_item, **button_style).pack(pady=10)

def edit_function():
    clear_frame()

    def edit_item_name():
        item_input = item_name_entry.get().strip()
        new_name = new_name_entry.get().strip()
        found_item = find_item_case_insensitive(item_input)
        if found_item:
            if find_item_case_insensitive(new_name):
                messagebox.showinfo("Name Exists", f"The name {new_name} already exists!")
                return
            inventory[new_name] = inventory.pop(found_item)
            messagebox.showinfo("Item Renamed", f'Item "{found_item}" renamed to "{new_name}" successfully!')
        else:
            messagebox.showinfo("Item Not Found", f"The item {item_input} was not found!")

    def edit_item_quantity():
        item_input = item_name_entry.get().strip()
        new_quantity = new_quantity_entry.get()
        if not is_valid_quantity(new_quantity):
            messagebox.showinfo("Input Error", "Quantity must be a valid number.")
            return
        found_item = find_item_case_insensitive(item_input)
        if found_item:
            inventory[found_item]['Quantity'] = new_quantity
            messagebox.showinfo("Item Updated", f"Updated {found_item}'s quantity to {new_quantity}")
        else:
            messagebox.showinfo("Item Not Found", f"The item {item_input} was not found!")

    tk.Label(action_frame, text="Enter Item Name:", **label_style).pack(pady=5)
    item_name_entry = tk.Entry(action_frame, **entry_style, validate="key")
    item_name_entry.pack(pady=5)
    item_name_entry.configure(validatecommand=(windows.register(validate_item_name_input), "%P"))
    tk.Label(action_frame, text="Enter New Name:", **label_style).pack(pady=5)
    new_name_entry = tk.Entry(action_frame, **entry_style, validate="key")
    new_name_entry.pack(pady=5)
    new_name_entry.configure(validatecommand=(windows.register(validate_item_name_input), "%P"))
    tk.Label(action_frame, text="Enter New Quantity:", **label_style).pack(pady=5)
    new_quantity_entry = tk.Entry(action_frame, **entry_style)
    new_quantity_entry.pack(pady=5)
    tk.Button(action_frame, text="Rename Item", command=edit_item_name, **button_style).pack(pady=5)
    tk.Button(action_frame, text="Edit Quantity", command=edit_item_quantity, **button_style).pack(pady=5)

def intro_system():
    menu_frame = tk.Frame(windows, bg="#282828")
    menu_frame.pack(padx=20, pady=20)
    tk.Button(menu_frame, text="Add Item", command=add_function, **button_style).pack(side="left", padx=10, pady=5)
    tk.Button(menu_frame, text="Show Items", command=show_inventory, **button_style).pack(side="left", padx=10, pady=5)
    tk.Button(menu_frame, text="Remove Item", command=remove_function, **button_style).pack(side="left", padx=10, pady=5)
    tk.Button(menu_frame, text="Edit Item", command=edit_function, **button_style).pack(side="left", padx=10, pady=5)

intro_system()
windows.mainloop()

