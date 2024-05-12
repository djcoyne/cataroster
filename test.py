from PyQt6.QtCore import QMimeData, QSize, Qt
from PyQt6.QtGui import QDrag, QPixmap, QPainter, QCursor
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
    def __init__(self, raider, x, y, text):
        super().__init__(text=text)
        self.setAcceptDrops(True)
        self.x0, self.y0 = x,y
        self.raider = raider
        self.colorstyle = "QLabel{color:%s; background-color:%s;}" % (
                    'black',
                    self.raider.a.c,
                    )
        self.setStyleSheet(self.colorstyle)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.pos()
    
    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.MouseButton.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        mimedata.setColorData(self.colorstyle)
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec(Qt.DropAction.MoveAction)

class DropLabel(QLabel):
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        pos = event.position()
        text = event.mimeData().text()
        self.setText(text)
        event.acceptProposedAction()



"""
GUI section
"""
#Define Main Window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CB Cata Roster Tool")
        minw = 1200
        minh = 700
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
        rosterTab = QWidget()
        outerlayout = QHBoxLayout()
        leftlayout = QVBoxLayout()
        gridlayout = QGridLayout()
        gridlayout.setVerticalSpacing(3)
        gridlayout.setHorizontalSpacing(3)
        i = 0
        j = 0
        for x in r:
            gridlayout.addWidget(Draggable(x,i,j,text=x.n + "; "+ x.s+" ("+x.a.r+")"),i,j)
            i+=1
            if i % 5 == 0:
                i=0
                j+=1
        rosterslots = QGridLayout()
        rosterslots.setVerticalSpacing(3)
        rosterslots.setHorizontalSpacing(3)
        for i in range(5):
            for j in range(5):
                label = DropLabel()
                label.setStyleSheet('background-color: gray;')
                rosterslots.addWidget(label,i,j)
        leftlayout.addLayout(gridlayout)
        leftlayout.addLayout(rosterslots)
        outerlayout.addLayout(leftlayout)
        rightlayout = QVBoxLayout()
        rightlayout.addWidget(QPushButton("Reset"))
        outerlayout.addLayout(rightlayout)
        rosterTab.setLayout(outerlayout)
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

    
