#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import json
import FilesWindow
   

class LinkFileWindow(gtk.Window):

    chosenFilePath = ''
    chosenCatalog = ''
    
    def __init__(self):
        super(LinkFileWindow, self).__init__()
        self.catalogComboBox = ''   
        self.set_title("Dodaj do katalogu nowa zakladke z plikiem.")
        self.set_default_size(350, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        labelCatalog = gtk.Label('Wybierz z rozwijanej listy katalog, w ktorym dodasz nowa zakladke.')
        catalogsList = gtk.combo_box_new_text()
        catalogsList.connect('changed', self.chooseCatalog)

        with open('Database.json') as json_file:
            data = json.load(json_file)
        catalogsAsKeys = data.keys()
        for cak in catalogsAsKeys:
            catalogsList.append_text(str(cak))
        
        newTab = gtk.Label('Wpisz nazwe nowej zakladki :')
        self.newTabName = gtk.Entry()    
        newPath = gtk.Label('Wklej lub wpisz sciezke pliku :')
        self.newTabPath = gtk.Entry()
        self.newTabPath.set_text(LinkFileWindow.chosenFilePath)
        buttonFindFile = gtk.Button('Znajdz plik')
        buttonFindFile.connect('clicked', self.windowFilesDriveC)
        buttonAddTab = gtk.Button('Dodaj')
        buttonAddTab.connect('clicked', self.addingTabWithPath)

        screen = gtk.Fixed()
        screen.put(labelCatalog, 10, 10)
        screen.put(catalogsList, 10, 30)
        screen.put(newTab, 10, 60)
        screen.put(self.newTabName, 10, 80)
        screen.put(newPath, 10, 120)
        screen.put(self.newTabPath, 10, 140)
        screen.put(buttonFindFile, 220, 140)
        screen.put(buttonAddTab, 10, 170)
        self.add(screen)
        self.show_all()
        return

    def chooseCatalog(self, widget):
        self.catalogComboBox = widget.get_active_text()
        LinkFileWindow.chosenCatalog = widget.get_active_text()
        
    def addingTabWithPath(self, widgets):
        with open('Database.json') as json_file:
            data = json.load(json_file)
        data[str(self.catalogComboBox)][str(self.newTabName.get_text())] = str(self.newTabPath.get_text()) 
        with open('Database.json', 'w') as outfile:
            json.dump(data, outfile)

    def windowFilesDriveC(self, widgets):
        FilesWindow.launch()

def launch():
    LinkFileWindow()
    gtk.main()
