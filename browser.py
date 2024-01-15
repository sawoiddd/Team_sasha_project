import customtkinter
import os
from datetime import *
import pygame.mixer
from time import strftime

root = customtkinter.CTk()
root.title('Clock')
root.geometry('1200x900')
root.resizable(width=False, height=False)
# customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("dark")

print(datetime.time)


def time():
    string = strftime('%H:%M:%S')
    lbl.configure(text=string)
    lbl.after(1000, time)

def addTimer():
    global frame_timer
    global entry_hours
    global entry_minutes
    global entry_seconds
    global timer
    global entry_name

    timer = customtkinter.CTk()
    timer.title('Timer')
    timer.geometry('300x280')
    timer.resizable(width=False, height=False)





    timer_label = customtkinter.CTkLabel(timer,text='Add new timer',font=('Roboto', 23))
    timer_label.place(x=20,y=10)


    entry_hours = customtkinter.CTkEntry(timer, width=75, height=75,placeholder_text="00",font=('Roboto', 50))
    entry_hours.place(x=20, y=70)

    label_doblepoint = customtkinter.CTkLabel(timer,text=":",font=('Roboto', 50) )
    label_doblepoint.place(x=97, y=70)

    entry_minutes = customtkinter.CTkEntry(timer, width=75, height=75,placeholder_text="00",font=('Roboto', 50))
    entry_minutes.place(x=112, y=70)

    label_doblepoint = customtkinter.CTkLabel(timer, text=":", font=('Roboto', 50))
    label_doblepoint.place(x=189, y=70)

    entry_seconds = customtkinter.CTkEntry(timer, width=75, height=75, placeholder_text="00",font=('Roboto', 50))
    entry_seconds.place(x=205, y=70)

    entry_name = customtkinter.CTkEntry(timer, width=260, height=30, placeholder_text="Timer 1", font=('Roboto', 14))
    entry_name.place(x=20, y=170)

    button_save = customtkinter.CTkButton(timer, text='Save',font=('Roboto', 15),width=125,height=35,command=startTimer)
    button_save.place(x=20,y=230)

    button_cancel = customtkinter.CTkButton(timer, text='Cancel', font=('Roboto', 15), width=125, height=35, fg_color='#242424')
    button_cancel.place(x=155, y=230)

    timer.mainloop()
var =0
def startTimer():
    global var
    var += 1

    hours = int(entry_hours.get() or "00")
    minutes = int(entry_minutes.get() or "00")
    seconds = int(entry_seconds.get() or "00")
    name = entry_name.get()  or f"timer {var}"


    frame_timer = customtkinter.CTkFrame(scrollable_frame, width=300, height=300)
    frame_timer.pack(pady=10)
    timer_label2 = customtkinter.CTkLabel(frame_timer, text='', width=300, height=300,font=('Roboto', 50))
    timer_label2.pack()

    print(name)


    total_seconds = hours * 3600 + minutes * 60 + seconds

    def update_timer():
        nonlocal total_seconds
        if total_seconds > 0:
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            timer_label2.configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            total_seconds -= 1
            root.after(1000, update_timer)
        else:
            timer_label2.configure(text="00:00:00")
            # play_notification_sound()
            frame_timer.destroy()

    update_timer()
    timer.destroy()


    def play_notification_sound():
        pygame.mixer.init()

        
        if switch_var.get() == "off":
            pygame.mixer.music.load("c1-rainforest-133060.mp3")
            pygame.mixer.music.play()
def settings():
    global switch_var
    sett = customtkinter.CTk()
    sett.title('Clock')
    sett.geometry('400x400')
    sett.resizable(width=False, height=False)

    def switch_event():
        print(switch_var.get())
        '''customtkinter.set_appearance_mode(switch_var.get())
        button_settings.configure()'''


    def radiobutton_event():
        print("radiobutton toggled, current value:", radio_var.get())
        # customtkinter.set_appearance_mode(radio_var.get())
        if radio_var.get() == 1:
            customtkinter.set_appearance_mode("dark")
            scrollable_frame.configure(fg_color='#242424')
        elif radio_var.get() == 2:
            customtkinter.set_appearance_mode("light")
            scrollable_frame.configure(fg_color='#ebebeb')

    label = customtkinter.CTkLabel(sett, text="Settings", fg_color="transparent",font=('Roboto', 27))
    label.place(x=10,y=10)

    label_colormode = customtkinter.CTkLabel(sett, text="Switch Notice", fg_color="transparent", font=('Roboto', 20))
    label_colormode.place(x=10, y=65)

    switch_var = customtkinter.StringVar(value="off")
    switch = customtkinter.CTkSwitch(sett, text="", command=switch_event,
                                     variable=switch_var, onvalue="on", offvalue="off")

    switch.place(x=11, y=100)

    label_colormode = customtkinter.CTkLabel(sett, text="Color Mode", fg_color="transparent", font=('Roboto', 20))
    label_colormode.place(x=10, y=140)

    radio_var = customtkinter.IntVar(value=0)
    radiobutton_1 = customtkinter.CTkRadioButton(sett, text="Dark",
                                                 command=radiobutton_event, variable=radio_var, value=1)
    radiobutton_1.place(x=11,y=175)
    radiobutton_2 = customtkinter.CTkRadioButton(sett, text="Light",
                                                 command=radiobutton_event, variable=radio_var, value=2)
    radiobutton_2.place(x=11, y=215)
    '''radiobutton_3 = customtkinter.CTkRadioButton(sett, text="System mode",
                                                 command=radiobutton_event, variable=radio_var, value=3)
    radiobutton_3.place(x=11, y=255)'''

    label_colormode = customtkinter.CTkLabel(sett, text="About program", fg_color="transparent", font=('Roboto', 20))
    label_colormode.place(x=10, y=295)

    label_colormode = customtkinter.CTkLabel(sett, text="Program clock: v1", fg_color="transparent", font=('Roboto', 14))
    label_colormode.place(x=11, y=325)

    label_colormode = customtkinter.CTkLabel(sett, text="© Developer Sashkoa", fg_color="transparent",
                                             font=('Roboto', 14))
    label_colormode.place(x=11, y=347)

    sett.mainloop()





# Frame_bar

frame = customtkinter.CTkFrame(root, width=230, height=900)
frame.place(x=0,y=0)

lbl = customtkinter.CTkLabel(frame, font=('calibri', 50, 'bold'))
lbl.place(x=20,y=10)

# button_timer = customtkinter.CTkButton(frame,text="Timer", width=230,height=40 ,fg_color="#2C2C2C",corner_radius=0,font=('Roboto', 12,'bold'))
# button_timer.place(x=0,y=10)

button_settings = customtkinter.CTkButton(frame,text="Settings", width=230,height=40,fg_color="#2C2C2C",corner_radius=0,font=('Roboto', 12,'bold'),command=settings)
button_settings.place(x=0,y=850)



# scrollable_frame

scrollable_frame = customtkinter.CTkScrollableFrame(root, width=930, height=890, fg_color='#242424')
scrollable_frame.place(x=240,y=0)


button_add = customtkinter.CTkButton(root,text="+ add a new timer", width=200,height=40,corner_radius=4,font=('Roboto', 16), command=addTimer)
button_add.place(x=950,y=850)


time()
root.mainloop()
