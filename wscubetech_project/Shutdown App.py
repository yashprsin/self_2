from tkinter import *
import os


def restart():
    os.system("shutdown /r /t 1")


def restart_time():
    os.system("shutdown /r /t 20")


def logout():
    os.system("shutdown -l")


def shutdown():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")

r_button = Button(st, text="Restart", font=("Time New Roman", 22, "bold"), relief=RAISED, cursor="plus",
                  command=restart)
r_button.place(x=150, y=60, height=40, width=200)

rt_button = Button(st, text="Restart Time", font=("Time New Roman", 22, "bold"), relief=RAISED, cursor="plus",
                   command=restart_time)
rt_button.place(x=150, y=150, height=40, width=200)

lg_button = Button(st, text="Log Out", font=("Time New Roman", 22, "bold"), relief=RAISED, cursor="plus",
                   command=logout)
lg_button.place(x=150, y=230, height=40, width=200)

shut_button = Button(st, text="Shut Down", font=("Time New Roman", 22, "bold"), relief=RAISED, cursor="plus",
                     command=shutdown)
shut_button.place(x=150, y=310, height=40, width=200)

st.mainloop()
