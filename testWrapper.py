#! /usr/bin/python

import sys
import getTestTweets
import getTestRTReviews
import yelpCall
import formTestAttributeVector

def main(query , label , limit):
    getTestTweets.getStream(query , limit)
    getTestRTReviews.getReviews(query)
    yelpCall.getReviews(query)
    formTestAttributeVector.getAttribute(label)

if __name__ == "__main__":
    main(sys.argv[1] , eval(sys.argv[2]) , eval(sys.argv[3]))
