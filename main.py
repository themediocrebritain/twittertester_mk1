import twitter

api = twitter.Api(consumer_key = [consumer_key],
	consumer_secret = '',
	access_token_key = '',
	access_token_secret = '')

user = "pizzahut"

statuses = api.GetUserTimeline(screen_name = user)
print([s.text for s in statuses])
