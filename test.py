# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:59:50 2024

@author: CoyneDa
"""

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout, QTabWidget, QWidget, QComboBox, QLineEdit, QLabel
import dragManager as dm
import players as p
import pandas as pd
import numpy as np
import sys

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
Define MainWindow subclass
"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CB Cata Roster Tool")

        layout = QHBoxLayout()
        
        tabs = QTabWidget()
        tabs.addTab(self.rosterTabUI(), "Roster")
        tabs.addTab(self.addPATabUI(players), "Add PA")
        tabs.addTab(self.manageRaidersTabUI(), "Manage Raiders")
        layout.addWidget(tabs)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

    def rosterTabUI(self):
        rosterTab = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("Reset"))
        rosterTab.setLayout(layout)
        return rosterTab
    
    def addPATabUI(self, roster):
        PATab = QWidget()
        layout = QVBoxLayout()
        self.cb = QComboBox()
        for x in roster:
            self.cb.addItem(x.name)
        layout.addWidget(self.cb)
        PATab.setLayout(layout)
        return PATab
    
    def manageRaidersTabUI(self):
        manageRaidersTab = QWidget()
        layout = QVBoxLayout()
        tabs = QTabWidget()
        tabs.addTab(self.addRaider(), "Add Raider")
        tabs.addTab(self.editRaider(), "Edit Raider")
        tabs.addTab(self.removeRaider(players), "Remove Raider")
        layout.addWidget(tabs)
        manageRaidersTab.setLayout(layout)
        return manageRaidersTab

    def addRaider(self):
        addRaiderTab = QWidget()
        layout = QFormLayout()
        layout.addRow(QLabel("Name: "), QLineEdit())
        layout.addRow(QLabel("Class: "), QLineEdit())
        layout.addRow(QLabel("Spec: "), QLineEdit())
        addRaiderTab.setLayout(layout)
        return addRaiderTab
        
    def editRaider(self):
        editRaiderTab = QWidget()
        layout = QFormLayout()
        layout.addRow(("Name: "), QLineEdit())
        layout.addRow(("Class: "), QLineEdit())
        layout.addRow(("Spec: "), QLineEdit())
        editRaiderTab.setLayout(layout)
        return editRaiderTab
        
    def removeRaider(self, roster):
        removeRaiderTab = QWidget()
        layout = QVBoxLayout()
        self.cb = QComboBox()
        for x in roster:
            self.cb.addItem(x.name)
        layout.addWidget(self.cb)
        removeRaiderTab.setLayout(layout)
        return removeRaiderTab



"""
GUI section
"""

app = QApplication(sys.argv)

ui = MainWindow()
ui.show()

"""
OLD UI SECTION

groups=[]
i=1
while i < 6:
    groups.append(tk.Label(ui,
                           text = "Group " + str(i)
                           ))
    groups[-1].grid(row=6, column = i, sticky='s')
    i+=1

Raid positions

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
      

Draggables

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


Reset Button


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


Calculate Buffs

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


Results Section

m1 = tk.Label(text="Your raid is missing:\n"+calculateBuffs(rlist),
              font= ('Arial'))
m1.grid(row=6, column=8, rowspan=7, sticky='e')

ui.mainloop()
"""

app.exec()

    
