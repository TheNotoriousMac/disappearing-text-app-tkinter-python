from tkinter import *
import time

timer_start = None

def start():
    print("START")
    global timer_start
    timer_start = time.time()
    reset_timer()


def clear_text():
    print("DELETED")
    entry.delete('1.0', END)


def reset_timer():
    global timer_start
    entry.after_cancel(timer_start)
    timer_start = entry.after(5000, clear_text)


def on_key_pressed(event):
    reset_timer()

window = Tk()
window.title = "Disappearing Text App"
window.config(padx=10, pady=10)

heading = Label(text="Disappearing Text App", font=("Arial", 24, "bold"))
heading.pack(pady=10,padx=10)

instructions_label = Label(text="Starting typing or else after 5 seconds your text will disappear!", font=("Arial", 12))
instructions_label.pack(padx=10)

entry = Text(font=("Arial", 12))
entry.pack(pady=20, padx=10)

entry.bind("<Key>", on_key_pressed)
start()


window.mainloop()


