#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import json

class ChangeTabName(gtk.Window):
    def __init__(self):
        super(ChangeTabName, self).__init__()

        self.catalogComboBox = ''

        self.connect('destroy', gtk.main_quit)
        
        self.set_default_size(400, 50)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title('Wybierz zakladke i wpisz jej nowa nazwe.')

        self.entryTabName = gtk.Entry()
        self.entryTabName.set_text(' litery , cyfry , spacje , stopki ')

        buttonConfirm = gtk.Button('Potwierdz')
        buttonConfirm.connect('clicked', self.updateTabName)

        tabList = gtk.combo_box_new_text()
        tabList.connect('changed', self.chooseTab)
        
        with open('Database.json') as json_file:
            data = json.load(json_file)
        tabs = data.keys()
        for i in tabs:
            for j in data[i]:
                tabList.append_text(str(j))

        screen = gtk.Fixed()

        screen.put(tabList, 10, 10)       
        screen.put(self.entryTabName, 10, 40)
        screen.put(buttonConfirm, 10, 70)

        self.add(screen)
        self.show_all()
        gtk.main()
        return

    def chooseTab(self, widget):
        self.chosenTab = widget.get_active_text()
        
    def updateTabName(self, widgets):
        with open('Database.json') as json_file:
            data = json.load(json_file)
        catalogs = data.keys()
        for i in catalogs:
                for tab in data[i]:
                    if tab == self.chosenTab:
                        wartosc = data[i][tab]
                        data[i][str(self.entryTabName.get_text())] = wartosc
                        data[i].pop(tab, None)
                        with open('Database.json', 'w') as outfile:
                            json.dump(data, outfile)
                        return
                    
