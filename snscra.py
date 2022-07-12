#raviteja addaguduru
#importing pandas,os,and snscrape api 
import snscrape.modules.twitter as sntwitter
import pandas as pd
import os
# import module
from geopy.geocoders import Nominatim
# initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# Creating list to append tweet data to
tweets_list2 = []

#taking user input
tweetnum = int(input("Enter the tweet count wanted: "))
tweetstr = str(input("Enter the tweet string: "))    #tweetstr = " #DonaldTrump"
tweetsin = str(input("Enter the  since date: "))
tweetunt = str(input("Enter the  until date: "))
#uses city name to filter tweets and radius
tweetloc = str(input("Enter the  city name: "))
tweetrad = int(input("Enter the  radius: "))

if tweetsin == "none":
    tweetsin = ""
else: 
    tweetsin = " since:" + tweetsin

if tweetunt == "none":
    tweetunt = ""
else: 
    tweetunt = " until:" + tweetunt

if tweetloc == "none":
    tweetloc = ""
    tweetrad = str(tweetrad)
    tweetrad = ""
else: 
    tweetloc = "near:"+ tweetloc +" "
    tweetrad = str(tweetrad)
    tweetrad = "within:" + tweetrad  + "km "




tweetsrchitem = tweetstr + tweetsin + tweetunt + " " + tweetloc + tweetrad
print(tweetsrchitem)
# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper("'"+tweetsrchitem+"'" ).get_items()):
    if i>tweetnum:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime','Tweet Id', 'Text', 'Username'])
tweets_df2.to_csv(os.getcwd() + r'/twitterscrape/output.csv', sep=',', encoding='utf-8', header=True, index=False)