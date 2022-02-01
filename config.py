import tweepy
from tweepy import OAuthHandler

consumer_key = 'JhFMnm0cewsnnkYN8FxZ44oUL'
consumer_secret = 'N8bdKlzeUWQCJaUz7WQwo0C3R4mzFGRtMwdj3dl2mUIsuDyZHo'
access_token = 'AAAAAAAAAAAAAAAAAAAAAIgTYwEAAAAAQsyaWecqUGrhrE2TctLyx9mE5ls%3DCvDBo7kKVzsQ79ilyByUOGTLs5l9sUxVdrFJtLzyoqDIZQQTwm'
access_secret = 'N8bdKlzeUWQCJaUz7WQwo0C3R4mzFGRtMwdj3dl2mUIsuDyZHo'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
