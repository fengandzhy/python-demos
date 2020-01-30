'''
Created on 2020年1月30日

@author: Ellite Service
'''

import os
import sys
os.system('cls')
f_handler = open('out.log','w')
oldstdout = sys.stdout
sys.stdout = f_handler
os.system('cls')
sys.stdout = oldstdout