#CONFIGURATION

#NOTE: THIS DOES NOT RUN ON A SCHEDULE AUTOMATICALLY. I RECOMMEND SETTING UP A cronjob TO RUN THE MAIN PYTHONS SCRIPT ON A SCHEDULE

#This is for your Twitter App keys
app_key = ""
app_secret = ""
oauth_token = ""
oauth_token_secret = ""

#Images Directory, which should look similar to "/var/RedditTwitterPoster/images/"
img_dir = ""

#This how Reddit sees your script poking in, name it something unique
user_agent = ""

#Enables if the bot actually posts to twitter. Useful for testing with prints instead of spamming your followers
enable_tweets = True

#Sets the number of tweets before a submission may be reposted. Recommended no higher than either a quarter of the total link submissions from the subreddit, or 250 (Whichever is smaller) (Integer)
repeat_threshold = 5

#Choose the subreddit you wish to pull from such as 'python' for reddit.com/r/python
source_subreddit = 'Python'

#Choose the string of hashtags to use (Recommended no longer than 30 characters) (Set to "" if you want blank)
hashtags = "#Python #Programming"

#Sets if the bot should try convert strings enclosed by square brackets into hashtags (True or False)
autohashtag = False

#Sets if the bot will post the Reddit submission title within the tweet (True or False)
post_reddit_title = True

#Sets if the bot will post the Reddit submission permalink within the tweet (True or False)
link_to_reddit = True

#Sets if the bot will post NSFW-tagged submissions (True or False)
post_NSFW = False

#Sets the minimum score a submission must have to be posted (integer)
min_score = 0

#Sets if the bot will post images (Limited to .png and .jpg/.jpeg) (True or False)
post_images = True

#Sets if the bot will post gifs (animated or not) (True or False)
post_gifs = False

#Sets if the bot will post links from Vine (True or False)
post_vine = False

#Sets if the bot will post links from Soundcloud (True or False)
post_soundcloud = False

#Sets if the bot will post links from YouTube (True or False)
post_youtube = True
