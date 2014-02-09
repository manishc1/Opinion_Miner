#! /usr/bin/env python
 
import tweetstream

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def getStream(limit):
    limit = limit / 2
    words = [":)",":-)",":D",":-D",":(",":-(",":@",":'("]
    stream = tweetstream.FilterStream("twtrmanish", "manishmeetto",track=words)

    plength = 0;
    nlength = 0
    f = open("data/trainTweets.data" , "w")
    for tweet in stream:
        if tweet.has_key("lang") and tweet['lang'] == "en":
            if tweet.has_key("text"):
                text = strip_non_ascii(tweet['text'])
                text = text.replace('\n','')
                if (":)" in text) or (":-)" in text) or (":D" in text) or (":-D" in text):
                    if (plength < limit):
                        f.write("%s positive\n" % (text))
                        plength = plength + 1
                if (":(" in text) or (":-(" in text) or (":@" in text) or (":'(" in text):
                    if (nlength < limit):
                        f.write("%s negative\n" % (text))
                        nlength = nlength + 1
        if (plength >= limit) and (nlength >= limit):
            break
