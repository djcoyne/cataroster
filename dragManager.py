# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:10:33 2024

@author: CoyneDa
"""

class DragManager():
    def add_draggable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand1")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        pass

    def on_drag(self, event):
        x = event.x + event.widget.winfo_x()
        y = event.y + event.widget.winfo_y()
        event.widget.place(x=x, y=y, anchor="center")

    def on_drop(self, event):
        # find the widget under the cursor
        x,y = event.widget.winfo_pointerxy()