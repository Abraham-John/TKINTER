import tkinter as tk
root = tk.Tk()
root.geometry("410x640")
root.resizable(False,True)
root.config(bg="black")

eqn = ""

def show(value):
    global eqn
    eqn+=value
    l1.config(text= eqn)

def clear():
    global eqn
    eqn = ""
    l1.config(text= eqn)

def calculate():
    global eqn
    result = ""
    if eqn !="":
        try:
            result= eval(eqn)   
        except:
            result= "ERROR_404!!!"
            eqn = ""
    l1.config(text=result)

l1 = tk.Label(root,text="",width=50,height=5,font="arial")
l1.pack()

tk.Button(root,text="C", width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="black",bg="#3697f5",command=lambda:clear()).place(x=10,y=140)
tk.Button(root,text="**",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("**")).place(x=110,y=140)
tk.Button(root,text="%", width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("%")).place(x=210,y=140)
tk.Button(root,text="/", width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="#09dd09",bg="#2a2d36",command=lambda:show("/")).place(x=310,y=140)

tk.Button(root,text="7",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("7")).place(x=10,y=240)
tk.Button(root,text="8",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("8")).place(x=110,y=240)
tk.Button(root,text="9",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("9")).place(x=210,y=240)
tk.Button(root,text="*",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="#09dd09",bg="#2a2d36",command=lambda:show("*")).place(x=310,y=240)

tk.Button(root,text="4",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("4")).place(x=10,y=340)
tk.Button(root,text="5",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("5")).place(x=110,y=340)
tk.Button(root,text="6",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("6")).place(x=210,y=340)
tk.Button(root,text="-",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="#09dd09",bg="#2a2d36",command=lambda:show("-")).place(x=310,y=340)

tk.Button(root,text="1",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("1")).place(x=10,y=440)
tk.Button(root,text="2",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("2")).place(x=110,y=440)
tk.Button(root,text="3",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("3")).place(x=210,y=440)
tk.Button(root,text="+",width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="#09dd09",bg="#2a2d36",command=lambda:show("+")).place(x=310,y=440)

tk.Button(root,text="+/-",width=3,height=1,font=("arial",   29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("+/-")).place(x=10,y=540)
tk.Button(root,text="0",  width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show("0")).place(x=110,y=540)
tk.Button(root,text=".",  width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#2a2d36",command=lambda:show(".")).place(x=210,y=540)
tk.Button(root,text="=",  width=3, height=1, font=("arial", 29, "bold"),bd=5,fg="white",bg="#018301",command=lambda:calculate()).place(x=310,y=540)

root.mainloop()
 