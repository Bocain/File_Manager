#!/usr/bin/env python
# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import graphics
import json
import BottomButtonBar

FolderIcon, FileIcon = graphics.FolderIcon, graphics.FileIcon

def refreshWindowTabs():
    return LeftColumnWithCatalogs.var_lista

class LeftColumnWithCatalogs(object):

    var_lista = gtk.ListStore(str)
    katalogBaza = ''
    katalogZmiana = ''
    
    def __init__(self, dname = None, path_to_file = None):    
        
        """tworzenie listy katalogów"""
        self.tabs_store = gtk.ListStore(str)
        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)
        klucze = caly_slownik.keys()
        for tab in klucze:
            self.tabs_store.append([str(tab)])

        print "poszla kolumna"
        
        self.tabs_tree = gtk.TreeView()
        self.tabs_tree.set_model(self.tabs_store)
            
        self.tabs_column = gtk.TreeViewColumn("K a t a l o g i", gtk.CellRendererText(), text=0)
        self.tabs_tree.append_column(self.tabs_column)

        """funkcyjność okienka po podwójnym kliknięciu"""
        self.tabs_tree.connect("row-activated", self.tab_activated)

        """wybrany wiersz emituje sygnal"""
        self.selection = self.tabs_tree.get_selection()
        self.selection.connect("changed", self.pozycjaKatalogu)
        
        """umieszczenie okna katalogów w przewijanym okienku"""
        self.tabs_tree_sw = gtk.ScrolledWindow()
        self.tabs_tree_sw.add(self.tabs_tree)

       
    def tab_activated(self, widget, row, col):
        LeftColumnWithCatalogs.var_lista.clear()
        model = widget.get_model()
        text = model[row][0]
        LeftColumnWithCatalogs.katalogBaza = text
        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)
        asd = caly_slownik[str(text)].keys()
        for tab2 in asd:
            LeftColumnWithCatalogs.var_lista.append([str(tab2)])        
            
    def pozycjaKatalogu(self, selection):        
        (model, iter) = selection.get_selected()
        LeftColumnWithCatalogs.katalogZmiana = str(model[iter][0])
        
        if iter is not None:
            text = model[iter][0]

        else:
            text = "brak iter ???"

        print str(text)




