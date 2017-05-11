import sys
import os

def usage():
    print 'Usage: python text_parser.py -input inputfile [-dictCSV dictfile | -dict dictfile]\nIf dictCSV is specified dict has to be in CSV format'
    exit(0)

if len(sys.argv) < 2:
    usage()

i = 1
inputfile = ''
dictfile = ''
while i < len(sys.argv):
    if sys.argv[i] == '-input':
        inputfile = sys.argv[i+1]
    elif sys.argv[i] == '-dict':
        dictfile = sys.argv[i+1] + '.csv'
        os.system('python dict_parser.py ' + sys.argv[i+1] + ' ' + dictfile)
    elif sys.argv[i] == '-dictCSV':
        dictfile = sys.argv[i+1]
    else:
        usage()
    i += 2

if inputfile == '' or dictfile == '':
    usage()

fdict = open(dictfile, 'r')
dict_model = {}

for line in fdict.read().split('\n'):
    if len(line) > 0:
        vals = line.split(';')
        dict_model[vals[0].lower()] = vals[2]
fdict.close()

dict = {}

finp = open(inputfile, 'r')
text_preproces = ''

for l in finp.read().split('\n'):
    for line in l.split('.'):
        if len(line) > 0:
            for char in line:
                if char.isalpha() or char == ' ':
                    text_preproces += char.lower()
            text_preproces += '\n'

finp.close()

text_out = ''

for line in text_preproces.split('\n'):
    if len(line) > 0:
        for word in line.split(' '):
            if word in dict_model.keys():
                dict[word] = dict_model[word]
                text_out += word + ' '
        text_out = text_out[:-1] + '\n'


f = open(inputfile + '.out','w')
f.write(text_out)
f.close()

f = open(inputfile + '.dict', 'w')
for k in dict.keys():
    f.write(k + '\t\t' + dict[k] + '\n')
f.write('<s>\t\tsil\n</s>\t\tsil')
f.close()
