import tkinter
from tkinter import filedialog, DISABLED, PhotoImage, Canvas, YES
import customtkinter
from PIL import Image
import hashlib



##############################  Function ##############################

# choice wordlist
def file_open(): 
    path = filedialog.askopenfilename(filetypes=(("txt files", "*.txt"),)) # .txt only
    wordlist_entry.configure(state="normal")
    wordlist_entry.delete(0, 'end') # clean text 
    wordlist_entry.insert(0, path) 
    wordlist_entry.configure(state="disabled")









##############################  Function ##############################

##############################  MAIN APP CONFIGURE ##############################

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.minsize(750,750)
app.maxsize(750,750)
app.title("FxHash")
app.iconbitmap("assets/lock.ico")

##############################  MAIN APP CONFIGURE ##############################


##############################  add image ##############################

skull_image = Image.open('assets/skull.png')
skull_ctk_image = customtkinter.CTkImage(skull_image, size=(120,120))
skull_img_label = customtkinter.CTkLabel(app, image=skull_ctk_image, text="")
skull_img_label.place(x=10, y=10)

##############################  add image ##############################



##############################  add labels ##############################

hash_label = customtkinter.CTkLabel(master=app, text="Hash", font=("Copperplate Gothic Bold",20))
hash_label.place(relx=0.1, rely=0.25, anchor=tkinter.CENTER)

wordlist_label = customtkinter.CTkLabel(master=app, text="Wordlist", font=("Copperplate Gothic Bold",20))
wordlist_label.place(relx=0.10, rely=0.35, anchor=tkinter.CENTER)


title_label = customtkinter.CTkLabel(master=app, text="FxHash", font=("Copperplate Gothic Bold",50), text_color="green")
title_label.place(relx=0.50, rely=0.10, anchor=tkinter.CENTER)

version_label = customtkinter.CTkLabel(master=app, text="V.1.0.0", font=("Copperplate Gothic Bold",20), text_color="green")
version_label.place(relx=0.93, rely=0.98, anchor=tkinter.CENTER)

##############################  add labels ##############################


##############################  add entry ##############################

hash_entry = customtkinter.CTkEntry(master=app,width=400,height=30,border_width=2, corner_radius=15)
hash_entry.place(relx=0.45, rely=0.25, anchor=tkinter.CENTER)

wordlist_entry = customtkinter.CTkEntry(master=app,width=400,height=30,border_width=2,corner_radius=15)
wordlist_entry.place(relx=0.45, rely=0.35, anchor=tkinter.CENTER)
wordlist_entry.configure(state="disabled")

##############################  add entry ##############################


##############################  add button ##############################

wordlist_button = customtkinter.CTkButton(master=app,width=30,height=32,border_width=0,corner_radius=8,text="...",command=file_open)
wordlist_button.place(relx=0.75, rely=0.35, anchor=tkinter.CENTER)

start_button = customtkinter.CTkButton(master=app,width=700,height=32,border_width=0,corner_radius=8,text="Start")
start_button.place(relx=0.50, rely=0.60, anchor=tkinter.CENTER)

##############################  add button ##############################


##############################  add combobox ##############################

combobox = customtkinter.CTkOptionMenu(master=app,
                                     values=["MD5","Sha1","Sha224","Sha256","Sha384","Sha512","Sha3_224","Sha3_256","Sha3_384","Sha3_512"])
combobox.place(relx=0.83, rely=0.25, anchor=tkinter.CENTER)
combobox.set("Type Hash")

##############################  add combobox ##############################


##############################  add textbox ##############################

textbox = customtkinter.CTkTextbox(master=app, width=500, height=30,corner_radius=8)
textbox.place(relx=0.50, rely=0.50, anchor=tkinter.CENTER)
textbox.insert("0.0", "") 
textbox.configure(state="disabled")

##############################  add textbox ##############################


app.mainloop()