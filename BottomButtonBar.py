# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
pygtk.require('2.0')
import gtk
import json
import LeftColumnWithCatalogs
import LeftColumnWithFolds
import RightColumnWithRemarks

class BottomButtonBar(object):

    def __init__(self):
        self.BottomBar = gtk.Fixed()
        
        buttonName = gtk.Button("Zapisz notatke")
        buttonName.connect("button_press_event", self.buttonNotatka)
        buttonName.set_property("width-request", 90)
        buttonName.set_property("height-request", 30)
        self.BottomBar.put(buttonName, 100, 1)

    def buttonNotatka(self,widget,event):
        a = RightColumnWithRemarks.RightColumnWithRemarks.view.get_buffer()
        si = a.get_start_iter()
        ei = a.get_end_iter()
        text = a.get_text(si, ei)
        
        with open('json_notatka.json') as json_file:
            slownik = json.load(json_file)

        slownik["notatka"] = text
        
        with open('json_notatka.json', 'w') as outfile:
            json.dump(slownik, outfile)
        

        


        
