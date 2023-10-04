import cowsay
import pyttsx3
import tkinter as tk

engine = pyttsx3.init()

def add_text():
    this = entry.get()
    entry.delete(0, tk.END)
    cowsay.cow(this)
    engine.say(this)
    engine.runAndWait()

label = tk.Label(text="What you wanna say? ", font=("Helvetica", 16), bg='#708090', fg='white')
label.pack()
entry = tk.Entry(font=("Helvetica", 12))
entry.pack()
button = tk.Button(text="Enter", command=add_text, font=("Helvetica", 12))
button.pack()

tk.mainloop()