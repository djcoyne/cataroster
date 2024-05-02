# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:59:50 2024

@author: CoyneDa
"""

import tkinter as tk
import dragManager as dm
import players as p
import pandas as pd

roster=pd.DataFrame(columns=['Name','Role','Class','Spec'])
raidbuffs = pd.read_csv('raidbuffs.csv', names=['Buff'])

playerlist = []
Raph = p.Player('Raph')
Dave = p.Player('Dave')
Alan = p.Player('Alan')
Tara = p.Player('Tara')
Chelsea = p.Player('Chelsea')

Raph.add_character('Thurdead','Death Knight','Blood', role='tank')
Dave.add_character('Gwendolock','Warlock','Affliction')
Dave.add_character('Gwenance','Priest','Discipline')
Alan.add_character('Knotadellon','Druid','Restoration')
Tara.add_character('Maureensy','Warlock','Destruction')
Chelsea.add_character('Kittn','Shaman','Elemental')



r = []
r.append(Raph.charlist[0])
r.append(Dave.charlist[0])
r.append(Alan.charlist[0])
r.append(Tara.charlist[0])
r.append(Chelsea.charlist[0])

playerlist.append(Raph)
playerlist.append(Dave)
playerlist.append(Alan)
playerlist.append(Tara)
playerlist.append(Chelsea)


availbuffs = []
rosterlist = []
for x in r:
    roster.loc[len(roster.index)] =[x.n, x.a.r, x.c, x.s]
    availbuffs.extend(x.a.buffs)
    rosterlist.append(x.n) 

availbuffs = set(availbuffs)
missbuffs = pd.concat([raidbuffs,pd.DataFrame(availbuffs, columns=['Buff'])]).drop_duplicates(keep=False)

"""
GUI section
"""

ui = tk.Tk()
ui.state('zoomed')
ui.configure(bg='gray')
ui.title(' Continental Breakfast Cata Roster Tool ')

"""
Draggables
"""
raider=[]
dnd=[]
i=0    

for x in r:
    raider.append(tk.Label(ui,
                        text=x.n + "; "+ x.s+" ("+x.a.r+")",
                        bg=x.a.c,
                        height=2,
                        width=30
                        ))
    raider[-1].place(x=200, y = 20+4*i,anchor="center")
    dnd.append(dm.DragManager())
    dnd[-1].add_draggable(raider[-1])
    i+=10
    
"""
Reset Button
"""

button = tk.Button(
    text = "Reset",
    width=7,
    height=2,
    bg='red',
    fg='black',
    )
button.pack()

"""
Results Section
"""

m1 = tk.Label(text="Your raid is missing:")
m2 = tk.Label(text=missbuffs.to_string(index=False, header=False))                           
m1.pack()
m2.pack()

ui.mainloop()
    

    
