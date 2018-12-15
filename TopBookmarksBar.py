# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import MemberFunctions
  
class TopBookmarksBar(object):
    def __init__(self):
        self.TopBar = gtk.MenuBar()

        FileList = gtk.Menu()
        FileFold = gtk.MenuItem('_Plik')
        FileFold = gtk.ImageMenuItem(gtk.STOCK_OPEN)
        FilePos_Hist = gtk.MenuItem('_Historia')
        FilePos_Hist.connect('activate', MemberFunctions.FilePos_Hist)
        FilePos_Impo = gtk.MenuItem('_Importuj zakladki')
        FilePos_Impo.connect('activate', MemberFunctions.FilePos_Impo)
        FilePos_Eksp = gtk.MenuItem('_Eksportuj zakladki')
        FilePos_Eksp.connect('activate', MemberFunctions.FilePos_Eksp)        
        FilePosSeparator = gtk.SeparatorMenuItem()
        FilePos_Quit = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        FilePos_Quit.connect('activate', MemberFunctions.FilePos_Quit)

        FileList.append(FilePos_Hist)
        FileList.append(FilePos_Impo)
        FileList.append(FilePos_Eksp)
        FileList.append(FilePosSeparator)
        FileList.append(FilePos_Quit)        

        ToolsList = gtk.Menu()
        ToolsFold = gtk.MenuItem('_Narzedzia')
        ToolsPos_AddKata = gtk.MenuItem('_Dodaj katalog')
        ToolsPos_AddKata.connect('activate', MemberFunctions.ToolsPos_AddKata)
        ToolsPos_AddLink = gtk.MenuItem('_Dodaj link')
        ToolsPos_AddLink.connect('activate', MemberFunctions.ToolsPos_AddLink)
        ToolsPos_AddHttp = gtk.MenuItem('_Dodaj http')
        ToolsPos_AddHttp.connect('activate', MemberFunctions.ToolsPos_AddHttp)
        ToolsPos_DelePosi = gtk.MenuItem('_Usun pozycje')
        ToolsPos_DelePosi.connect('activate', MemberFunctions.ToolsPos_DelePosi)
        ToolsPos_ChangName = gtk.MenuItem('_Zmien nazwe')
        ToolsPos_ChangName.connect('activate', MemberFunctions.ToolsPos_ChangName)
        ToolsPos_Help = gtk.MenuItem('_Pomoc')
        ToolsPos_Help.connect('activate', MemberFunctions.ToolsPos_Help)
        
        ToolsList.append(ToolsPos_AddKata)
        ToolsList.append(ToolsPos_AddLink)
        ToolsList.append(ToolsPos_AddHttp)
        ToolsList.append(ToolsPos_DelePosi)
        ToolsList.append(ToolsPos_ChangName)
        ToolsList.append(ToolsPos_Help)
        
        FileFold.set_submenu(FileList)
        ToolsFold.set_submenu(ToolsList)

        self.TopBar.append(FileFold)
        self.TopBar.append(ToolsFold)

        return
