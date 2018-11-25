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

class LeftColumnWithFolds():

    def __init__(self):

        """tworzenie okna zak�adek"""   
        subtabs_tree = gtk.TreeView()
        subtabs_tree.set_model(LeftColumnWithCatalogs.LeftColumnWithCatalogs.var_lista)
        subtabs_column = gtk.TreeViewColumn("Tematyczne linki do wybranej zakladki", gtk.CellRendererText(), text=0)
        subtabs_tree.append_column(subtabs_column)

        """funkcyjno�� okienka po podw�jnym klikni�ciu"""
        subtabs_tree.connect("row-activated", self.subtab_activated)

        """umieszczenie okna zak�adek w przewijanym okienku"""
        self.subtabs_tree_sw = gtk.ScrolledWindow()
        self.subtabs_tree_sw.add(subtabs_tree)

    def subtab_activated(self, widget, row, col):
        model = widget.get_model()
        text = model[row][0]
        MemberFunctions.openLink(str(text))

    def test_update_window(self, nothing):
        subtabs_tree.set_model(LeftColumnWithCatalogs.LeftColumnWithCatalogs.var_lista)



