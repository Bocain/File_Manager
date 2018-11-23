# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import json
import subprocess
import LeftColumnWithCatalogs  
import RightColumnWithFiles

import HttpWindow   

def FilePos_Hist(widget):
    print 'Wyswietl historie zakladek'

def FilePos_Impo(widget):
    print 'Importuje zakladki'

def FilePos_Eksp(widget):
    print 'Eskportuje zakladki'

def FilePos_Quit( widget):
    print 'Zamyka program'
    gtk.main_quit()
    os.remove("BottomButtonBar.pyc")
    os.remove("TopBookmarksBar.pyc")
    os.remove("MemberFunctions.pyc")
    os.remove("graphics.pyc")
    os.remove("LeftColumnWithCatalogs.pyc")
    os.remove("LeftColumnWithFolds.pyc")
    os.remove("RightColumnWithFiles.pyc")
    os.remove("HttpWindow.pyc")
    
    
def ToolsPos_AddKata( widget):
    print 'Dodaj katalog'
    
    with open('json_test.json') as json_file:
        data = json.load(json_file)
    var1 = raw_input('Podaj tytu� nowego katalogu : ')
    data[var1]={}
    with open('json_test.json', 'w') as outfile:
        json.dump(data, outfile)

def ToolsPos_AddLink( widget):
    print 'Dodaj odnosnik'
    
    with open('json_test.json') as json_file:
        data = json.load(json_file)
    var3 = raw_input('Podaj tytu� nowej zakladki : ')
    data[str(LeftColumnWithCatalogs.LeftColumnWithCatalogs.katalogBaza)][var3]= str(RightColumnWithFiles.RightColumnWithFiles.SciezkaPliku) 

    with open('json_test.json', 'w') as outfile:
        json.dump(data, outfile)

def ToolsPos_AddHttp( widget):
    print "strona internetowa"
    HttpWindow.odpal()
    
    
def ToolsPos_DelePosi( widget):
    print 'Usun pozycje'

def ToolsPos_ChanName( widget):
    print 'Zmien nazwe'

def ToolsPos_Help( widget):
    print 'Wyswietl instrukcje obslugi'

def ArrangementPos_Wide( widget):
    print 'Zmien szerokosc lewej kolumny'

def ArrangementPos_TallKata( widget):
    print 'Zmien wysokosc okienka katalogow'

def ArrangementPos_TallLink( widget):
    print 'Zmien wysokosc okienka odnosnikow'

def ArrangementPos_FontSizeKata( widget):
    print 'Zmien rozmiar czcionki katalogow'

def ArrangementPos_FontSizeLink( widget):
    print 'Zmien rozmiar czcionki odnosnikow'

def ArrangementPos_FontSizeFileTree( widget):
    print 'Zmien rozmiar czcionki nazw plikow'

def ArrangementPos_IkonChanKata( widget):
    print 'Zmien ikonke katalogu'

def ArrangementPos_IkonChanLink( widget):
    print 'Zmien ikonke odnosnika'

def openLink(zakladka):
    with open('json_test.json') as json_file:
        data = json.load(json_file)
    sciezka = data[str(LeftColumnWithCatalogs.LeftColumnWithCatalogs.katalogBaza)][str(zakladka)]
    try:
        os.startfile(str(sciezka))
    except:
        subprocess.call([r'C:\Program Files\Mozilla Firefox\Firefox.exe', '-new-tab', str(sciezka)])

    