#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import json
import LeftColumnWithCatalogs

class ChangeName(gtk.Window):
    def __init__(self):
        super(ChangeName, self).__init__()

        self.catalogComboBox = ''

        self.connect("destroy", gtk.main_quit)
        
        self.set_default_size(400, 50)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title("Wybierz katalog i wpisz jego nowa nazwe.")

        self.entry = gtk.Entry()
        self.entry.set_text("litery,cyfry,spacje,stopki")

        btn_yes = gtk.Button('Potwierdz')
        btn_yes.connect('clicked', self.button_yes)

        cb = gtk.combo_box_new_text()
        cb.connect('changed', self.comboOption)
        
        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)
        klucze = caly_slownik.keys()
        for tab in klucze:
            cb.append_text(str(tab))

        screen = gtk.Fixed()

        screen.put(cb, 10, 10)       
        screen.put(self.entry, 10, 30)
        screen.put(btn_yes, 10, 60)

        self.add(screen)
        self.show_all()
        gtk.main()
        return

    def comboOption(self, widget):
        self.catalogComboBox = widget.get_active_text()
        
    def button_yes(self, widgets):
        with open('json_test.json') as json_file:
            data = json.load(json_file)
            
        klucze = data.keys()

        data[str(self.entry.get_text())]= klucze[str(self.catalogComboBox)]
        
        with open('json_test.json', 'w') as outfile:
            json.dump(data, outfile)
        LeftColumnWithCatalogs.LeftColumnWithCatalogs()
