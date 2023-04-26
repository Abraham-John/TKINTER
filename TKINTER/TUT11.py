import tkinter as tk
root = tk.Tk()
root.geometry("500x500")

def submit():
    print(radio.get())
    print(check.get())

tk.Label(root, text="What is your favourite anime").pack()

radio = tk.StringVar()
radio.set("r")

check = tk.IntVar()

tk.Radiobutton(root, text="Naruto", variable= radio, value=" grow up kiddo" ).pack()
tk.Radiobutton(root, text="Bleach", variable= radio, value="GREAT CHOICE" ).pack()
tk.Radiobutton(root, text="One piece", variable= radio, value="YES sir" ).pack()
tk.Checkbutton(root, text="confirm", variable=check).pack()


tk.Button(root, text= "submit" ,command=submit).pack()


root.mainloop()
