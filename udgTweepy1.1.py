from discordwebhook import Discord
import tweepy
import keys


client = tweepy.Client(keys.BEARER_TOKEN, keys.API_KEY, keys.API_KEY_SECRET, keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
auth = tweepy.OAuth1UserHandler(keys.API_KEY,keys.API_KEY_SECRET, keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

print(api.get_user("underdog_nba"))
