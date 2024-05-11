# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:10:33 2024

@author: CoyneDa
"""
from PyQt6.QtCore import QMimeData, Qt
from PyQt6.QtGui import QDrag
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget, QLabel

class dragManager(QLabel):
    def __init__(self, master, raider, x, y, text, width, height, color, anchor="center"):
        super().__init__(master, text=text, width=width, height=height, bg=color, anchor=anchor)
        self.x0, self.y0 = x,y
        self.raider = raider
        self.bind("<Button-1>", self.on_drag_start)
        self.bind("<B1-Motion>", self.on_drag_move)
        self.bind("<ButtonRelease-1>", self.on_drag_end)
        self.configure(cursor="hand1")

    def on_drag_start(self, event):
        self.xstart = event.x
        self.ystart = event.y

    def on_drag_move(self, event):
        widget=event.widget
        self.x = widget.winfo_x() + event.x
        self.y = widget.winfo_y() + event.y
        self.lift()
        self.place(x=self.x,y=self.y, anchor="center")

    def on_drag_end(self, event):
        widget=event.widget
        self.x = widget.winfo_pointerx() - self.xstart + event.x
        self.y = widget.winfo_pointery() - self.ystart + event.y
        curx = widget.winfo_pointerx()
        cury = widget.winfo_pointery()
        print(curx, cury)
        if 300 < curx < 1800 & 700 < cury < 1300:
            i = curx//300
            print(i)
            j = cury//100
            print(j)
            widget.grid(row=j, column=i, sticky='nsew', padx=3, pady=3)
        else:
            widget.grid(row=self.x0,column=self.y0, sticky='nsew', padx=3, pady=3)
            
    def reset(self):
        self.grid(row=self.x0,column=self.y0, sticky='nsew', padx=3, pady=3 )
        