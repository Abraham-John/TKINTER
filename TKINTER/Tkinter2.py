import tkinter as tk
root = tk.Tk()
root.geometry("1200x720")

label = tk.Label(text='''Death is the irreversible cessation of all biological functions that sustain an organism. 
\nFor organisms with a brain, death can also be defined as the irreversible cessation of functioning of the
 whole brain,\nincluding brainstem, and brain death is sometimes used as a legal definition of death.''' 
  , bg="grey",fg= "black" ,font="arial 13 bold italic" ,
   padx="250" , pady="269" , borderwidth="10" , relief="solid")

label.pack()
 
 
root.mainloop() 