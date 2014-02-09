#! /usr/bin/env python
 
import tweetstream

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

def getStream(query , limit):

    words = query.split(" ")
    stream = tweetstream.FilterStream("twtrmanish", "manishmeetto", track=words)

    length = 0;
    f = open("data/testTweets.data" , "w")
    for tweet in stream:
        if tweet.has_key("lang") and tweet['lang'] == "en":
            if tweet.has_key("text"):
                text = strip_non_ascii(tweet['text'])
                text = text.replace('\n','')
                f.write("%s\n" % (text))
                length = length + 1
        if (length >= limit):
            break

