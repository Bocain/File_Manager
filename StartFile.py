#!/usr/bin/env python
# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import TopBookmarksBar
import BottomButtonBar
import RightColumnWithRemarks
import LeftColumnWithCatalogs
import LeftColumnWithFolds

class StartFile(gtk.Window):
    def __init__(self):
        super(StartFile, self).__init__()
        self.set_default_size(800, 640)
        self.set_position(gtk.WIN_POS_CENTER)

        TopBar = TopBookmarksBar.TopBookmarksBar()
        BottomBar = BottomButtonBar.BottomButtonBar()
        RightColumn = RightColumnWithRemarks.RightColumnWithRemarks()
        LeftColumnCatalogs = LeftColumnWithCatalogs.LeftColumnWithCatalogs()
        LeftColumnFolds = LeftColumnWithFolds.LeftColumnWithFolds()

        box_main = gtk.VBox()
        box_side = gtk.HBox()
        box_tabs = gtk.VBox()

        box_main.pack_start(TopBar.TopBar, False, False, 0)
        box_tabs.pack_start(LeftColumnCatalogs.catalogsWindow_sw)
        box_tabs.pack_start(LeftColumnFolds.tabsTree_sw)
        box_side.pack_start(box_tabs)
        box_side.pack_start(RightColumn.notesWindow, True, True, 0)
        box_main.pack_start(box_side)
        box_main.pack_start(BottomBar.BottomBar, False, False, 0)
        
        self.add(box_main)
        self.show_all()

        return       

def main():
    gtk.main()

if __name__ == "__main__":
    StartFile()

main()
