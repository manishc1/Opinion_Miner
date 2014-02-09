#! /usr/bin/python

import sys
import getTrainTweets
import filterTrainTweets
import formBagOfWords
import formTrainAttributeVector

def main(limit):
    getTrainTweets.getStream(limit)
    filterTrainTweets.filterTweets()
    formBagOfWords.formBagOfWords()
    formTrainAttributeVector.getAttribute()

if __name__ == "__main__":
    main(eval(sys.argv[1]))
