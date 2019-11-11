# -*- coding: utf-8 -*-

"""Constants for VarGenPath"""

import os
from datetime import datetime


__all__ = [
    'HERE',
    'OUTPUT',
    'IMAGE_PATH',
    'SESSION_PATH',
    'DATA',
    'LINKSET_PATH',
    'VARIANT_LIST_PATH'
]

date = datetime.today().strftime('%d%m%Y_')
HERE = os.path.abspath(os.path.dirname(__file__))
OUTPUT = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'output'))
IMAGE_PATH = os.path.join(OUTPUT, date+'network')
SESSION_PATH = os.path.join(OUTPUT, date+'session')
DATA = os.path.abspath(os.path.join(HERE, os.pardir, os.pardir, 'data'))
LINKSET_PATH = os.path.join(DATA, 'wikipathways-20190610-hsa.xgmml')
VARIANT_LIST_PATH = os.path.join(DATA, 'variant_list.txt')
