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
        
        buttonSaveRemarks = gtk.Button("Zapisz notatke")
        buttonSaveRemarks.connect("button_press_event", self.updateRemark)
        buttonSaveRemarks.set_property("width-request", 90)
        buttonSaveRemarks.set_property("height-request", 30)
        self.BottomBar.put(buttonSaveRemarks, 710, 1)

    def updateRemark(self,widget,event):
        remarks = RightColumnWithRemarks.RightColumnWithRemarks.view.get_buffer()
        firstLetterInRemarks = remarks.get_start_iter()
        lastLetterInRemarks = remarks.get_end_iter()
        wholeRemark = remarks.get_text(firstLetterInRemarks, lastLetterInRemarks)
        
        with open('Notes.json') as json_file:
            data = json.load(json_file)

        data["notatka"] = wholeRemark
        
        with open('Notes.json', 'w') as outfile:
            json.dump(data, outfile)
        

        


        
