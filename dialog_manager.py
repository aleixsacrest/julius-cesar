import sys
import os

for i in range(1,len(sys.argv)):
    print sys.argv[i]
    if 'open page' in sys.argv[i]:
        os.system('firefox http://fib.upc.edu &')
    elif 'open emacs' in sys.argv[i]:
        os.system('emacs &')
    elif 'top' in sys.argv[i]:
        os.system('top')
    elif 'dictat' in sys.argv[i]:
        text = sys.argv[1].split('dictat ')[1].split(' final')[0]
        os.system('echo ' + text + ' > dictat.txt')
