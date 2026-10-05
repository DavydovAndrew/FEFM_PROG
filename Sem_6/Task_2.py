from tkinter import *
from tkinter import ttk

def calc(*args):
    i = float(mass.get()) / float(height.get().replace(',', '.')) ** 2
    out.set(round(i, 1))
    res.set(diag(i))

def diag(i):
    if i <= 16:
        return 'Выраженный дефицит массы тела'
    elif i <= 18.5:
        return 'Недостаточная (дефицит) масса тела'
    elif i <= 25:
        return 'Норма'
    elif i <= 30:
        return 'Избыточная масса тела (предожирение)'
    elif i <= 35:
        return 'Ожирение 1 степени'
    elif i <= 40:
        return 'Ожирение 2 степени'
    return 'Ожирение 3 степени'

root = Tk()
root.title('BMI Calculator')

mainframe = ttk.Frame(root, padding="3 3 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mass = StringVar()
mass_entry = ttk.Entry(mainframe, width=7, textvariable=mass)
mass_entry.grid(column=2, row=1, sticky=(W, E))

height = StringVar()
height_entry = ttk.Entry(mainframe, width=7, textvariable=height)
height_entry.grid(column=4, row=1, sticky=(W, E))

out = StringVar()
ttk.Label(mainframe, textvariable=out).grid(column=2, row=2, sticky=(W, E))

res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calc).grid(column=4, row=3, sticky=W)

ttk.Label(mainframe, text="Mass [kg]:").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Height [m]:").grid(column=3, row=1, sticky=E)
ttk.Label(mainframe, text="BMI:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Result:").grid(column=1, row=3, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

mass_entry.focus()
root.bind("<Return>", calc)
root.mainloop()