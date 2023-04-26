import tkinter as tk
root = tk.Tk()
root.geometry("300x250")

def submit():
    
    st1 = palinEntry.get()
    st2 = st1[::-1]
    if (st1==st2):
        print("palindrome")
    else:
        print("not palindrome")


tk.Label(root,text="Enter a Sentence",padx=15,pady=10).grid()

palin = tk.StringVar()
palinEntry = tk.Entry(root,textvariable=palin)
palinEntry.grid(row=0,column=1)

tk.Button(root,text="submit",command=submit).grid(row=5,column=1)

root.mainloop()