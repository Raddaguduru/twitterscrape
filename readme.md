# the script has to have the neccesary downloads of snsscrape and pandas
# There are two ways to get a location from Twitter; a geo-tag from a specific tweet, or a user’s location as part of their profile. 
# According to Twitter, only 1–2% of tweets are geo-tagged hence it isn’t a great metric to be using; on the other hand a significant amount of users have a location in their profile, but they can enter whatever they want. Some are nice to people like us and will write ‘London, England’ or similar, while others are less useful, putting things like ‘My Parents Basement’.
# So the script includes the ability to filter by location with use of cities and km radius but not the same kind of country wide simple geolocation
# The script also takes a while to proccess and input every request so although the possibility of including infinite number of tweets is there , it make take a while to process it all
# when inputting the dates or location strings or any strings either input a valid string or input "none" which will trigger another output