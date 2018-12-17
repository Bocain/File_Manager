#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import json

class ChangeNameTab(gtk.Window):
    def __init__(self):
        super(ChangeNameTab, self).__init__()

        self.catalogComboBox = ''

        self.connect("destroy", gtk.main_quit)
        
        self.set_default_size(400, 50)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title("Wybierz zakladke i wpisz jej nowa nazwe.")

        self.entry = gtk.Entry()
        self.entry.set_text("litery,cyfry,spacje,stopki")

        btn_yes = gtk.Button('Potwierdz')
        btn_yes.connect('clicked', self.button_yes)

        cb = gtk.combo_box_new_text()
        cb.connect('changed', self.comboOption)
        
        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)
        klucze_katalogi = caly_slownik.keys()
        for i in klucze_katalogi:
                for j in caly_slownik[i]:
                    cb.append_text(str(j))

        screen = gtk.Fixed()

        screen.put(cb, 10, 10)       
        screen.put(self.entry, 10, 40)
        screen.put(btn_yes, 10, 70)

        self.add(screen)
        self.show_all()
        gtk.main()
        return

    def comboOption(self, widget):
        self.catalogComboBox = widget.get_active_text()
        
    def button_yes(self, widgets):
        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)
        klucze_katalogi = caly_slownik.keys()
        for i in klucze_katalogi:
                for j in caly_slownik[i]:
                    if j == self.catalogComboBox:
                        wartosc = caly_slownik[i][j]
                        caly_slownik[i][str(self.entry.get_text())] = wartosc
                        caly_slownik[i].pop(j, None)
                        with open('json_test.json', 'w') as outfile:
                            json.dump(caly_slownik, outfile)
                        return
                    
