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

##        view = gtk.TextView()

        self.okno = gtk.ScrolledWindow()

        with open('Notes.json') as json_file:
            slownik = json.load(json_file)

        buffer0 = RightColumnWithRemarks.view.get_buffer()
        
        buffer0.set_text(slownik["notatka"])

        startiter = buffer0.get_start_iter()
        enditer = buffer0.get_end_iter()
##        self.buffer0.delete(startiter, enditer)
        RightColumnWithRemarks.text = buffer0.get_text(startiter, enditer)

        self.okno.add(RightColumnWithRemarks.view)

        return
