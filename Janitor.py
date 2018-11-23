#!/usr/bin/env python
# -*- coding: cp1250 -*-

import os

for f in os.listdir(os.getcwd()):
    if f.endswith(".pyc"):
        os.remove(f)
