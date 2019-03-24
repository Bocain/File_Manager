#!/usr/bin/env python
# -*- coding: cp1250 -*-

import os, stat, time
import pygtk
import gtk
import json

class RightColumnWithRemarks(object):
    
    view = gtk.TextView()
    text = ''
    
    def __init__(self):

        self.notesWindow = gtk.ScrolledWindow()
        with open('Notes.json') as json_file:
            slownik = json.load(json_file)
        bufferNotes = RightColumnWithRemarks.view.get_buffer()
        bufferNotes.set_text(slownik["notatka"])
        startIter = bufferNotes.get_start_iter()
        endIter = bufferNotes.get_end_iter()
        RightColumnWithRemarks.text = bufferNotes.get_text(startIter, endIter)
        self.notesWindow.add(RightColumnWithRemarks.view)
        return
