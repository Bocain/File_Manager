#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import json

class HttpWindow(gtk.Window):
    def __init__(self):
        super(HttpWindow, self).__init__()

        self.catalogComboBox = ''
        
        self.set_title("Dodaj nowa zakladke do katalogu.")
        self.set_default_size(350, 200)
        self.set_position(gtk.WIN_POS_CENTER)

        lb_katalog = gtk.Label('Wybierz z rozwijanej listy katalog, w ktorym dodasz nowa zakladke.')
##        self.entry_katalog = gtk.Entry()

        
        cb = gtk.combo_box_new_text()
        cb.connect('changed', self.comboOption)
##        cb.append_text('Create catalogue')
##        cb.append_text('Delete catalogue')
##        cb.append_text('Add commment to catalogue')
        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)
        klucze = caly_slownik.keys()
        for tab in klucze:
            cb.append_text(str(tab))
        
        lb_1 = gtk.Label('Wpisz nazwe nowej zakladki :')
        self.entry_1 = gtk.Entry()
        
        lb_2 = gtk.Label('Wklej lub wpisz adres strony internetowej :')
        self.entry_2 = gtk.Entry()
        
        btn_add = gtk.Button('Dodaj')
        btn_add.connect('clicked', self.button_add)

        btn_errase = gtk.Button('Anuluj')
        btn_errase.connect('clicked', self.button_errase)
        
##        box_main = gtk.VBox()
        screen = gtk.Fixed()

        screen.put(lb_katalog, 10, 10)
##        screen.put(self.entry_katalog, 10, 30)
        screen.put(cb, 10, 30)
               
        screen.put(lb_1, 10, 60)
        screen.put(self.entry_1, 10, 80)

        screen.put(lb_2, 10, 120)
        screen.put(self.entry_2, 10, 140)
        
        screen.put(btn_add, 10, 170)
        screen.put(btn_errase, 55, 170)
        
        
##        box_main.pack_start()
##        box_main.pack_start()
##        self.add(box_main)

        self.add(screen)
        self.show_all()
        return

    def comboOption(self, widget):
        self.catalogComboBox = widget.get_active_text()

    def button_add(self, widgets):
        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)
            
        caly_slownik[str(self.catalogComboBox)][str(self.entry_1.get_text())]= str(self.entry_2.get_text()) 

        with open('json_test.json', 'w') as outfile:
            json.dump(caly_slownik, outfile)
            
        print "Dodałeś nową zakładkę"

        
    def button_errase(self, widgets):
        print('Resetuje ustawienia')


def odpal():
    HttpWindow()
    gtk.main()

#odpal()
