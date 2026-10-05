from tkinter import *
from tkinter import ttk

def calc(*args):
    try:
        color = inp.get()
        compl = ''
        for xx in color[:2], color[2:4], color[4:]:
            compl += hex(255 - int(xx, 16))[2:].zfill(2)
        out.set(compl)
        ttk.Label(mainframe, text='', padding=(30, 8), background='#' + color).grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text='', padding=(30, 8), background='#' + compl).grid(column=3, row=2, sticky=W)
    except:
        out.set('Nothing found(((')

root = Tk()
root.title('Color calculator')

mainframe = ttk.Frame(root, padding="3 3 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

inp = StringVar()
inp_entry = ttk.Entry(mainframe, width=7, textvariable=inp)
inp_entry.grid(column=2, row=1, sticky=(W, E))

out = StringVar()
ttk.Label(mainframe, textvariable=out).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calc).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Color: #").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Complementary: #").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

inp_entry.focus()
root.bind("<Return>", calc)
root.mainloop()