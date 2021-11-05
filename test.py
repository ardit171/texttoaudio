import tkinter as tk

my_w = tk.Tk()
my_w.geometry("350x200")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

my_list = ["PHP", "MySQL", "Python", "HTML", "JQuery"]
options = tk.StringVar(my_w)
options.set(my_list[0])  # default value

om1 = tk.OptionMenu(my_w, options, *my_list)
om1.grid(row=2, column=5)

b1 = tk.Button(my_w, text='Remove All', command=lambda: my_remove())
b1.grid(row=1, column=2)

b2 = tk.Button(my_w, text='Add All Opt', command=lambda: my_add())
b2.grid(row=2, column=2)

b3 = tk.Button(my_w, text='Remove Selectd', command=lambda: my_remove_sel())
b3.grid(row=3, column=2)


def my_remove():
    options.set('')  # remove default selection only, not the full list
    om1['menu'].delete(0, 'end')  # remove full list


def my_add():
    my_remove()  # remove all options
    for opt in my_list:
        om1['menu'].add_command(label=opt, command=tk._setit(options, opt))
    options.set(my_list[0])  # default value set


def my_remove_sel():
    r_index = om1['menu'].index(options.get())
    om1['menu'].delete(r_index)
    options.set(om1['menu'].entrycget(0, "label"))  # select the first one


my_w.mainloop()