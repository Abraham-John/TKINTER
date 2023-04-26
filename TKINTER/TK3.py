import tkinter as tk
from PIL import Image , ImageTk

root = tk.Tk()
root.geometry("1080x720")

image = Image.open("weekd.jpg")
photo = ImageTk.PhotoImage(image)

label = tk.Label(text='''THE WEEKND''' 
  , bg="grey",fg= "black" ,font="arial 13 bold italic" ,
   padx="1200" , pady="50" , borderwidth="10" , relief="solid")
label.pack()

label= tk.Label(image=photo)
label.pack()



root.mainloop()




