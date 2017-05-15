import os

os.system('ls -1 data > datainputtexts')

f = open('datainputtexts', 'r')
fo = open('input/input_lm', 'w')

for file in f.read().split('\n'):
    if len(file) > 0:
        text = open('data/' + file, 'r').read()
        fo.write(text + '\n')

f.close()
fo.close()

os.system('rm datainputtexts')
