from dis import disco
import keys
import tweepy
import players
import time
from discordwebhook import Discord

client = tweepy.Client(keys.BEARER_TOKEN, keys.API_KEY, keys.API_KEY_SECRET, keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
auth = tweepy.OAuth1UserHandler(keys.API_KEY,keys.API_KEY_SECRET, keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

previous_status = {}
#goal with this is to store the name as a key and the status from the previous tweet as the pair
#Maybe only if out, questionable, upgrade, downgrade, no retweets or replies too



####

# Loop over all three lists and give a different alert for the all_stars than the other ones

####
class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        set = 0
        for player in players.all_stars:
            if player.upper() in tweet.text.upper():
                res = "\N{Police Cars Revolving Light}" + "\N{Police Cars Revolving Light}" + tweet.text + "\N{Police Cars Revolving Light}" + "\N{Police Cars Revolving Light}"
                #start of where I post it to discord
                discord = Discord(url="https://discordapp.com/api/webhooks/1003384743359950988/3BzT7fzJMOniP9bHx05DlUSOgl2rNABsTVmP8Jws0eadag4OluQNuySCbOcilwi8AUdb")
                discord.post(content=res)
                #end of discord
                set = 1
                break
        
        if set == 0:
            for player in players.rest:
                if player.upper() in tweet.text.upper():
                    # print(tweet.text)
                    #start of where I post it to discord
                    discord = Discord(url="https://discordapp.com/api/webhooks/1003384743359950988/3BzT7fzJMOniP9bHx05DlUSOgl2rNABsTVmP8Jws0eadag4OluQNuySCbOcilwi8AUdb")
                    discord.post(content=tweet.text)
                    #end of discord
                    break


stream = MyStream(bearer_token=keys.BEARER_TOKEN)




stream.filter()


