#taking user input
tweetnum = int(input("Enter the tweet count wanted: "))
tweetstr = str(input("Enter the tweet string: "))    #tweetstr = " #DonaldTrump"
tweetsin = str(input("Enter the  since date: "))
tweetunt = str(input("Enter the  until date: "))
tweetloc = str(input("Enter the  country: "))

if tweetsin == "none":
    tweetsin = ""
else: tweetsin = tweetsin

if tweetunt == "none":
    tweetunt = ""
else: tweetunt = tweetunt

if tweetloc == "none":
    tweetloc = ""
else: tweetloc = tweetloc

tweetsrchitem = tweetstr + " since:" + tweetsin + " until:" + tweetunt

print(tweetsrchitem)

 if tweet.cordinates:
        location = geolocator.reverse(tweet.cordinates)
        tweets_list2[i].append(location.address)