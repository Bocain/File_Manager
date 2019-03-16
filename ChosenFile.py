#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import LinkFileWindow

class ChosenFile(gtk.Window):
    def __init__(self, wybor_pliku):
        super(ChosenFile, self).__init__()

        self.connect('destroy', gtk.main_quit)
        
        self.set_default_size(400, 50)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title('Czy potwierdzasz wybor pliku ?')

        buttonConfirm = gtk.Button('Tak')
        buttonConfirm.connect('clicked', self.chooseFile, chosenFilePath)

        filePath = gtk.Label(chosenFilePath)

        screen = gtk.Fixed()

        screen.put(filePath, 10, 10)       
        screen.put(buttonConfirm, 10, 30)

        self.add(screen)
        self.show_all()
        gtk.main()
        return
        
    def chooseFile(self, widgets, chosenFilePath):
        LinkFileWindow.LinkFileWindow.chosenFilePath = chosenFilePath
        LinkFileWindow.launch()


