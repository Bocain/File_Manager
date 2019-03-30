#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import json
   

class HttpWindow(gtk.Window):
    def __init__(self):
        super(HttpWindow, self).__init__()
        self.chosenCatalogComboBox = ''
        
        self.set_title("Dodaj do katalogu nowa zakladke z linkiem www.")
        self.set_default_size(350, 200)
        self.set_position(gtk.WIN_POS_CENTER)

        labelCatalog = gtk.Label('Wybierz z rozwijanej listy katalog, w ktorym dodasz nowa zakladke.')       
        catalogList = gtk.combo_box_new_text()
        catalogList.connect('changed', self.comboOption)
        
        with open('Database.json') as json_file:
            data = json.load(json_file)
        catalogsAsKeys = data.keys()
        for catalogAsKey in catalogsAsKeys:
            catalogList.append_text(str(catalogAsKey))
        
        labelNewTab = gtk.Label('Wpisz nazwe nowej zakladki :')
        self.entryNewTab = gtk.Entry()
        
        labelNewLink = gtk.Label('Wklej lub wpisz adres strony internetowej :')
        self.entryNewLink = gtk.Entry()
        
        buttonConfirmAdd = gtk.Button('Dodaj')
        buttonConfirmAdd.connect('clicked', self.AddingConfirmation)
        
        screen = gtk.Fixed()

        screen.put(labelCatalog, 10, 10)
        screen.put(catalogList, 10, 30)
               
        screen.put(labelNewTab, 10, 60)
        screen.put(self.entryNewTab, 10, 80)

        screen.put(labelNewLink, 10, 120)
        screen.put(self.entryNewLink, 10, 140)
        
        screen.put(buttonConfirmAdd, 10, 170)

        self.add(screen)
        self.show_all()
        
        return

    def comboOption(self, widget):
        self.chosenCatalogComboBox = widget.get_active_text()

    def AddingConfirmation(self, widgets):
        with open('Database.json') as json_file:
            data = json.load(json_file)           
        data[str(self.chosenCatalogComboBox)][str(self.entryNewTab.get_text())] = str(self.entryNewLink.get_text())
        with open('Database.json', 'w') as outfile:
            json.dump(data, outfile)

def launch():
    HttpWindow()
    gtk.main()
