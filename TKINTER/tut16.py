import tkinter as tk

root =  tk.Tk()

root.geometry("500x500")
Menu1=tk.Menu(root)
root.config(menu=Menu1)

fileMenu = tk.Menu(Menu1)
Menu1.add_cascade(label= "file")


root.mainloop()