import tkinter as tk
root = tk.Tk()
root.geometry("300x250")
root.title("LOGIN FORMS")

def submit():
    with open("login_form.csv","a") as f:
        f.write(f"user name : {usernameEntry.get()} , password : {passwordEntry.get()} ,checkbutton : {check.get()}\n")

tk.Label(root, text="Login" , padx=20,pady=15).grid()

tk.Label(root, text="User Name ").grid(row=1,column=0)
tk.Label(root, text="Password  ").grid(row=5,column=0)

username = tk.StringVar
password = tk.StringVar     
check = tk.IntVar()

usernameEntry = tk.Entry(root, textvariable=username)
passwordEntry = tk.Entry(root, textvariable=password)

usernameEntry.grid(row=1,column=2 ,pady=15)
passwordEntry.grid(row=5,column=2,pady=15) 

tk.Checkbutton(root, text="Keep me logged in", variable=check).grid(row=7,column=2,pady=15)
tk.Button(root, text="submit", command=submit).grid(row=9,column=2)


root.mainloop()
