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
##        ToolsPos_ChanName = gtk.MenuItem('_Zmien nazwe')
##        ToolsPos_ChanName.connect('activate', MemberFunctions.ToolsPos_ChanName)
        ToolsPos_Help = gtk.MenuItem('_Pomoc')
        ToolsPos_Help.connect('activate', MemberFunctions.ToolsPos_Help)
        
        ToolsList.append(ToolsPos_AddKata)
        ToolsList.append(ToolsPos_AddLink)
        ToolsList.append(ToolsPos_AddHttp)
        ToolsList.append(ToolsPos_DelePosi)
##        ToolsList.append(ToolsPos_ChanName)
        ToolsList.append(ToolsPos_Help)

        ArrangementList = gtk.Menu()
        ArrangementFold = gtk.MenuItem('_Konfiguracja')
        ArrangementPos_Wide = gtk.MenuItem('_Szerokosc lewej kolumny')
        ArrangementPos_Wide.connect('activate', MemberFunctions.ArrangementPos_Wide)
        ArrangementPos_TallKata = gtk.MenuItem('_Wysokosc okienka zakladek')
        ArrangementPos_TallKata.connect('activate', MemberFunctions.ArrangementPos_TallKata)
        ArrangementPos_TallLink = gtk.MenuItem('_Wysokosc okienka linkow')
        ArrangementPos_TallLink.connect('activate', MemberFunctions.ArrangementPos_TallLink)
        ArrangementPos_FontSizeKata = gtk.MenuItem('_Rozmiar czcionki zakladek')
        ArrangementPos_FontSizeKata.connect('activate', MemberFunctions.ArrangementPos_FontSizeKata)
        ArrangementPos_FontSizeLink = gtk.MenuItem('_Rozmiar czcionki linkow')
        ArrangementPos_FontSizeLink.connect('activate', MemberFunctions.ArrangementPos_FontSizeLink)
        ArrangementPos_FontSizeFileTree = gtk.MenuItem('_Rozmiar czcionki listy plikow')
        ArrangementPos_FontSizeFileTree.connect('activate', MemberFunctions.ArrangementPos_FontSizeFileTree)
        ArrangementPos_IkonChanKata = gtk.MenuItem('_Zmiana ikonki zakladek')
        ArrangementPos_IkonChanKata.connect('activate', MemberFunctions.ArrangementPos_IkonChanKata)
        ArrangementPos_IkonChanLink = gtk.MenuItem('_Zmiana ikonki linkow')
        ArrangementPos_IkonChanLink.connect('activate', MemberFunctions.ArrangementPos_IkonChanLink)
        
        ArrangementList.append(ArrangementPos_Wide)
        ArrangementList.append(ArrangementPos_TallKata)
        ArrangementList.append(ArrangementPos_TallLink)
        ArrangementList.append(ArrangementPos_FontSizeKata)
        ArrangementList.append(ArrangementPos_FontSizeLink)
        ArrangementList.append(ArrangementPos_FontSizeFileTree)
        ArrangementList.append(ArrangementPos_IkonChanKata)
        ArrangementList.append(ArrangementPos_IkonChanLink)
        
        FileFold.set_submenu(FileList)
        ToolsFold.set_submenu(ToolsList)
        ArrangementFold.set_submenu(ArrangementList)

        self.TopBar.append(FileFold)
        self.TopBar.append(ToolsFold)
        self.TopBar.append(ArrangementFold)

        return
