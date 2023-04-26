import tkinter as tk
root= tk.Tk()
root.geometry("600x500")
 
pl_list= ("Python","JAVA","JAVASCRIPT","C","C++")
list_enter = tk.StringVar(value= pl_list)

lbx = tk.Listbox(root,height=7,width=30,selectmode="SINGLE", listvariable=list_enter)
lbx.pack()




root.mainloop()