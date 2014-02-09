import yelpSearch
#import yelpBusiness
import json
import sys

def getReviews(title):
	consumer_key="VS9QWAQEPuQyAvOG82--BQ" 
	consumer_secret="9a7C6CSpTtrHG6-hElLCjjB54qc" 
	token="2Dp1dZXtKAUmjEltpDoSmgn0LmT_rpkA" 
	token_secret="y-jZ81OxhPp7-GpQ_BDVof2U0Z0"
	host = 'api.yelp.com'
	path = '/v2/search'
	path2 = '/v2/business'

	try:
		title = title.replace(" ","+")
		resp = yelpSearch.searchRequest(host, path, consumer_key, consumer_secret, token, token_secret,title)
		bid = resp["businesses"][0]["id"]
		review = resp["businesses"][0]["snippet_text"]
		#print review
		#return review
		f = open("data/testTweets.data" , "a")
		f.write("%s\n" % (review))
		f.close
	except:
		f = open("data/testTweets.data" , "a")
		f.write("%s\n" % (review))
		f.close
		#print ["Error:Not found"]
		#return ["Error:Not found"]

#bresp = yelpBusiness.bRequest(host, path2, consumer_key, consumer_secret, token, token_secret, bid)
#print json.dumps(bresp, sort_keys=True, indent=2)

if __name__ == "__main__":
	getReview(sys.argv[1])

