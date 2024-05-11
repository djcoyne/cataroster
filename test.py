from PyQt6.QtCore import QMimeData, QSize, Qt
from PyQt6.QtGui import QDrag, QMouseEvent
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout 
from PyQt6.QtWidgets import QTabWidget, QGridLayout, QWidget, QComboBox, QLineEdit, QLabel
import players as p
import pandas as pd
import numpy as np
import sys

#Read in the CSV with the current roster
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

# Create the list of Mains
r = []
for x in players:
    r.append(x.charlist[0])

# Define the list of Raiders for the Active Roster
raider=[]

# Reset Button function

def resetPlayers():
    for x in raider:
        x.reset()
    rlist=[]
    calculateBuffs(rlist)

# Calculate Buffs function

def calculateBuffs(rlist):
    raidbuffs = pd.read_csv('raidbuffs.csv', names=['Buff'])
    availbuffs = []
    for x in rlist:
        availbuffs.extend(x.a.buffs)

    availbuffs = set(availbuffs)
    missbuffs = pd.concat([raidbuffs,pd.DataFrame(availbuffs, columns=['Buff'])]).drop_duplicates(keep=False)
    return missbuffs


# Define draggable elements class
class Draggable(QLabel):
    def __init__(self, raider, x, y, text, width, height):
        super().__init__(text=text, width=width, height=height)
        self.x0, self.y0 = x,y
        self.raider = raider
        colorstyle = "QLabel{color:%s; background-color:%s}" % (
                    'black',
                    self.raider.a.c,
                    )
        self.setStyleSheet(colorstyle)

    def dragStart(self,e):
        if e.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData
            drag.setMimeData(mime)
            drag.exec_(Qt.MoveAction)



"""
GUI section
"""
#Define Main Window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CB Cata Roster Tool")
        minw = 1000
        minh = 500
        self.setMinimumSize(minw, minh)
        layout = QHBoxLayout()
        
        tabs = QTabWidget()
        tabs.addTab(self.rosterTabUI(), "Roster")
        tabs.addTab(self.addPATabUI(players), "Add PA")
        tabs.addTab(self.manageRaidersTabUI(), "Manage Raiders")
        layout.addWidget(tabs)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

#Create the Roster Tab

    def rosterTabUI(self):
        self.setAcceptDrops(True)
        rosterTab = QWidget()
        outerlayout = QHBoxLayout()
        leftlayout = QGridLayout()
        leftlayout.setVerticalSpacing(3)
        leftlayout.setHorizontalSpacing(3)
        i = 0
        j = 0
        for x in r:
            leftlayout.addWidget(Draggable(x,i,j,text=x.n + "; "+ x.s+" ("+x.a.r+")", width=30, height=2))
            i+=1
            if i % 5 == 0:
                i=0
                j+=1
        outerlayout.addLayout(leftlayout)
        rightlayout = QVBoxLayout()
        rightlayout.addWidget(QPushButton("Reset"))
        outerlayout.addLayout(rightlayout)
        rosterTab.setLayout(outerlayout)

        def dragEnterEvent(self, e):
            e.accept()

        return rosterTab

 #Create the PA Management Tab   

    def addPATabUI(self, roster):
        PATab = QWidget()
        layout = QVBoxLayout()
        self.cb = QComboBox()
        for x in roster:
            self.cb.addItem(x.name)
        layout.addWidget(self.cb)
        PATab.setLayout(layout)
        return PATab

#Create the Raider Management Tab 

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

# Initialize and run the app   
 
app = QApplication(sys.argv)
ui = MainWindow()
ui.show()
app.exec()

    
