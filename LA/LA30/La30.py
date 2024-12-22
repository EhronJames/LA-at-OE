print("La:30")
import tkinter as tk

web_title = "OOP"
name = "ehron, jims"
section = "BSIT-2A"
web_tittle = "OOP"
root = tk.Tk()
root.title(f"{web_title}")
root.geometry("500x300")
root.configure(bg="white")

label = tk.Label(root, text=f"{web_title} LA29 {name} {section}")
label.grid(row=0, column=0)

def display_text():
    print("My favorite anime is Robin dude")

button = tk.Button(root, text="Spank me Daddy", command=display_text)
button.grid(row=2, column=0)

root.mainloop()
