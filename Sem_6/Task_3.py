from tkinter import *
from tkinter import ttk
from random import choice
import pandas as pd
films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])

complex_genres = []
for film_genre in film_genres_list:
    genres = film_genre.split(' | ')
    if len(genres) > 1:
        for genre in genres:
            film_genres_list.append(genre)
        complex_genres.append(film_genre) 
  
for genre in complex_genres:
    film_genres_list.remove(genre)
    
genres_set = set(film_genres_list)

dct = {}
for g in genres_set:
    dct[g] = []
    for i in range(250):
        if g in films['Genre'][i]:
            dct[g].append(films['Title'][i])

def search(*args):
    try:
        out.set(choice(dct[inp.get()]))
    except:
        out.set('Nothing found(((')

root = Tk()
root.title('Random movie')

mainframe = ttk.Frame(root, padding="3 3 10 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

inp = StringVar()
inp_entry = ttk.Entry(mainframe, width=7, textvariable=inp)
inp_entry.grid(column=2, row=1, sticky=(W, E))

out = StringVar()
ttk.Label(mainframe, textvariable=out).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Search", command=search).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Genre:").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="For example,").grid(column=1, row=2, sticky=E)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

inp_entry.focus()
root.bind("<Return>", search)
root.mainloop()