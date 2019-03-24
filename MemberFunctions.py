# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import json
import subprocess
import LeftColumnWithCatalogs  
import HttpWindow
import LinkFileWindow
import AddCatalog
import ChangeCatalogName
import HelpWindow
import DeleteCatalog
import ChangeTabName

def FilePos_Quit( widget):
    print 'Zamyka program'
    gtk.main_quit()
    os.remove("BottomButtonBar.pyc")
    os.remove("TopBookmarksBar.pyc")
    os.remove("MemberFunctions.pyc")
    os.remove("Graphics.pyc")
    os.remove("LeftColumnWithCatalogs.pyc")
    os.remove("LeftColumnWithFolds.pyc")
    os.remove("HttpWindow.pyc")
    os.remove("LinkFileWindow.pyc")
    os.remove("RightColumnWithRemarks.pyc")
    os.remove("FilesWindow.pyc")
    os.remove("ChosenFile.pyc")
    os.remove("AddCatalog.pyc")
    os.remove("ChangeCatalogName.pyc")
    os.remove("ChangeTabName.pyc")
    os.remove("HelpWindow.pyc")
    os.remove("DeleteCatalog.pyc")
    
    
def ToolsPos_AddKata( widget):
    AddCatalog.AddCatalog()

def ToolsPos_AddLink( widget):
    LinkFileWindow.launch()

def ToolsPos_AddHttp( widget):
    HttpWindow.launch()
    
def ToolsPos_DelePosi( widget):
    DeleteCatalog.DeleteCatalog()

def ToolsPos_ChangName( widget):
    ChangeCatalogName.ChangeCatalogName()

def ToolsPos_ChangNameTab( widget):
    ChangeTabName.ChangeTabName()

def ToolsPos_Help( widget):
    HelpWindow.HelpWindow()

def openLink(tab):
    with open('Database.json') as json_file:
        data = json.load(json_file)
    path = data[str(LeftColumnWithCatalogs.LeftColumnWithCatalogs.primaryCatalog)][str(tab)]
    try:
        os.startfile(str(path))
    except:
        subprocess.call([r'C:\Program Files\Mozilla Firefox\Firefox.exe', '-new-tab', str(path)])

def drzewko(): 
    """Zwraca listę dysków. Metoda niezaimplementowana."""
    disks = []
    for x in range(65, 90):
        if os.path.exists(chr(x) + ':\\'):
            disks.append(chr(x))
    return disks    
