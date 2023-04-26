import tkinter as tk


root = tk.Tk()
root.geometry("500x400")

def click():
    print("you are gae")


f1 = tk.Frame(root , borderwidth = 2 , relief= "solid" , padx= 170)
f1.pack()

l1 = tk.Label(f1 , text="hey" ,)
l1.pack()

b1 = tk.Button(f1, text="CLICK IF YOU ARE NOT GAE" , borderwidth= 2 , relief = "solid" , 
    command= click)
b1.pack()


root.mainloop()