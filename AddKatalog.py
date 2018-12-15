#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import json
import LeftColumnWithCatalogs

class AddKatalog(gtk.Window):
    def __init__(self):
        super(AddKatalog, self).__init__()
        
        self.entry = gtk.Entry()

        self.entry.set_text("litery,cyfry,spacje,stopki")

        self.connect("destroy", gtk.main_quit)
        
        self.set_default_size(400, 50)
        self.set_position(gtk.WIN_POS_CENTER)

        self.set_title("Wprowadz nazwe nowej zakladki ?")

        btn_name = gtk.Button('Potwierdz')
        btn_name.connect('clicked', self.button_name)

        screen = gtk.Fixed()

        screen.put(self.entry, 10, 10)       
        screen.put(btn_name, 10, 30)

        self.add(screen)
        self.show_all()
        gtk.main()
        return
        
    def button_name(self, widgets):   
        with open('json_test.json') as json_file:
            data = json.load(json_file)
            
        klucze = data.keys()
        var = str(self.entry.get_text())

        if var in klucze:
            print"nazwa juz istnieje"
        else:
            data[var]={}
            with open('json_test.json', 'w') as outfile:
                json.dump(data, outfile)
            LeftColumnWithCatalogs.LeftColumnWithCatalogs()
