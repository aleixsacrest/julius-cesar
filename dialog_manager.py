import sys
import os

num = {'one': 1, 'two':2, 'three':3,'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12}

for i in range(1,len(sys.argv)):
    print sys.argv[i]
    if 'open' in sys.argv[i]:
        if 'newspaper' in sys.argv[i]:
            os.system('google-chrome http://www.ara.cat/ &')
        elif 'emacs' in sys.argv[i]:
            os.system('emacs &')
        elif 'terminal'in sys.argv[i]:
            os.system('gnome-terminal')
        elif 'file system' in sys.argv[i]:
            os.system('nautilus')
    elif 'directory' in sys.argv[i]:
        if 'make' in sys.argv[i]:
            os.system('mkdir ~/newdir')
        elif 'remove' in sys.argv[i]:
            os.system('rm -r ~/newdir')
    elif 'top' in sys.argv[i]:
        os.system('gnome-terminal -e top')
    elif 'matrix' in sys.argv[i]:
        os.system('gnome-terminal -e cmatrix')
    elif 'factor' in sys.argv[i]:
        os.system('factor ' + str(num[sys.argv[i].split('factor ')[i].split(' ')[0]]))
    elif 'volume' in sys.argv[i]:
        c = 'amixer -D pulse sset Master 5%'
        if 'raise' in sys.argv[i]:
            c += '+'
        elif 'lower' in sys.argv[i]:
            c += '-'
        os.system(c)
    elif 'dictate' in sys.argv[i]:
        text = sys.argv[1].split('dictate ')[1].split(' final')[0]
        os.system('echo ' + text + ' > dictat.txt')
        print 'Text saved in dictat.txt'
