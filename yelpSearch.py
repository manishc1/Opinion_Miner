import json
import oauth2
import optparse
import urllib
import urllib2

def searchRequest(host, path, consumer_key, consumer_secret, token, token_secret,searchTerm):
  """Returns response for API request."""
  #host = 'api.yelp.com'
  #path = '/v2/search'
  url = 'http://%s%s?' % (host, path)
  url = url + 'term='+ searchTerm +'&location=united+states&limit=1'
  #print 'URL: %s' % (url)

  # Sign the URL
  consumer = oauth2.Consumer(consumer_key, consumer_secret)
  oauth_request = oauth2.Request('GET', url, {})
  oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                        'oauth_timestamp': oauth2.generate_timestamp(),
                        'oauth_token': token,
                        'oauth_consumer_key': consumer_key})

  token = oauth2.Token(token, token_secret)
  oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
  signed_url = oauth_request.to_url()
  #print 'Signed URL: %s\n' % (signed_url,)

  # Connect
  try:
    conn = urllib2.urlopen(signed_url, None)
    try:
      response = json.loads(conn.read())
    finally:
      conn.close()
  except urllib2.HTTPError, error:
    response = json.loads(error.read())

  return response


