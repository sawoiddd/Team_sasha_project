import customtkinter

root = customtkinter.CTk()
root.title('Нотатки')
root.geometry('1080x720')
root.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")


def create():
    global entry_name
    global textbox
    global button_save
    global button_close
    entry_name = customtkinter.CTkEntry(frame2, width=170, height=30, font=('Roboto', 15), placeholder_text="Enter file name")
    entry_name.place(x=10, y=15)

    textbox = customtkinter.CTkTextbox(master=frame2, width=730, height=610)
    textbox.place(x=10, y=55)

    button_save = customtkinter.CTkButton(frame2, text="Save", command=save_and_update_list, width=95, font=('Roboto', 15))
    button_save.place(x=645, y=15)
    button_close = customtkinter.CTkButton(frame2, text="Close", command=close, width=95,fg_color='#242424',
                                          font=('Roboto', 15))
    button_close.place(x=540, y=15)

    update_file_list()




def save_and_update_list():
    save()
    update_file_list()

def update_file_list():

    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    file_folder = "file"
    for filename in os.listdir(file_folder):
        frame_saves = customtkinter.CTkFrame(scrollable_frame, width=200, height=50, bg_color='#495057')
        frame_saves.pack(pady=5)
        label_file = customtkinter.CTkLabel(frame_saves, text=filename,width=150, font=('Roboto', 12), fg_color='#495057' )
        label_file.pack(side="left")
        button_open = customtkinter.CTkButton(frame_saves, text="Open", command=lambda name=filename: open_file(name), width=50, font=('Roboto', 12),bg_color='#495057')
        button_open.pack(side="right")

def open_file(filename):
    file_path = os.path.join("file", filename)

    global entry_name
    global textbox
    global button_save
    global button_close
    entry_name = customtkinter.CTkEntry(frame2, width=170, height=30, font=('Roboto', 15),
                                        placeholder_text="Enter file name")
    entry_name.place(x=10, y=15)

    textbox = customtkinter.CTkTextbox(master=frame2, width=730, height=610)
    textbox.place(x=10, y=55)

    button_save = customtkinter.CTkButton(frame2, text="Save", command=save_and_update_list, width=95,
                                          font=('Roboto', 15))
    button_save.place(x=645, y=15)
    button_close = customtkinter.CTkButton(frame2, text="Close", command=close, width=95, fg_color='#242424',
                                          font=('Roboto', 15))
    button_close.place(x=540, y=15)
    with open(file_path, 'r') as file:
        content = file.read()
        entry_name.delete(0, "end")
        entry_name.insert(0, os.path.splitext(filename)[0]) 
        textbox.delete("1.0", "end")
        textbox.insert("1.0", content)





import os

def save():
    file_name = entry_name.get()
    text_content = textbox.get("1.0", "end-1c")
    folder_path = "file"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, f'{file_name}.txt')

    global frame_supp
    global label_supp
    global label_status 
    global button_status

    if os.path.exists(file_path):
        frame_supp = customtkinter.CTkFrame(root, width=300, height=60, fg_color='#495057')
        frame_supp.place(x=850, y=600)
        label_status = customtkinter.CTkLabel(frame_supp, text=f"Файл з таким іменем вже існує", font=('Roboto', 14))
        label_status.place(x=10, y=5)
        button_status = customtkinter.CTkButton(frame_supp, text='Save', font=('Roboto', 13), width=60, height=20,command=save_supp)
        button_status.place(x=150,y = 35)
        button_status = customtkinter.CTkButton(frame_supp, text='Cancel',fg_color='#495057', font=('Roboto', 13), width=60, height=20,command=cancel_supp)
        button_status.place(x=85, y=35)
    else:
        frame_supp.destroy()
        label_supp.destroy()
        label_status.destroy()
        button_status.destroy()


        with open(file_path, 'w') as file:
            file.write(text_content)
            print(f"File '{file_name}.txt' saved successfully.")

def save_supp():
    file_name = entry_name.get()
    text_content = textbox.get("1.0", "end-1c")
    folder_path = "file"

    file_path = os.path.join(folder_path, f'{file_name}.txt')

    frame_supp.destroy()
    label_supp.destroy()
    label_status.destroy()
    button_status.destroy()

    with open(file_path, 'w') as file:
        file.write(text_content)
        print(f"File '{file_name}.txt' saved successfully.")

def cancel_supp():
    frame_supp.destroy()
    label_supp.destroy()
    label_status.destroy()
    button_status.destroy()
def close():
    entry_name.destroy()
    textbox.destroy()
    button_save.destroy()
    button_close.destroy()

def delete():
    pass

def colorMode():
    pass

'''Frame1'''

frame1 = customtkinter.CTkFrame(master=root, width=250, height=720, bg_color='#242424')
frame1.place(x=0,y=0)

entry_search = customtkinter.CTkEntry(frame1,width=200, placeholder_text="Search..")
entry_search.place(x=40,y=10)

button_delete = customtkinter.CTkButton(frame1, text="Delete", command=delete, width=95, fg_color='#2b2b2b',hover_color="#495057", border_width=2,border_color='#343A40', font=('Roboto',15),)
button_delete.place(x=40,y=670)

button_create = customtkinter.CTkButton(frame1, text="Create", command=create, width=95, font=('Roboto',15))
button_create.place(x=145,y=670)

scrollable_frame = customtkinter.CTkScrollableFrame(frame1, width=190, height=600,bg_color='#212121')
scrollable_frame.place(x=40,y=44)


update_file_list()
'''Frame Bar'''
frame_bar = customtkinter.CTkFrame(master=frame1, width=30, height=720, fg_color='#353535')
frame_bar.place(x=0,y=0)

'''button_create = customtkinter.CTkButton(frame1, text="+", command=colorMode, width=30, font=('Roboto',30),fg_color='#353535')
button_create.place(x=0,y=670)'''

'''#Frame2'''

frame2 = customtkinter.CTkFrame(master=root, width=750, height=680, bg_color='#242424')
frame2.place(x=300,y=22)



root.mainloop()
