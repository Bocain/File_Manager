#!/usr/bin/env python
# -*- coding: cp1250 -*-

import os

for files in os.listdir(os.getcwd()):
    if files.endswith(".pyc"):
        os.remove(files)
