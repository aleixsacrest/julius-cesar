import sys
import os

f = open('results-julius_config', 'r')
config = f.read().split('\n')
f.close()

if 'evaluation-mode' in config:
    if os.path.exists('hypothesis'):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not
    f = open('hypothesis', append_write)
    f.write(sys.argv[1] + '\n')

num = {'one': 1, 'two':2, 'three':3,'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12}

if not 'no_dialog-manager' in config:
    print sys.argv[1]
    if 'open' in sys.argv[1]:
        if 'newspaper' in sys.argv[1]:
            os.system('google-chrome http://www.ara.cat/ &')
        elif 'emacs' in sys.argv[1]:
            os.system('emacs &')
        elif 'terminal'in sys.argv[1]:
            os.system('gnome-terminal')
        elif 'file system' in sys.argv[1]:
            os.system('nautilus')
    elif 'directory' in sys.argv[1]:
        if 'make' in sys.argv[1]:
            os.system('mkdir ~/newdir')
        elif 'remove' in sys.argv[1]:
            os.system('rm -r ~/newdir')
    elif 'top' in sys.argv[1]:
        os.system('gnome-terminal -e top')
    elif 'matrix' in sys.argv[1]:
        os.system('gnome-terminal -e cmatrix')
    elif 'factor' in sys.argv[1]:
        os.system('factor ' + str(num[sys.argv[1].split('factor ')[1].split(' ')[0]]))
    elif 'volume' in sys.argv[1]:
        s = ''
        if 'raise' in sys.argv[1]:
            s += '+'
        elif 'lower' in sys.argv[1]:
            s += '-'
        if s != '':
            c = 'amixer -D pulse sset Master 5%' + s
            os.system(c)
    elif 'dictate' in sys.argv[1]:
        text = sys.argv[1].split('dictate ')[1].split(' final')[0]
        os.system('echo ' + text + ' > dictat.txt')
        print 'Text saved in dictat.txt'
