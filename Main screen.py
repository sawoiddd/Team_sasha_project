import customtkinter as tk
from PIL import Image
from datetime import datetime

images = {"calculator": "calculator.svg.png",
          "to-do list": "to do list.png",
          "snake": "snake.png",
          "browser": "browser.png",
          "weather": "weather.jpeg",
          "calendar": "calendar.png"}


class Window(tk.CTk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("1920x1080")
        self._set_appearance_mode("Black")
        #self._set_default_color_theme("blue")
        self.frame = Frame(self)
        self.mainloop()


class Frame(tk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

            #calculator
        tk.CTkButton(self, width=50, height=50, text="",
            image=tk.CTkImage(light_image=Image.open(images.get("calculator")),
            size=(40, 40))).place(x=500, y=110)
        tk.CTkLabel(self, text="Calculator",
                    font=("Times New Roman", 15)).place(x=495, y=160)

        #to-do list
        tk.CTkButton(self, width=50, height=50, text="",
                     image=tk.CTkImage(light_image=Image.open(images.get("to-do list")),
                                       size=(40, 40))).place(x=700, y=110)
        tk.CTkLabel(self, text="To-do list",
                    font=("Times New Roman", 15)).place(x=698, y=160)
        #weather
        tk.CTkButton(self, width=50, height=50, text="",
                     image=tk.CTkImage(light_image=Image.open(images.get("weather")),
                                       size=(40, 40))).place(x=900, y=110)
        tk.CTkLabel(self, text="Weather",
                    font=("Times New Roman", 15)).place(x=900, y=160)

        #snake
        tk.CTkButton(self, width=50, height=50, text="",
                     image=tk.CTkImage(light_image=Image.open(images.get("snake")),
                                       size=(40, 40))).place(x=500, y=330)
        tk.CTkLabel(self, text="Snake",
                    font=("Times New Roman", 15)).place(x=510, y=380)

        #browser
        tk.CTkButton(self, width=50, height=50, text="",
                     image=tk.CTkImage(light_image=Image.open(images.get("browser")),
                                       size=(40, 40))).place(x=700, y=330)
        tk.CTkLabel(self, text="Browser",
                    font=("Times New Roman", 15)).place(x=702, y=380)

        #calendar
        tk.CTkButton(self, width=50, height=50, text="",
                     image=tk.CTkImage(light_image=Image.open(images.get("calendar")),
                                       size=(40, 40))).place(x=900, y=330)
        tk.CTkLabel(self, text="Calendar",
                    font=("Times New Roman", 15)).place(x=900, y=380)

        self.place(x=0, y=0, relwidth=1, relheight=0.7)


if __name__ == '__main__':
    Window()
