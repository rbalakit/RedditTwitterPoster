#CONFIGURATION

#NOTE: THIS DOES NOT RUN ON A SCHEDULE AUTOMATICALLY. I RECOMMEND SETTING UP A cronjob TO RUN THE MAIN PYTHONS SCRIPT ON A SCHEDULE

#This is for your Twitter App keys
app_key = ""
app_secret = ""
oauth_token = ""
oauth_token_secret = ""

#This how Reddit sees your script poking in, name it something unique
user_agent = ""

#Images Directory, which should look similar to "/var/RedditTwitterPoster/images/"
img_dir = ""

#Choose the subreddit you wish to pull from such as 'python' for reddit.com/r/python
source_subreddit = 'Python'

#Choose the string of hashtags to use (Recommended no longer than 30 characters) (Set to "" if you want blank)
hashtags = "#Python #Programming"

#Sets if the bot should try convert strings enclosed by square brackets into hashtags ("enabled" or "disabled")
autohashtag = "disabled"

#Sets if the bot will post the Reddit submission title within the tweet ("enabled" or "disabled")
post_reddit_title = "enabled"

#Sets if the bot will post the Reddit submission permalink within the tweet ("enabled" or "disabled")
link_to_reddit = "enabled"

#Sets if the bot will post NSFW-tagged submissions ("enabled" or "disabled")
post_NSFW = "disabled"

#Sets the minimum score a submission must have to be posted (integer)
min_score = 0

#Sets if the bot will post images (Limited to .png and .jpg/.jpeg) ("enabled" or "disabled")
post_images = "enabled"

#Sets if the bot will post gifs (animated or not) ("enabled" or "disabled")
post_gifs = "disabled"

#Sets if the bot will post links from Vine ("enabled" or "disabled")
post_vine = "disabled"

#Sets if the bot will post links from Soundcloud ("enabled" or "disabled")
post_soundcloud = "disabled"

#Sets if the bot will post links from YouTube ("enabled" or "disabled")
post_youtube = "enabled"
