# importing the module 
import tweepy
import requests

# Set adress here
url = 'https://dvtapi.com/3000/api/DVT/mainnet/address/qr32dwczk2pr5xh9nvuh3yv4rkc93t7yuugq4tmufe/balance' 
response = requests.get(url)
data = response.json()
limit = 2500000000000
if data["balance"] >= limit:
    print(limit, data["balance"])
    print("do something")
    tweet = "Mission sucesfull."
else:
    print(limit, data["balance"])
    with open('day.txt','r+') as f:
            day_number = int(f.read())
            f.seek(0)
            f.write(str(day_number+1))
            f.truncate()
    tweet = (f"Day {day_number} of asking @BitcoinJake09 for sending some #DVT devault:qr32dwczk2pr5xh9nvuh3yv4rkc93t7yuugq4tmufe")

# personal details 
consumer_key =""
consumer_secret =""
access_token =""
access_token_secret =""
  
# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  
# update the status 
api.update_status(status=tweet) 
