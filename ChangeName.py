#!/usr/bin/env python
# -*- coding: cp1250 -*-

import pygtk
import gtk
import LinkFileWindow

class ChosenFile(gtk.Window):
    def __init__(self, wybor_pliku):
        super(ChosenFile, self).__init__()

        self.connect("destroy", gtk.main_quit)
        
        self.set_default_size(400, 50)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_title("Czy potwierdzasz wybor pliku ?")

        btn_yes = gtk.Button('Tak')
        btn_yes.connect('clicked', self.button_yes, wybor_pliku)

        plik = gtk.Label(wybor_pliku)

        screen = gtk.Fixed()

        screen.put(plik, 10, 10)       
        screen.put(btn_yes, 10, 30)

        self.add(screen)
        self.show_all()
        gtk.main()
        return
        
    def button_yes(self, widgets, wybor_pliku):
        LinkFileWindow.LinkFileWindow.wybrany_plik = wybor_pliku
        LinkFileWindow.odpal()


