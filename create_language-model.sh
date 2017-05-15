#!/bin/bash

# python text_parser.py -input inputfile [-dictCSV dictfile | -dict dictfile]
# If dictCSV is specified dict has to be in CSV format
python language_models/text_parser.py -input language_models/input/$1 -dictCSV language_models/dict.csv

ngram-count -text language_models/input/$1.out -order 2 -lm language_models/corpus.lm -addsmooth0 -interpolate1

language_models/mkbingram -nlr language_models/corpus.lm language_models/corpus.bin
