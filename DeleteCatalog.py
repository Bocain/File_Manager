#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import json
import LeftColumnWithCatalogs

class DeleteCatalog(gtk.Window):
    catalog = 'katalog_link'
    
    def __init__(self):
        super(DeleteCatalog, self).__init__()

        self.connect('destroy', gtk.main_quit)
        
        self.set_default_size(400, 50)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title('Czy potwierdzasz wybor pozycji ?')

        buttonConfirm = gtk.Button('Tak')
        buttonConfirm.connect('clicked', self.deleteConfirmation, DeleteCatalog.catalog)

        catalogName = gtk.Label(DeleteCatalog.catalog)

        screen = gtk.Fixed()

        screen.put(catalogName, 10, 10)       
        screen.put(buttonConfirm, 10, 30)

        self.add(screen)
        self.show_all()
        gtk.main()
        return
        
    def deleteConfirmation(self, widgets, catalog):
        catalog = catalog
        with open('Database.json') as json_file:
            data = json.load(json_file)

        catalogsAsKeys = data.keys()
        if catalog in catalogsAsKeys:
            data.pop(str(catalog), None)
            with open('Database.json', 'w') as outfile:
                json.dump(data, outfile)
            LeftColumnWithCatalogs.LeftColumnWithCatalogs()
        else:
            for i in catalogsAsKeys:
                for j in data[i]:
                    if j == catalog:
                        data[i].pop(j, None)
                        with open('Database.json', 'w') as outfile:
                            json.dump(data, outfile)
                        return
