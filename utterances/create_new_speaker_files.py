#!/usr/bin/python

import sys
import os

def usage():
    print 'USAGE: python create_new_speaker_files.py [A|B] speakerName'

if len(sys.argv) != 3 or (sys.argv[1] != 'A' and sys.argv[1] != 'B'):
    usage()
    exit(0)

student = sys.argv[1]
name = sys.argv[2]

os.system('mkdir ' + student + '/' + name)

f = open('names' + student, 'r')

filenames = f.read()

f.close()

for fn in filenames.split('\n'):
    if len(fn) > 0:
        os.system('touch ' + student + '/' + name + '/' + name + fn)
