import customtkinter as tk
from PIL import Image
from datetime import datetime
import subprocess


tk.set_appearance_mode("Black")
tk.set_default_color_theme("blue")
root_start = tk.CTk()
root_start.geometry("1920x1080")
root_start.title("")

now = datetime.now()
date = now.strftime("%A, %d %B")
time = now.strftime("%H:%M")


real_password = "0000"


def check_password():
    if real_password == entry.get():
        root_start.destroy()
        subprocess.run(["python", "main_screen.py"])





'''image_path = "dark orange.jpeg"
image = tk.CTkImage(light_image=Image.open(image_path), size=(1920, 1080))
image_label = tk.CTkLabel(root_start, image=image, text="")
image_label.place(x=0, y=0)'''

space_top = tk.CTkLabel(root_start, text="")
space_top.pack(pady=10)

date_label = tk.CTkLabel(root_start, text=date, font=("Times New Roman", 30))
date_label.pack(pady=10)


time_label = tk.CTkLabel(root_start, text=time, font=("Times New Roman", 80))
time_label.pack(pady=0)

space_bottom = tk.CTkLabel(root_start, text="")
space_bottom.pack(pady=200)

entry = tk.CTkEntry(root_start, show="•", font=("Times New Roman", 20), corner_radius=0)
entry.pack()

enter_button = tk.CTkButton(root_start, text="Enter", command=check_password)
enter_button.pack(pady=10)


def update_time():

    now = datetime.now()
    date = now.strftime("%A, %d %B")
    time = now.strftime("%H:%M")
    date_label.configure(text=now.strftime("%A, %d %B"))
    time_label.configure(text=now.strftime("%H:%M"))
    root_start.after(1000, update_time)

update_time()


root_start.mainloop()
