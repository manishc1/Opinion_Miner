#! /usr/bin/env python

def formBagOfWords():
    # Read the feature vectors one by one and add to bag of words
    bow = []
    fp = open('data/featureVector.data', 'r')
    line = fp.readline()
 
    while line:
        line = line.strip()
        bow = bow + line.split(',')
        line = fp.readline()
    # end loop

    fp.close()
    bow = list(set(bow))
    # print len(bow)

    fp = open('data/bagOfWords.data','w')
    fp.write(','.join(bow))
    fp.close()
