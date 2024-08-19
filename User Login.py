from tkinter import *
from tkinter import messagebox
login_window=Tk()
login_window.geometry("300x150+700+300")
login_window.title("OBS AY")




def login():
    AYE = ("AHMET", "AHMET123")
    if user_entry.get()==AYE[0] and password_entry.get()==AYE[1]:
        print("asd")
        messagebox.showinfo("Conclusion","Login Succesful")
    else:
        messagebox.showinfo("Conclusion","Login Unsuccesful")



user_name = Label(text="Username",font="Ariel 12")
user_name.place(x=25,y=10)

password = Label(text="Password",font="Ariel 12")
password.place(x=25,y=40)

user_entry=Entry()
user_entry.place(x=110,y=13)

password_entry=Entry()
password_entry.place(x=110,y=42)

login_button=Button(text="Login",command=login)
login_button.place(x=120,y=75)



login_window.mainloop()