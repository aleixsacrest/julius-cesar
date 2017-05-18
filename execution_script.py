#!/usr/bin/python

import os
from WER_computation import *

utt = {'A' : ['dictate one two three final', 'make directory', 'open emacs', 'open terminal', 'top', 'raise volume'], 'B' : ['dictate five five five final', 'matrix', 'open file system', 'open newspaper', 'remove directory', 'lower volume']}

stats_utt = {'open file system': {'wcount': 0, 'wersum': 0}, 'dictate five five five final': {'wcount': 0, 'wersum': 0}, 'matrix': {'wcount': 0, 'wersum': 0}, 'make directory': {'wcount': 0, 'wersum': 0}, 'top': {'wcount': 0, 'wersum': 0}, 'dictate one two three final': {'wcount': 0, 'wersum': 0}, 'open terminal': {'wcount': 0, 'wersum': 0}, 'open emacs': {'wcount': 0, 'wersum': 0}, 'open newspaper': {'wcount': 0, 'wersum': 0}, 'remove directory': {'wcount': 0, 'wersum': 0}, 'raise volume': {'wcount': 0, 'wersum': 0}, 'lower volume': {'wcount': 0, 'wersum': 0}}

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
            os.system('echo \'ref | hyp\\n\' > utterances/performance/' + s + '.res')
            i = 0
            for file in files:
                if len(file) > 0:
                    if os.path.exists('references'):
                        append_write = 'a' # append if already exists
                    else:
                        append_write = 'w' # make a new file if not
                    f = open('references', append_write)
                    f.write(utt[student][int(i/2)] + '||' + s + '\n')
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

    speakers_WER = {}

    wersum = 0
    wcount = 0
    for i in range(len(vref)):
        if len(vref[i]) > 0:
            command = vref[i].split('||')[0]
            s = vref[i].split('||')[1]
            if not s in speakers_WER.keys():
                speakers_WER[s] = {'wcount':0,'wersum':0}
            
            speakers_WER[s]['wcount'] += len(command.split(' '))
            wcount += len(command.split(' '))
            stats_utt[command]['wcount'] += len(command.split(' '))
            
            hyp_parsed = vhyp[i].replace('<s> ', '').replace(' </s>', '')
            print hyp_parsed, '|', vref[i]
            
            f = open('utterances/performance/' + s + '.res', 'a')
            f.write(command + ' | ' + hyp_parsed + '\n')
            f.close()
            
            f = open('utterances/performance/tot.res', 'a')
            f.write(command + ' | ' + hyp_parsed + ' || ' + s + '\n')
            f.close()

            ws = wer(command.split(), hyp_parsed.split())
            wersum += ws
            speakers_WER[s]['wersum'] += ws
            stats_utt[command]['wersum'] += ws

    for k in speakers_WER.keys():
        f = open('utterances/performance/' + k + '.res', 'a')
        _WER = float(speakers_WER[k]['wersum']) / float(speakers_WER[k]['wcount']) * 100.0
        _A = 100.0 - _WER

        f.write('\n\nwer-sum: ' + str(speakers_WER[k]['wersum']) + ' wcount: ' + str(speakers_WER[k]['wcount']) + ' Acc: ' + str(_A) + '%')
        f.close()

    f = open('utterances/performance/tot_command.res', 'a')
    for k in stats_utt.keys():
        f.write(k + ';' + str(100.0 - 100.0 * (float(stats_utt[k]['wersum']) / float(stats_utt[k]['wcount']))) + '\n')
    f.close()

    return wersum, wcount

f = open('results-julius_config', 'w')
f.write('evaluation-mode\nno_dialog-manager')
f.close()

os.system('rm hypothesis')
os.system('rm references')
os.system('rm -r utterances/performance')
os.system('mkdir utterances/performance')
os.system('echo \'ref | hyp\\n\' > utterances/performance/tot.res')
os.system('echo \'command;accuracy\\n\' > utterances/performance/tot_command.res')

executeJuliusFor('A')
executeJuliusFor('B')

wersum,wcount = computeWER()

WER = float(wersum) / float(wcount) * 100.0
A = 100.0 - WER

print '\n\nwer-sum:', wersum, 'wcount:', wcount, 'Acc:', A, '%'

f = open('utterances/performance/tot.res', 'a')
f.write('\n\nwer-sum: ' + str(wersum) + ' wcount: ' + str(wcount) + ' Acc: ' + str(A) + '%')
f.close()


os.system('echo \'\' > results-julius_config')
os.system('rm hypothesis')
os.system('rm references')


