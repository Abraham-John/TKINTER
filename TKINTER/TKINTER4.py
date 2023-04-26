import tkinter as tk
root = tk.Tk()
root.geometry("1800x700")

label = tk.Label(text='''The term anime [a·nuh·mei] is a Japanese colloquialism\n 
used as an abbreviation for the term “animation.” Generally in Japan,\n 
the word anime (written アニメ) is synonymous with animation of any kind from anywhere.\n
internationally, however, anime is typically referred to as animation that is produced from Japan.''' 

  , bg="grey",fg= "black" ,font="arial 13 bold italic" ,
   padx="200" , pady="200" , borderwidth="10" , relief="solid")



label.pack(side= "right",anchor="n", fill="x" , padx="100" , pady="50" )


root.mainloop()