import tkinter as tk
from tkinter import filedialog
import main
from main import download
global folder_path

def open_popup(finished):
   top= tk.Toplevel(root)
   top.geometry("750x250")
   top.title("Child Window")
   if finished:
      message = "Finished"
   else:
      message = "Error try Again"
   tk.Label(top, text= message, font=('Mistral 18 bold')).place(x=150,y=80)


def onOptionsChange(*args):
   dialect = main.dialects[args[0]]
   voicesClass = dialect.getVoice()
   my_add(voicesClass)

def buttonDownload():
   input = textbox.get("1.0",'end-1c')
   dialect = variable.get()
   voice = voiceVa.get()
   finished = download(input,dialect,voice, folder_path)
   open_popup(finished)


def browse_button():
   filename = filedialog.askdirectory()
   global folder_path
   folder_path=filename

def my_remove():
   voiceVa.set('')  # remove default selection only, not the full list
   voice['menu'].delete(0, 'end')  # remove full list


def my_add(my_list):
   my_remove()  # remove all options
   for opt in my_list:
      voice['menu'].add_command(label=opt, command=tk._setit(voiceVa, opt))
   voiceVa.set(my_list[0])  # default value set

root = tk.Tk(className="Text To Audio")
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
textbox = tk.Text(root)
textbox.pack()
textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)
B = tk.Button(root, text ="Download", command=buttonDownload)
dialect = ["British", "American"]
variable = tk.StringVar(root)
variable.set(dialect[0])
dialec = tk.OptionMenu(root, variable, *dialect, command=onOptionsChange)
dialec.pack(side=tk.LEFT)
voices = ["British","American"]
voiceVa = tk.StringVar(root)
voiceVa.set(voices[0])
voice = tk.OptionMenu(root, voiceVa, *voices)
voice.pack(side=tk.LEFT)
button2 = tk.Button(text="Browse", command=browse_button)
button2.pack(side=tk.LEFT)
B.pack()



root.mainloop()