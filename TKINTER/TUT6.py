import tkinter as tk
root = tk.Tk()
root.geometry("500x300")

def click():
    print("addition is adding to numbers ")

f1 = tk.Frame(root, borderwidth= 2 , relief= "solid", padx=170)
f1.pack()

l1 = tk.Label(f1 , text="hey")
l1.pack()

b1 = tk.Button(f1 , text="addition" , borderwidth= 2 , relief = "solid" ,
   command= click )
b1.pack()

root.mainloop()