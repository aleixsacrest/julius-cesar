import sys

if len(sys.argv) != 3:
    print 'Two parameter is needed'
    exit(0)

f = open(sys.argv[1],'r')
csv = ''

for line in f.read().split('\n'):
    if len(line) > 0:
        word = ''
        count = 0
        i = 0
        while line[i] != '[':
            if line[i] != ' ':
                word += line[i]
            i += 1
        csv += word + ';'
        word = ''
        while line[i] != ' ':
            word += line[i]
            i += 1
        csv += word + ';'
        word = ''
        while line[i] == ' ':
            i += 1
        word = line[i:]
        csv += word + '\n'

f.close()
f = open(sys.argv[2],'w')
f.write(csv)
f.close()
