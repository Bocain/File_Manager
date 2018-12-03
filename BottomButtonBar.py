# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
pygtk.require('2.0')
import gtk
import json
import RightColumnWithFiles
import LeftColumnWithCatalogs
import LeftColumnWithFolds

class BottomButtonBar(object):

    def __init__(self):
        self.BottomBar = gtk.Fixed()

        buttonErrase = gtk.Button("Usun pozycje")
        buttonErrase.connect("button_press_event", self.buttonErrase)
        buttonErrase.set_property("width-request", 90)
        buttonErrase.set_property("height-request", 30)

        
        buttonName = gtk.Button("Zmien nazwe katalogu")
        buttonName.connect("button_press_event", self.buttonName)
        buttonName.set_property("width-request", 90)
        buttonName.set_property("height-request", 30)

        self.BottomBar.put(buttonErrase, 1, 1)
        self.BottomBar.put(buttonName, 100, 1)

    def buttonErrase(self,widget,event):
        LeftColumnWithCatalogs.LeftColumnWithCatalogs()
##        print RightColumnWithFiles.RightColumnWithFiles.SciezkaPliku

    def buttonName(self,widget,event):       
        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)
            
        nowaNazwa = raw_input('Podaj nowa nazwe : ')
        
        asd = caly_slownik
        asd[nowaNazwa]=asd.pop(LeftColumnWithCatalogs.LeftColumnWithCatalogs.katalogZmiana)

        with open('json_test.json', 'w') as outfile:
            json.dump(asd, outfile)
        

        


        
