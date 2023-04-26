import tkinter as tk
root = tk.Tk()
root.geometry("500x500")

def click():
    print("bruh")

l1 = tk.Label(root ,text="Hey").grid()

l2 = tk.Label(root , text="yoo").grid()

b1 = tk.Button(root, text="click me" , borderwidth= 2 , relief = "solid" ,
   command= click).grid(row=0 , column= 1 )

root.mainloop()
