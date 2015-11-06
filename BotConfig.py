#CONFIGURATION
#This is for your Twitter App keys
app_key = ""
app_secret = ""
oauth_token = ""
oauth_token_secret = ""

#Images Directory, which should look similar to "/var/RedditTwitterPoster/images/"
img_dir = "/var/NicoBot/KongouImages/"

#This how Reddit sees your script poking in, name it something unique
user_agent = "NicoNicoNi_Twitter 0.0.0.1 by /u/Mushrooshi"

#Enables if the bot actually posts to twitter. Useful for testing with prints instead of spamming your followers
enable_tweets = True

#Sets the number of tweets before a submission may be reposted. Recommended no higher than either a quarter of the total link submissions from the subreddit, or 250 (Whichever is smaller) (Integer)
repeat_threshold = 50

#Choose the subreddit you wish to pull from such as 'python' for reddit.com/r/python
source_subreddit = 'OneTrueKongou'

#Choose the string of hashtags to use (Recommended no longer than 30 characters) (Set to "" if you want blank)
hashtags = "#Kongou #Kancolle"

#Sets if the bot should try convert strings enclosed by square brackets into hashtags (True or False)
autohashtag = False

#Sets if the bot will post the Reddit submission title within the tweet (True or False)
post_reddit_title = True

#Sets if the bot will post the Reddit submission permalink within the tweet (True or False)
link_to_reddit = True

#Sets if the bot will post NSFW-tagged submissions (True or False)
post_NSFW = True

#Sets the minimum score a submission must have to be posted (integer)
min_score = 0

#Sets if the bot will post images (Limited to .png and .jpg/.jpeg) (True or False)
post_images = True

#Sets if the bot will post gifs (animated or not) (True or False)
post_gifs = True

#Sets if the bot will post links from Vine (True or False)
post_vine = True

#Sets if the bot will post links from Soundcloud (True or False)
post_soundcloud = True

#Sets if the bot will post links from YouTube (True or False)
post_youtube = True
