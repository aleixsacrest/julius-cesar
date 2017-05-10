import sys


if len(sys.argv) != 2:
    print 'One parameter is needed'
    exit(0)

f = open(sys.argv[1],'r')
text_out = ''

for line in f.read().split('.'):
    for char in line:
        if char.isalpha() or char == ' ':
            text_out += char.lower()
    text_out += '\n'

f.close()

f = open(sys.argv[1]+'.out','w')
f.write(text_out)
