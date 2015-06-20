import json
import ssl
import re
import praw
import pprint
import urllib
import os.path
from twython import Twython
from mimetypes import guess_extension
from BotConfig import *

'''
IN ORDER TO RUN PROPERLY, THE CONFIGURATION FILE "BotConfig.py" IS NECESSARY
'''

twitter = Twython(app_key,app_secret,oauth_token,oauth_token_secret)
r = praw.Reddit(user_agent=user_agent)
diditpost = 0
while (diditpost == 0):
	submission = r.get_random_submission(source_subreddit)
	if (not submission.over_18) or (post_NSFW == "enabled"):
		if not submission.is_self:
			if submission.score > min_score:
			
				if link_to_reddit == "enabled":
					titlelength = 135-(53+len(hashtags))
					subpermalink = submission.permalink
				else:
					titlelength = 135-(23+len(hashtags))
					subpermalink = ""
				if autohashtag == "enabled":
					hashtitle = re.sub(r'(\[)', r'\1#', submission.title)
					shorttitle = hashtitle[:titlelength] + (hashtitle[titlelength:] and '...')
				else:
					shorttitle = submission.title[:titlelength] + (submission.title[titlelength:] and '...')
				
				if post_reddit_title == "disabled":
					shorttitle = ""
					
				tweeturl = submission.url
				if "imgur" in submission.url: 
					if not ("i.imgur" in submission.url): 
						iurl = re.sub(r'(\http://)', r'\1i.', submission.url)
						iexurl = iurl+ ".png";
					else:
						iexurl = submission.url
						iurl = iexurl[:-4]
					source = urllib.urlopen(iexurl)
					extension = guess_extension(source.info()['Content-Type'])
					if extension == ".jpe":
						tweeturl = iurl+".jpg";
					elif extension == ".png":
						tweeturl = iurl+".png";
					elif extension == ".gif":
						tweeturl = iurl+".gif";
					
					
				if (tweeturl[-4:] == ".jpg" or tweeturl[-5:] == "jpeg" or tweeturl[-4:] == ".png") and (post_images == "enabled"):
					if not os.path.exists(img_dir+submission.id+"_"+tweeturl.split('/')[-1]):
						urllib.urlretrieve(tweeturl, img_dir+submission.id+"_"+tweeturl.split('/')[-1])
					print submission.title, submission.url, submission.id
					print "Twitter Pic Post:\n\t" + (shorttitle +" "+ hashtags+" "+ subpermalink)
					photo = open(img_dir+submission.id+"_"+tweeturl.split('/')[-1], 'rb')
					twitter.update_status_with_media(status= (shorttitle +" "+ hashtags +" "+ subpermalink), media=photo)
					diditpost = 1
								
				elif (tweeturl[-4:] == ".gif") and (post_gifs == "enabled"):
					if not os.path.exists(img_dir+submission.id+"_"+tweeturl.split('/')[-1]):
						urllib.urlretrieve(tweeturl, img_dir+submission.id+"_"+tweeturl.split('/')[-1])
					print submission.title, submission.url, submission.id
					print "Twitter Pic Post:\n\t" + (shorttitle +" "+ hashtags+" "+ subpermalink)
					photo = open(img_dir+submission.id+"_"+tweeturl.split('/')[-1], 'rb')
					twitter.update_status_with_media(status= (shorttitle +" "+ hashtags +" "+ subpermalink), media=photo)
					diditpost = 1
				else:
					print submission.title, submission.url, submission.id
					print "link post "+submission.title+" is not jpg, png, or gif"
					if (("youtube." in submission.url) or ("youtu.be" in submission.url)) and (post_youtube == "enabled"):
						print "Twitter YouTube Post:\n\t" + (shorttitle +" "+ hashtags+" "+ subpermalink+" "+ tweeturl)
						twitter.update_status(status=(shorttitle +" "+ hashtags+" "+ subpermalink+" "+ tweeturl))
						diditpost = 1
					elif(("vine.co" in submission.url)) and (post_vine == "enabled"):
						print "Twitter Vine Post:\n\t" + (shorttitle +" "+ hashtags+" "+ subpermalink+" "+ tweeturl)
						twitter.update_status(status=(shorttitle +" "+ hashtags+" "+ subpermalink+" "+ tweeturl))
						diditpost = 1
					elif(("soundcloud" in submission.url) or ("snd.sc" in submission.url)) and (post_soundcloud == "enabled"):
						print "Twitter Soundcloud Post:\n\t" + (shorttitle +" "+ hashtags+" "+ subpermalink+" "+ tweeturl)
						twitter.update_status(status=(shorttitle +" "+ hashtags+" "+ subpermalink+" "+ tweeturl))
						diditpost = 1
					else:
						print "[!]There is no Twitter post for this submission try, it will reroll![!]"