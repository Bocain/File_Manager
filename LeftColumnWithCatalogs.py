#!/usr/bin/env python
# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import json
import DeleteCatalog

class LeftColumnWithCatalogs(object):

    catalogsList = gtk.ListStore(str)
    primaryCatalog = ''
    surrogateCatalog = ''
    allCatalogs = gtk.ListStore(str)
    
    def __init__(self):

        """tworzenie listy katalogów"""
        LeftColumnWithCatalogs.allCatalogs.clear()     
        with open('Database.json') as json_file:
            data = json.load(json_file)
        catalogsAsKeys = data.keys()
        for cak in catalogsAsKeys:
            LeftColumnWithCatalogs.allCatalogs.append([str(cak)])

        self.catalogsWindow = gtk.TreeView()     
        self.catalogsWindow.set_model(LeftColumnWithCatalogs.allCatalogs)
        self.catalogsColumn = gtk.TreeViewColumn("K a t a l o g i", gtk.CellRendererText(), text=0)
        self.catalogsWindow.append_column(self.catalogsColumn)
        self.catalogsWindow.connect("row-activated", self.windowRefresh)
        self.selection = self.catalogsWindow.get_selection()
        self.selection.connect("changed", self.changeTabsWindowAsCatalogChange)
        self.catalogsWindow_sw = gtk.ScrolledWindow()
        self.catalogsWindow_sw.add(self.catalogsWindow)

    def windowRefresh(self, widget, row, col):
        LeftColumnWithCatalogs.catalogsList.clear()
        model = widget.get_model()
        text = model[row][0]
        LeftColumnWithCatalogs.primaryCatalog = text
        with open('Database.json') as json_file:
            data = json.load(json_file)
        catalogsAsKeys = data[str(text)].keys()
        for cak in catalogsAsKeys:
            LeftColumnWithCatalogs.catalogsList.append([str(cak)])        
            
    def changeTabsWindowAsCatalogChange(self, selection):        
        (model, iter) = selection.get_selected()
        LeftColumnWithCatalogs.surrogateCatalog = str(model[iter][0])
        
