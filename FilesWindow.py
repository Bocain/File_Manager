#!/usr/bin/env python
# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import graphics

FolderIcon, FileIcon = graphics.FolderIcon, graphics.FileIcon

class FilesWindow(object):

    SciezkaPliku = ''
    
    def __init__(self, dname = None, path_to_file = None):
        
        """nazwy kolumn"""
        column_names = ['Name', 'Size', 'Mode', 'Last Changed']

        """tworzy okno plik�w"""
        treeview = gtk.TreeView()
        listmodel = self.make_list(dname)
        
        """tworzy kolumny. cell_data_func pomija pierwsz� kolumn�."""
        cell_data_funcs = (None, self.file_size, self.file_mode, self.file_last_changed)
        tvcolumn = [None] * len(column_names)

        """pierwsza kolumna. dodanie nazwy kolumny i ikonek w tej kolumnie"""
        cellpb = gtk.CellRendererPixbuf()
        tvcolumn[0] = gtk.TreeViewColumn(column_names[0], cellpb)
        tvcolumn[0].set_cell_data_func(cellpb, self.file_pixbuf)

        """pierwsza kolumna. dodanie nazwy plik�w"""
        cell = gtk.CellRendererText()
        tvcolumn[0].pack_start(cell, False)
        tvcolumn[0].set_cell_data_func(cell, self.file_name)
        treeview.append_column(tvcolumn[0])

        """dodawanie nazw kolumn. dodaje do ka�dego pliku/pozycji rozmiar, kod dost�pu pliku, ostatni� zmian� w pliku."""
        for n in range(1, len(column_names)):
            cell = gtk.CellRendererText()
            tvcolumn[n] = gtk.TreeViewColumn(column_names[n], cell)
            if n == 1:
                cell.set_property('xalign', 1.0)
            tvcolumn[n].set_cell_data_func(cell, cell_data_funcs[n])
            treeview.append_column(tvcolumn[n])

        """funkcyjno�� okienka po podw�jnym klikni�ciu. zahaszowane linie s� jeszcze do dopracowania"""
        treeview.connect("row-activated", self.open_file)
        treeview.connect("row-activated", self.on_activated)
        treeview.set_model(listmodel)
        
        """umieszczenie okna plik�w w przewijanym okienku"""
        self.sw = gtk.ScrolledWindow()
        self.sw.add(treeview)

        return       
 
    def make_list(self, dname=None):
        """zwraca pe�n� list� plik�w z wybranej �cie�ki"""
        if not dname:
            """zwraca user home directory, czyli  Documents and Settings/IBM"""
            self.dirname = os.path.expanduser('~')
        else:
            """zwraca bie��c� �cie�ke, chyba do folderu z plikiem"""
            self.dirname = os.path.abspath(dname)

        """wy�witla �cie�k� w nag��wku okienka"""
        #self.set_title(self.dirname)

        """exploring the path. zahaszowane to eksperymenty"""
        files = [f for f in os.listdir(self.dirname) if f[0] <> '.']
        #files.sort()
        files = ['..'] + files
        listmodel = gtk.ListStore(object)
        for f in files:
            listmodel.append([f])
        return listmodel

    def open_file(self, treeview, path, column):
        """nie wiem nic. zahaszowane to eksperymenty. sk�d path?"""

        """zwraca powi�zany model, czyli treeview od gtk.TreeView"""
        model = treeview.get_model()

        """nie mam poj�cia co to robi"""
        iter = model.get_iter(path)
        filename = os.path.join(self.dirname, model.get_value(iter, 0))
        self.path_to_file = filename
        FilesWindow.SciezkaPliku = filename
        filestat = os.stat(filename)
        if stat.S_ISDIR(filestat.st_mode): 
            new_model = self.make_list(filename) 
            treeview.set_model(new_model) 
        return

    def file_pixbuf(self, column, cell, model, iter):
        """dobiera ikonki dla plik�w. sk�d iter?"""

        """pobiera nazwe pliku z pierwszej kolumny i ��czy go ze �cie�k�"""
        filename = os.path.join(self.dirname, model.get_value(iter, 0))

        """zwraca ca�� liste stat() dla pliku"""
        filestat = os.stat(filename)

        """dobiera ikonki dla folder/plik"""
        if stat.S_ISDIR(filestat.st_mode):
            pb = FolderIcon
        else:
            pb = FileIcon
        cell.set_property('pixbuf', pb)
        return

    def file_name(self, column, cell, model, iter):
        """'text' - text to render. """
        cell.set_property('text', model.get_value(iter, 0))
        return

    def file_size(self, column, cell, model, iter):
        """zwraca rozmiar pliku"""
        filename = os.path.join(self.dirname, model.get_value(iter, 0))
        filestat = os.stat(filename)
        """wy�wietla rozmiar pliku"""
        cell.set_property('text', filestat.st_size)
        return

    def file_mode(self, column, cell, model, iter):
        """zwraca file system permision numeric notation"""
        filename = os.path.join(self.dirname, model.get_value(iter, 0))
        filestat = os.stat(filename)
        cell.set_property('text', oct(stat.S_IMODE(filestat.st_mode)))
        return

    def file_last_changed(self, column, cell, model, iter):
        """zwraca czas ostaniej zmiany w pliku"""
        filename = os.path.join(self.dirname, model.get_value(iter, 0))
        filestat = os.stat(filename)
        """zamienia sekundy na standardowy format jako True. 'text' to specyfikacja, domy�lnie None. """
        cell.set_property('text', time.ctime(filestat.st_mtime))

    def on_activated(self, widget, row, col):
        model = widget.get_model()
        text = model[row][0]
        print text
