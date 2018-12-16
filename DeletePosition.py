#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import LeftColumnWithCatalogs
import json

class DeletePosition(gtk.Window):
    pozycja = 'katalog_link'
    
    def __init__(self):
        super(DeletePosition, self).__init__()

        self.connect("destroy", gtk.main_quit)
        
        self.set_default_size(400, 50)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title("Czy potwierdzasz wybor pozycji ?")

        btn_yes = gtk.Button('Tak')
        btn_yes.connect('clicked', self.button_yes, DeletePosition.pozycja)

        plik = gtk.Label(DeletePosition.pozycja)

        screen = gtk.Fixed()

        screen.put(plik, 10, 10)       
        screen.put(btn_yes, 10, 30)

        self.add(screen)
        self.show_all()
        gtk.main()
        return
        
    def button_yes(self, widgets, pozycja):
        pozycja = pozycja
        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)

        klucze_katalogi = caly_slownik.keys()
        if pozycja in klucze_katalogi:
            caly_slownik.pop(str(pozycja), None)
            with open('json_test.json', 'w') as outfile:
                json.dump(caly_slownik, outfile)
            LeftColumnWithCatalogs.LeftColumnWithCatalogs()
