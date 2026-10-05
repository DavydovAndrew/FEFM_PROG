from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def choose_file(*args):
    file_var.set(fd.askopenfilename(title='Выберите CSV-файл'))

def mnk(*args):
    df = pd.read_csv(file_var.get())
    plt.scatter(df['x'], df['y'])

    a, b = np.polyfit(df['x'], df['y'], 1)
    mnk_var.set(f'a = {a}, b = {b}')

    plt.plot(df['x'], a * df['x'] + b, 'r')
    plt.savefig(f'{save_var.get()}.png', dpi=300)
    

root = Tk()
root.title("Подгонятор")
mainframe = ttk.Frame(root, padding="3 3 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


file_var = StringVar()
ttk.Label(mainframe, textvariable=file_var).grid(column=2, row=1, sticky=(W, E))

mnk_var = StringVar()
ttk.Label(mainframe, textvariable=mnk_var).grid(column=2, row=3, sticky=(W, E))

save_var = StringVar()
save_entry = ttk.Entry(mainframe, width=7, textvariable=save_var)
save_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Выбрать файл", command=choose_file).grid(column=3, row=1, sticky=E)
ttk.Button(mainframe, text="Построить график", command=mnk).grid(column=3, row=3, sticky=E)

ttk.Label(mainframe, text="Файл с данными:").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Введите имя файла графика:").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Коэффициенты МНК:").grid(column=1, row=3, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

save_entry.focus()
root.mainloop()