# analyze.py

import os, sys, errno
import itertools
import datetime

sys.path.append("modules")

# Modules to fetch and post data
import alldata
import log

# Modules to analyze data
import dips

def analyze():
  dips.mark()

analyze()