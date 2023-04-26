import tkinter as tk
root = tk.Tk()
root.geometry("500x500")

def submit():
    with open("student_Data.csv" ,"a") as f:
        f.write(f"Name : {NameEntry.get()}, Class : {ClassEntry.get()}, Section : {SectionEntry  .get()} , Year : {YearEntry.get()}\n")
        
tk.Label(root, text="details",padx=20,pady=15).grid()

tk.Label(root, text="Name").grid(row=1,column=0)
tk.Label(root, text="Class").grid(row=2,column=0)
tk.Label(root, text="Section").grid(row=3,column=0)
tk.Label(root, text="Year").grid(row=4,column=0)

Name = tk.StringVar
Class = tk.StringVar
Section = tk.StringVar
Year = tk.StringVar

NameEntry = tk.Entry(root,textvariable= Name )
ClassEntry = tk.Entry(root, textvariable=Class)
SectionEntry = tk.Entry(root, textvariable=Section)
YearEntry = tk.Entry(root, textvariable=Year)

NameEntry.grid(row=1,column=1)
ClassEntry.grid(row=2,column=1)
SectionEntry.grid(row=3,column=1)
YearEntry.grid(row=4,column=1)

tk.Button(root,text="submit",command=submit).grid(row=5,column=1)

root.mainloop()