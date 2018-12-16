#!/usr/bin/env python
# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import graphics
import subprocess
import LeftColumnWithCatalogs
import MemberFunctions
import BottomButtonBar
import DeletePosition

class LeftColumnWithFolds():

    def __init__(self):

        """tworzenie okna zakładek"""   
        self.subtabs_tree = gtk.TreeView()
        
        self.subtabs_tree.set_model(LeftColumnWithCatalogs.LeftColumnWithCatalogs.var_lista)
        
        subtabs_column = gtk.TreeViewColumn("Tematyczne linki do wybranej zakladki", gtk.CellRendererText(), text=0)
        self.subtabs_tree.append_column(subtabs_column)

        """funkcyjność okienka po podwójnym kliknięciu"""
        self.subtabs_tree.connect("row-activated", self.subtab_activated)

        selection = self.subtabs_tree.get_selection()
        selection.connect("changed", self.pozycjaKatalogu)

        """umieszczenie okna zakładek w przewijanym okienku"""
        self.subtabs_tree_sw = gtk.ScrolledWindow()
        self.subtabs_tree_sw.add(self.subtabs_tree)

    def subtab_activated(self, widget, row, col):
        model = widget.get_model()
        text = model[row][0]
        MemberFunctions.openLink(str(text))

    def pozycjaKatalogu(self, selection):        
        (model, iter) = selection.get_selected()
        DeletePosition.DeletePosition.pozycja = str(model[iter][0])




