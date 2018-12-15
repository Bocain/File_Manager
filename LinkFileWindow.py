#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import json
import FilesWindow
   

class LinkFileWindow(gtk.Window):

    wybrany_plik = 'Miejsce na sciezke pliku'
    wybrany_katalog = ''
    
    def __init__(self):
        super(LinkFileWindow, self).__init__()

        self.catalogComboBox = ''
        
        self.set_title("Dodaj do katalogu nowa zakladke z plikiem.")
        self.set_default_size(350, 200)
        self.set_position(gtk.WIN_POS_CENTER)

        lb_katalog = gtk.Label('Wybierz z rozwijanej listy katalog, w ktorym dodasz nowa zakladke.')

        
        cb = gtk.combo_box_new_text()
        cb.connect('changed', self.comboOption)

        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)
        klucze = caly_slownik.keys()
        for tab in klucze:
            cb.append_text(str(tab))
        
        lb_1 = gtk.Label('Wpisz nazwe nowej zakladki :')
        self.entry_1 = gtk.Entry()
        
        lb_2 = gtk.Label('Wklej lub wpisz sciezke pliku :')
        self.entry_2 = gtk.Entry()
        self.entry_2.set_text(LinkFileWindow.wybrany_plik)

        btn_file = gtk.Button('Znajdz plik')
        btn_file.connect('clicked', self.button_find_file)
        
        btn_add = gtk.Button('Dodaj')
        btn_add.connect('clicked', self.button_add)
        
        screen = gtk.Fixed()

        screen.put(lb_katalog, 10, 10)
        screen.put(cb, 10, 30)
               
        screen.put(lb_1, 10, 60)
        screen.put(self.entry_1, 10, 80)

        screen.put(lb_2, 10, 120)
        screen.put(self.entry_2, 10, 140)
        
        screen.put(btn_file, 220, 140)
        screen.put(btn_add, 10, 170)

        self.add(screen)
        self.show_all()
        return

    def comboOption(self, widget):
        self.catalogComboBox = widget.get_active_text()
        LinkFileWindow.wybrany_katalog = widget.get_active_text()
        

    def button_add(self, widgets):
        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)
            
        caly_slownik[str(self.catalogComboBox)][str(self.entry_1.get_text())] = str(self.entry_2.get_text()) 

        with open('json_test.json', 'w') as outfile:
            json.dump(caly_slownik, outfile)

    def button_find_file(self, widgets):
        FilesWindow.odpal()
        print('Otwiera okno z plikami')


def odpal():
    LinkFileWindow()
    gtk.main()
