import customtkinter as tk
import tkcalendar
import json

def update_values():
    global sel_date
    sel_date = cal.get_date()
    date_label.configure(text=sel_date)
    frame.after(100, update_values)

data_dict = {}


def get_note():
    global data_dict, sel_date
    data_dict[sel_date] = entry_note.get()
    with open("dict_json.json", "w") as f:
        json.dump(data_dict, f)

    create_event()


tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")
root_calendar = tk.CTk()
root_calendar.geometry("500x400")
root_calendar.title("Calendar")

frame = tk.CTkFrame(root_calendar, bg_color="white")
frame.place(x=0, y=0, relwidth=1, relheight=1)


cal = tkcalendar.Calendar(frame, showothermonthdays=False, showweeknumbers=False,
                          font=("Times New Roman", 20), selectmode="day",
                          headersforeground="#cccbca",
                          normalforeground="white", weekendforeground="#827f7d",
                          selectforeground="#5fd6fa", disableddaybackground="white",
                          date_pattern="y-mm-dd", tooltipforeground="yellow")
cal.pack(fill="both")

date = cal.datetime.today()

cal.calevent_create(date, "Today")



def create_root():
    root_notes = tk.CTk()
    root_notes.geometry("200x200")
    root_notes.title("Notes")
    create_event()
    notes_text = ""
    for key, value in data_dict.items():
        notes_text = notes_text + f"{key} --- {value}\n"

    notes_label = tk.CTkLabel(root_notes, text=notes_text,
                              font=("Times New Roman", 15))
    notes_label.pack(expand=True)

    clear_bottom = tk.CTkButton(root_notes, text="Clear",
                                font=("Times New Roman", 15), width=30)
    clear_bottom.pack(side=tk.BOTTOM, pady=10)



def create_event():
    with open("dict_json.json", "r") as f:
        global data_dict
        data_dict = json.load(f)



sel_date = cal.get_date()

date_label = tk.CTkLabel(frame, text=sel_date, font=("Times New Roman", 20))
date_label.pack(side=tk.LEFT, padx=70)

entry_note = tk.CTkEntry(frame, width=200)
entry_note.pack(side=tk.LEFT)

note_button = tk.CTkButton(frame, text="Note", font=("Times New Roman", 15),
                           width=100, command=get_note)
note_button.place(x=227, y=340)

note_button = tk.CTkButton(frame, text="Get", font=("Times New Roman", 15),
                           width=100, command=create_root)
note_button.place(x=340, y=340)

update_values()

root_calendar.mainloop()
