# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import json
import subprocess
import LeftColumnWithCatalogs  
import HttpWindow
import LinkFileWindow
import AddKatalog
import ChangeName
import HelpWindow
import DeletePosition
import ChangeNameTab

def FilePos_Quit( widget):
    print 'Zamyka program'
    gtk.main_quit()
    os.remove("BottomButtonBar.pyc")
    os.remove("TopBookmarksBar.pyc")
    os.remove("MemberFunctions.pyc")
    os.remove("graphics.pyc")
    os.remove("LeftColumnWithCatalogs.pyc")
    os.remove("LeftColumnWithFolds.pyc")
    os.remove("HttpWindow.pyc")
    os.remove("LinkFileWindow.pyc")
    os.remove("RightColumnWithRemarks.pyc")
    os.remove("FilesWindow.pyc")
    os.remove("ChosenFile.pyc")
    os.remove("AddKatalog.pyc")
    os.remove("ChangeName.pyc")
    os.remove("ChangeNameTab.pyc")
    os.remove("HelpWindow.pyc")
    os.remove("DeletePosition.pyc")
    
    
def ToolsPos_AddKata( widget):
    AddKatalog.AddKatalog()


def ToolsPos_AddLink( widget):
    LinkFileWindow.odpal()
    
    
##    with open('json_test.json') as json_file:
##        data = json.load(json_file)
##    var3 = raw_input('Podaj tytuł nowej zakladki : ')
##    data[str(LeftColumnWithCatalogs.LeftColumnWithCatalogs.katalogBaza)][var3]= str(RightColumnWithFiles.RightColumnWithFiles.SciezkaPliku) 
##
##    with open('json_test.json', 'w') as outfile:
##        json.dump(data, outfile)

def ToolsPos_AddHttp( widget):
    HttpWindow.odpal()
    
def ToolsPos_DelePosi( widget):
    DeletePosition.DeletePosition()

def ToolsPos_ChangName( widget):
    ChangeName.ChangeName()

def ToolsPos_ChangNameTab( widget):
    ChangeNameTab.ChangeNameTab()

def ToolsPos_Help( widget):
    HelpWindow.HelpWindow()

def openLink(zakladka):
    with open('json_test.json') as json_file:
        data = json.load(json_file)
    sciezka = data[str(LeftColumnWithCatalogs.LeftColumnWithCatalogs.katalogBaza)][str(zakladka)]
    try:
        os.startfile(str(sciezka))
    except:
        subprocess.call([r'C:\Program Files\Mozilla Firefox\Firefox.exe', '-new-tab', str(sciezka)])

def drzewko(): 
    """zwraca listę dysków. później to wykorzystam."""
    dyski = []
    for x in range(65, 90):
        if os.path.exists(chr(x) + ':\\'):
            dyski.append(chr(x))
    return dyski    
