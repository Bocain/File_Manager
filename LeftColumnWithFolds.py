#!/usr/bin/env python
# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import LeftColumnWithCatalogs
import MemberFunctions

class LeftColumnWithFolds():

    def __init__(self):
        self.tabsTree = gtk.TreeView()
        self.tabsTree.set_model(LeftColumnWithCatalogs.LeftColumnWithCatalogs.surrogateCatalog)
        subtabs_column = gtk.TreeViewColumn("Tematyczne linki do wybranej zakladki", gtk.CellRendererText(), text=0)
        self.tabsTree.append_column(subtabs_column)
        self.tabsTree.connect("row-activated", self.subtab_activated)
        self.tabsTree_sw = gtk.ScrolledWindow()
        self.tabsTree_sw.add(self.tabsTree)

    def subtab_activated(self, widget, row, col):
        model = widget.get_model()
        text = model[row][0]
        MemberFunctions.openLink(str(text))




