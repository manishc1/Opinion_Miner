import requests
import json
import sys

def getReviews(title):
	#title = sys.argv[1]
	apikey = "89wjdunfw87t689yjdbs4a24"

	req_url_old = "http://imdbapi.org/?title="+ title +"&yg=0"
	movieRequestURL = "http://api.rottentomatoes.com/api/public/v1.0/movies.json?q=" + title + "&apikey=89wjdunfw87t689yjdbs4a24"

	movieRequest = requests.get(movieRequestURL)
	movieResult = json.loads(movieRequest.text.strip())
	#print movieResult	
	try:
		title = movieResult[u"movies"][0][u"title"]
		reviewRequestURL = movieResult[u"movies"][0][u"links"][u"reviews"] + "?apikey=" + apikey + "&page_limit=5"

		reviewRequest = requests.get(reviewRequestURL)
		reviewResult = json.loads(reviewRequest.text.strip())

		rawReviews = reviewResult[u"reviews"]
		textReviews = []

		for rawReview in rawReviews:
			textReviews.append(rawReview[u"quote"])

		#print textReviews
		f = open("data/testTweets.data" , "a")
		for x in range(0 , len(textReviews)):
			f.write("%s\n" % (textReviews[x]))
		f.close()
		#return textReviews
	except:
		f = open("data/testTweets.data" , "a")
		f.close()
		#print ["Error:Not found"]
		#return ["Error:Not found"]

if __name__ == "__main__":
	movie = sys.argv[1]
	getReviews(movie)
