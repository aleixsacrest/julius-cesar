import os

os.system('ls -1 data > datainputtexts')

f = open('datainputtexts', 'r')
fo = open('input_language-model_text.txt', 'rw')

for file in f.read().split('\n'):
    if len(file) > 0:
        text = open(file, 'r').read()
        fo.write(text + '\n')

        
