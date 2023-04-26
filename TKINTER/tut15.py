import tkinter as tk
root= tk.Tk()
root.geometry("600x500")

def display_text():
    user_text = text.get("1.0","end")
    tk.Label(root, text=user_text).pack()


text = tk.Text(root,height=10)
text.pack()

tk.Button(root, text="display", command=display_text).pack()

root.mainloop()