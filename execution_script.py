#!/usr/bin/python

import os
from WER_computation import *

utt = {'A' : ['dictate one two three final', 'matrix', 'make directory', 'open emacs', 'open terminal', 'raise volume'], 'B' : ['dictate five five five final', 'matrix', 'open file system', 'open newspaper', 'remove directory', 'lower volume']}

def executeJuliusFor(student):
    os.system('ls -1 utterances/' + student + ' > speakers')
    
    f = open('speakers', 'r')
    
    speakers = f.read().split('\n')
    
    f.close()
    os.system('rm speakers')
    
    for s in speakers:
        if len(s) > 0:
            os.system('ls -1 utterances/' + student + '/' + s + ' > files')
            f = open('files', 'r')
            files = f.read().split('\n')
            f.close()
            os.system('rm files')
            i = 0
            for file in files:
                if len(file) > 0:
                    if os.path.exists('references'):
                        append_write = 'a' # append if already exists
                    else:
                        append_write = 'w' # make a new file if not
                    f = open('references', append_write)
                    f.write(utt[student][int(i/2)] + '\n')
                    f.close()
                    i += 1
                    os.system('./julius -input stdin -C Sample.jconf -plugindir plugin < utterances/' + student + '/' + s + '/' + file)

def computeWER():
    print '\n\nref | hyp\n\n'
    f = open('hypothesis', 'r')
    vhyp = f.read().split('\n')
    f.close()
    f = open('references', 'r')
    vref = f.read().split('\n')
    f.close()

    wersum = 0
    wcount = 0
    for i in range(len(vref)):
        if len(vref[i]) > 0:
            wcount += len(vref[i].split(' '))
            hyp_parsed = vhyp[i].replace('<s> ', '').replace(' </s>', '')
            print vref[i], '|', hyp_parsed
            wersum += wer(vref[i].split(), hyp_parsed.split())

    return wersum, wcount

f = open('results-julius_config', 'w')
f.write('evaluation-mode\nno_dialog-manager')
f.close()

os.system('rm hypothesis')
os.system('rm references')

executeJuliusFor('A')
executeJuliusFor('B')

wersum,wcount = computeWER()

WER = float(wersum) / float(wcount) * 100.0
A = 100.0 - WER

print '\n\nwer-sum:', wersum, 'wcount:', wcount, 'Acc:', A, '%'


os.system('echo \'\' > results-julius_config')
os.system('rm hypothesis')
os.system('rm references')


