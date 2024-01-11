
""" Importing Required Modules"""

import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showinfo

"""Function Definition Of Commands for buttons"""

def save_file():
    file_loc=asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files","*.txt"),("All Files","*.*")]
    )
    if not file_loc:
        return
    with open(file_loc,"w") as file_out:
        text=text_edit.get(1.0,tk.END)
        file_out.write(text)
    window.title(f"Text Editor-{file_loc}")

def open_file():
    file_loc=askopenfilename(
        filetypes=[("Text Files","*.txt"),("All Files","*.*")]
    )
    if not file_loc:
        return
    text=text_edit.delete(1.0,tk.END)
    with open(file_loc,"r") as file_in:
        text=file_in.read()
        text_edit.insert(tk.END,text)
    window.title(f"Text Editor-{file_loc}")

def help_me():
    contact_text="Developed By : Kirubahar B\nEmail : bkirubahar@gmail.com\nGithub : https://github.com/KirubaharBalaji"
    tk.messagebox.showinfo(title="Contact", message=contact_text)

"""GUI Window"""

window=tk.Tk()
window.title("Text Editor")
window.rowconfigure(0,minsize=1000)
window.columnconfigure(1,minsize=1000)

"""Text to display in GUI

sticky option. The sticky option specifies which edge of the cell the widget should stick to.
NSEW-North,South,East,West

"""

text_edit=tk.Text(window)
text_edit.grid(row=0,column=1,sticky="nsew")

""".grid gives position"""

"""Buttons for GUI"""

button_frame=tk.Frame(window,relief=tk.RAISED,bd=5)
button_frame.grid(row=0,column=0,sticky="ns")

"""bd is border"""

btn_open=tk.Button(button_frame,text="Open",command=open_file)
btn_save=tk.Button(button_frame,text="Save As",command=save_file)
btn_help=tk.Button(button_frame,text="Help",command=help_me)

"""Button Position"""

btn_open.grid(row=0,column=0,padx=10,pady=10)
btn_save.grid(row=0,column=1,padx=10,pady=10)
btn_help.grid(row=0,column=2,padx=10,pady=10)

"""To display the GUI"""

window.mainloop()
