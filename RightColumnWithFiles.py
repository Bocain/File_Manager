#!/usr/bin/env python
# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import graphics
import json

FolderIcon, FileIcon = graphics.FolderIcon, graphics.FileIcon

class RightColumnWithFiles(object):

    SciezkaPliku = ''
    
    def __init__(self, dname = None, path_to_file = None):
        
        column_names = ['Name']
        cell_data_funcs = (None)
        tvcolumn = [None]
        cellpb = gtk.CellRendererPixbuf()
        tvcolumn[0] = gtk.TreeViewColumn(column_names[0], cellpb)
        tvcolumn[0].set_cell_data_func(cellpb, self.file_pixbuf)
        cell = gtk.CellRendererText()
        tvcolumn[0].pack_start(cell, False)
        tvcolumn[0].set_cell_data_func(cell, self.file_name)

        self.treeview = gtk.TreeView()
        listmodel = self.make_list(dname)
        self.treeview.append_column(tvcolumn[0])

        self.treeview.connect("row-activated", self.open_file)
        self.treeview.connect("row-activated", self.on_activated)
        self.treeview.set_model(listmodel)
        
        self.sw = gtk.ScrolledWindow()
        self.sw.add(self.treeview)
        return       

    def test_katalogow(self, nothing):
        tabs_store = gtk.ListStore(str)
        with open('json_test.json') as json_file:
            caly_slownik = json.load(json_file)
        klucze = caly_slownik.keys()
        for tab in klucze:
            tabs_store.append([str(tab)])
        self.treeview.set_model(tabs_store)
        
    def make_list(self, dname=None):
        if not dname:
            self.dirname = os.path.expanduser('~')
        else:
            self.dirname = os.path.abspath(dname)
            
        files = [f for f in os.listdir(self.dirname) if f[0] <> '.']
        files = ['..'] + files
        listmodel = gtk.ListStore(object)
        for f in files:
            listmodel.append([f])
        return listmodel

    def open_file(self, treeview, path, column):
        
        model = self.treeview.get_model()
        iter = model.get_iter(path)
        filename = os.path.join(self.dirname, model.get_value(iter, 0))
        self.path_to_file = filename
        RightColumnWithFiles.SciezkaPliku = filename
        filestat = os.stat(filename)
        if stat.S_ISDIR(filestat.st_mode): 
            new_model = self.make_list(filename) 
            self.treeview.set_model(new_model) 
        return

    def file_name(self, column, cell, model, iter):
        """'text' - text to render. """
        cell.set_property('text', model.get_value(iter, 0))
        return

    def on_activated(self, widget, row, col):
        model = widget.get_model()
        text = model[row][0]
        print text
        
    def file_pixbuf(self, column, cell, model, iter):
        """dobiera ikonki dla plików. skąd iter?"""

        """pobiera nazwe pliku z pierwszej kolumny i łączy go ze ścieżką"""
        filename = os.path.join(self.dirname, model.get_value(iter, 0))

        """zwraca całą liste stat() dla pliku"""
        filestat = os.stat(filename)

        """dobiera ikonki dla folder/plik"""
        if stat.S_ISDIR(filestat.st_mode):
            pb = FolderIcon
        else:
            pb = FileIcon
        cell.set_property('pixbuf', pb)
        return
