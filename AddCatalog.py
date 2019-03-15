#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import json
import LeftColumnWithCatalogs

class AddCatalog(gtk.Window):
    def __init__(self):
        super(AddCatalog, self).__init__()

        self.connect('destroy', gtk.main_quit)
        
        self.set_default_size(400, 50)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title('Wprowadz nazwe nowej zakladki.')

        self.entryCatalogName = gtk.Entry()
        self.entryCatalogName.set_text(' litery , cyfry , spacje , stopki ') 

        buttonConfirm = gtk.Button('Potwierdz')
        buttonConfirm.connect('clicked', self.addingCatalog)

        screen = gtk.Fixed()
        screen.put(self.entryCatalogName, 10, 10)       
        screen.put(buttonConfirm, 10, 30)

        self.add(screen)
        self.show_all()
        gtk.main()
        return
        
    def addingCatalog(self, widgets):   
        with open('json_test.json') as json_file:
            programsContent = json.load(json_file)
            
        existingCatalogs = data.keys()
        newCatalogName = str(self.entry.get_text())

        if newCatalogName in existingCatalogs:
            print 'nazwa juz istnieje'
        else:
            programsContent[newCatalogName]={}
            with open('json_test.json', 'w') as outfile:
                json.dump(programsContent, outfile)
            LeftColumnWithCatalogs.LeftColumnWithCatalogs()
