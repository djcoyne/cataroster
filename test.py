from PyQt6.QtCore import QMimeData, QSize, Qt
from PyQt6.QtGui import QDrag, QPixmap, QPainter, QCursor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QFormLayout, QListWidget
from PyQt6.QtWidgets import QTabWidget, QGridLayout, QWidget, QComboBox, QLineEdit, QLabel, QCalendarWidget
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
global raidlist
raidlist = []

# Calculate Buffs function
def calculateBuffs(rlist):
    raidbuffs = pd.read_csv('raidbuffs.csv', names=['Buff'])
    availbuffs = []
    for x in rlist:
        availbuffs.extend(x.a.buffs)

    availbuffs = set(availbuffs)
    missbuffs = pd.concat([raidbuffs,pd.DataFrame(availbuffs, columns=['Buff'])]).drop_duplicates(keep=False).values.tolist()   
    return missbuffs
global mbuffs
mbuffs = calculateBuffs(raidlist)

# Reset function
def restart():
    app.exec()

# Define draggable elements class
class Draggable(QLabel):
    def __init__(self, raider, x, y, text):
        super().__init__(text=text)
        self.setAcceptDrops(True)
        self.raider = raider
        self.colorstyle = "QLabel{color:%s; background-color:%s;}" % (
                    'black',
                    self.raider.a.c,
                    )
        self.setStyleSheet(self.colorstyle)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mimedata = QMimeData()
            mimedata.setText(self.text())
            pixmap = QPixmap(self.size())
            painter = QPainter(pixmap)
            painter.drawPixmap(self.rect(), self.grab())
            painter.end()
            drag.setPixmap(pixmap)
            drag.setHotSpot(event.pos())
            drag.setMimeData(mimedata)
            drag.setHotSpot(event.position().toPoint())
            drag.exec(Qt.DropAction.MoveAction)
            self.drag_start_position = event.pos()        

class DropLabel(Draggable):
    def __init__(self, mbwid, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)
        self.mbwid = mbwid

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasText():
            text = event.mimeData().text()
            self.setText(text)
            self.raider = event.source().raider
            event.setDropAction(Qt.DropAction.MoveAction)
            event.accept()
            drag_color = event.source().palette().color(event.source().backgroundRole())
            self.setStyleSheet(f"background-color: {drag_color.name()};")
            self.setAlignment(Qt.AlignmentFlag.AlignCenter)
            raidlist.append(self.raider)
            event.source().hide()
            mbuffs = calculateBuffs(raidlist)
        else:
            event.ignore()



"""
GUI section
"""
#Define Main Window

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CB Cata Roster Tool")
        minw = 1500
        minh = 800
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
            if i % 6 == 0:
                i=0
                j+=1
        grouptitles = QGridLayout()
        grouptitles.setVerticalSpacing(3)
        grouptitles.setHorizontalSpacing(3)
        for i in range(1,6):
            lab = QLabel()
            lab.setText("Group "+str(i))
            lab.setAlignment(Qt.AlignmentFlag.AlignCenter)
            grouptitles.addWidget(lab,0,i)
        missingbuffs = QListWidget()
        for x in mbuffs:
            missingbuffs.addItems(x)
        rosterslots = QGridLayout()
        rosterslots.setVerticalSpacing(3)
        rosterslots.setHorizontalSpacing(3)
        for i in range(5):
            for j in range(5):
                label = DropLabel(mbwid=missingbuffs)
                label.setStyleSheet('background-color: gray;')
                rosterslots.addWidget(label,i,j)
        leftlayout.addLayout(gridlayout, stretch=6)
        leftlayout.addLayout(grouptitles, stretch=1)
        leftlayout.addLayout(rosterslots, stretch=5)
        outerlayout.addLayout(leftlayout, stretch=4)
        rightlayout = QVBoxLayout()
        resetbutton = QPushButton("Reset")
        resetbutton.clicked.connect(restart)
        rightlayout.addWidget(resetbutton)
        rightlayout.addWidget(missingbuffs)
        outerlayout.addLayout(rightlayout, stretch=1)
        rosterTab.setLayout(outerlayout)
        return rosterTab

 #Create the PA Management Tab   

    def addPATabUI(self, roster):
        PATab = QWidget()
        layout = QVBoxLayout()
        self.cb = QComboBox()
        for x in roster:
            self.cb.addItem(x.name)
        calendar = QCalendarWidget()
        layout.addWidget(self.cb)
        layout.addWidget(calendar)
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

    
