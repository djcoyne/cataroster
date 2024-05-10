# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:59:50 2024

@author: CoyneDa
"""

import tkinter as tk
import dragManager as dm
import players as p
import pandas as pd
import numpy as np


"""
This reads in a CSV with the current roster on it
"""
pl = pd.read_csv('cb_roster.csv').sort_values(by=['cl','spec','name']).reset_index()
players=[]
for index in pl.index:
    players.append(p.Player(pl['player'][index]))
    if pl['role'][index]==np.nan:
       players[index].add_character(name=pl['name'][index],cl=pl['cl'][index],spec=pl['spec'][index])
    else:
        players[index].add_character(name=pl['name'][index],cl=pl['cl'][index],spec=pl['spec'][index],role=pl['role'][index])
    if pl['altname'][index]!=np.nan:
        if pl['altrole'][index]==np.nan:
           players[index].add_character(name=pl['name'][index],cl=pl['cl'][index],spec=pl['spec'][index])
        else:
            players[index].add_character(name=pl['name'][index],cl=pl['cl'][index],spec=pl['spec'][index],role=pl['role'][index])


"""
This creates the list of mains
"""
r = []
for x in players:
    r.append(x.charlist[0])


"""
GUI section
"""

ui = tk.Tk()
ui.geometry("2500x1400")
ui.minsize(2500,1400)
ui.maxsize(2500,1400)
ui.title(' Continental Breakfast Cata Roster Tool ')

ui.columnconfigure((0,1,2,3,4,5,6,7), weight=3)
ui.columnconfigure(8, weight=1)
ui.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13), weight=1)

tk.Label(ui, text='').grid(column=0,row=5)

groups=[]
i=1
while i < 6:
    groups.append(tk.Label(ui,
                           text = "Group " + str(i)
                           ))
    groups[-1].grid(row=6, column = i, sticky='s')
    i+=1
"""
Raid positions
"""
pos=[]
i=1
while i < 6:
    j=8
    while j < 13:
      pos.append(tk.Frame(ui,
                          bg='gray'
                          ).grid(row=j, column=i,sticky='nsew', padx=3, pady=3 ))
      j+=1
    i+=1
      


"""
Draggables
"""
rlist = []
raider=[]
i=0    
j=0

for x in r:
    raider.append(dm.dragManager(ui,
                        raider = x,
                        text=x.n + "; "+ x.s+" ("+x.a.r+")",
                        color=x.a.c,
                        height=2,
                        width=30,
                        x=i,
                        y=j))
    raider[-1].grid(row=i, column=j, sticky='nsew', padx=3, pady=3)
    i+=1
    if i % 5==0:
        i=0
        j+=1

"""
Reset Button
"""

def resetPlayers():
    for x in raider:
        x.reset()
    rlist=[]
    calculateBuffs(rlist)

reset_butt = tk.Button(text = "Reset",
    width=7,
    height=2,
    bg='red',
    fg='black',
    command = resetPlayers
    )

reset_butt.grid(row=1,column=8, sticky='new')


"""
Calculate Buffs
"""
def calculateBuffs(rlist):
    raidbuffs = pd.read_csv('raidbuffs.csv', names=['Buff'])
    availbuffs = []
    for x in rlist:
        availbuffs.extend(x.a.buffs)

    availbuffs = set(availbuffs)
    missbuffs = pd.concat([raidbuffs,pd.DataFrame(availbuffs, columns=['Buff'])]).drop_duplicates(keep=False)
    return missbuffs.to_string(index=False, header=False)

calc_butt = tk.Button(text = "Calculate Buffs",
                  width=7,
                  height=2,
                  bg='green',
                  fg='black',
                  command = calculateBuffs(rlist)
                  )
calc_butt.grid(row=0, column=8, sticky='sew')

"""
Results Section
"""
m1 = tk.Label(text="Your raid is missing:\n"+calculateBuffs(rlist),
              font= ('Arial'))
m1.grid(row=6, column=8, rowspan=7, sticky='e')

ui.mainloop()
    

    
