#! /usr/bin/env python

import re 
import string
 
#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end
 
#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')
 
    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end
 
#start getfeatureVector
def getFeatureVector(tweet , stopWords):
    featureVector = []
    #split tweet into words
    #words = tweet.split()
    words = [item for item in map(string.strip, re.split("(\W+)", tweet)) if len(item) > 0]
    for word in words:
        ws = word.split()
        for w in ws:
            # replace two or more with two occurrences
            w = replaceTwoOrMore(w)
            # strip punctuation
            w = w.strip('\'"?,.')
            #w = w.strip(' ,.')
            # check if the word stats with an alphabet
            val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            # ignore if it is a stop word
            # if(w in stopWords or val is None):
            if(w in stopWords):
                continue
            else:
                featureVector.append(w.lower())
    return featureVector
#end
 
#start process_tweet
def processTweet(tweet):
    # process the tweets
 
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

# start form Attribute Vector
def formAttributeVector(v , f , bowVector , bowlen , label):
    vlen = len(v)
    s = ""
    s += '%d' % (label)
    for x in range (1 , bowlen+1):
        if bowVector[x-1] in v:
            s += ' %d:1' % (x)
        else:
            s += ' %d:0' % (x)
    f.write(s + '\n')
# end

def getAttribute(label):
    # Read the tweets one by one and process it
    fp = open('data/testTweets.data', 'r')
    line = fp.readline()
 
    #st = open('data/stopWords.data', 'r')
    stopWords = getStopWordList('data/stopWords.data')
    #st.close()

    bow = open('data/bagOfWords.data' , 'r')
    bowVector = bow.readlines()[0].split(",")
    bowlen = len(bowVector)
    bow.close()

    f = open('data/testAttributeVector.data' , 'w') 
    while line:
        processedTweet = processTweet(line)
        featureVector = getFeatureVector(processedTweet , stopWords)
        if len(featureVector) > 0:
            formAttributeVector(featureVector , f , bowVector , bowlen , label)
        line = fp.readline()
    # end loop

    fp.close()
    f.close()
