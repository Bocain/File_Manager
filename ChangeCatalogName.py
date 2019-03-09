#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import json
import LeftColumnWithCatalogs

class ChangeCatalogName(gtk.Window):
    def __init__(self):
        super(ChangeName, self).__init__()

        self.connect("destroy", gtk.main_quit)

        self.set_default_size(400, 50)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title("Wybierz katalog i wpisz jego nowa nazwe.")     

        self.entryCatalogName = gtk.Entry()
        self.entryCatalogName.set_text(" litery , cyfry , spacje , stopki ")

        buttonCONFIRM = gtk.Button('Potwierdz')
        buttonCONFIRM.connect('clicked', self.button_yes)
        
        self.catalogComboBox = ''
        self.chooseCatalog = gtk.combo_box_new_text()
        self.chooseCatalog.connect('changed', self.comboOption)
        chooseCatalogUploadList()
        
        screen = gtk.Fixed()
        screen.put(chooseCatalog, 10, 10)       
        screen.put(self.entryCatalogName, 10, 40)
        screen.put(buttonCONFIRM, 10, 70)

        self.add(screen)
        self.show_all()
        gtk.main()
        return

    def chooseCatalogUploadList(self):
        with open('json_test.json') as json_file:
            data = json.load(json_file)
        catalogs = data.keys()
        for catalog in catalogs:
            self.chooseCatalog.append_text(str(catalog))
        
    def comboOption(self, widget):
        self.catalogComboBox = widget.get_active_text()
        
    def button_yes(self, widgets):
        with open('json_test.json') as json_file:
            data = json.load(json_file)
        data[ str(self.entryCatalogName.get_text()) ] = data[ str(self.catalogComboBox) ]       
        data.pop(str(self.catalogComboBox), None)
        with open('json_test.json', 'w') as outfile:
            json.dump(data, outfile)            
        LeftColumnWithCatalogs.LeftColumnWithCatalogs()
