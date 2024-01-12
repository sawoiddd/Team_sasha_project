import tkinterweb
from tkinter import *
import customtkinter

root = customtkinter.CTk()

frame= tkinterweb.HtmlFrame(root)
frame.load_website('https://www.google.com/')
frame.pack()

root.mainloop()
