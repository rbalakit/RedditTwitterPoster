import json
import ssl
import re
import praw
import pprint
import urllib
import os.path
from twython import Twython
from mimetypes import guess_extension
import urllib3


# IN ORDER TO RUN PROPERLY, THE CONFIGURATION FILE "BotConfig.py" IS NECESSARY
# The following are default values if your configuration file is not up-to-date and missing some settings. They are overwritten by the values in the configuration file.
# This is contained in an 'if' branch so I can hide it. Is there a proper
# encloser I can put it in that an IDE/texteditor could hide it?
if True:
    img_dir = "/var/TwitterRedditPoster/images/"
    user_agent = "Unconfigured TwitterRedditPoster Script"
    enable_tweets = True
    repeat_threshold = 20
    source_subreddit = 'all'
    hashtags = "#Invalid #Config #File"
    autohashtag = False
    post_reddit_title = True
    link_to_reddit = True
    post_NSFW = False
    min_score = 0
    post_images = True
    post_gifs = False
    post_vine = False
    post_soundcloud = False
    post_youtube = True

from BotConfig import *


def processUrl(suburl):
    twturl = suburl
    if "imgur" in suburl:
        # if "m.imgur" in submission.url:
          #    submission.url.replace("m.imgur","i.imgur")
        if not ("i.imgur" in suburl):
            iurl = re.sub(r'(\http://)', r'\1i.', suburl)
            iexurl = iurl + ".png"
        else:
            iexurl = suburl
            iurl = iexurl[:-4]
        source = urllib.urlopen(iexurl)
        extension = guess_extension(source.info()['Content-Type'])
        if extension == ".jpe":
            twturl = iurl + ".jpg"
        elif extension == ".png":
            twturl = iurl + ".png"
        elif extension == ".gif":
            twturl = iurl + ".gif"
    return twturl


def postLink(srttitle, htags, subpl, twurl):
    if enable_tweets == True:
        twitter.update_status(
            status=(srttitle + " " + htags + " " + subpl + " " + twurl))
        print "Tweet was posted"
    else:
        print "Tweet was pretend-posted"
    return 1


def postImage(srttitle, htags, subpl, twurl, subid):
    if enable_tweets == True:
        photo = open(img_dir + subid + "_" + twurl.split('/')[-1], 'rb')
        twitter.update_status_with_media(
            status=(srttitle + " " + htags + " " + subpl), media=photo)
        print "Tweet was posted"
    else:
        print "Tweet was pretend-posted"
    return 1

# This part opens and loads the previous submissions so it doesn't repeat posts
file = open(img_dir + "submissions_log.txt", "a+")
prevlogs = file.read()
file.close()

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
r = praw.Reddit(user_agent=user_agent)
posted = 0
while (posted == 0):
    uniquepost = 0
    # for submission in r.get_subreddit('niconiconi').get_new(limit=1000):
    while (uniquepost == 0):
        print "\nfetching a new post..."
        submission = r.get_random_submission(source_subreddit)
        print submission.title, submission.url, submission.id
        if submission.id in prevlogs:
            uniquepost = 0
            print "\nThis submission has already been posted within the threshold, trying for a new submission..."
        else:
            uniquepost = 1
            print "\nThis is a relatively new submission, it will be posted"

            if (not submission.over_18) or (post_NSFW == True):
                if not submission.is_self:
                    if submission.score > min_score:

                        if link_to_reddit == True:
                            titlelength = 135 - (53 + len(hashtags))
                            subpermalink = submission.permalink
                        else:
                            titlelength = 135 - (23 + len(hashtags))
                            subpermalink = ""
                        if autohashtag == True:
                            hashtitle = re.sub(
                                r'(\[)', r'\1#', submission.title)
                            shorttitle = hashtitle[
                                :titlelength] + (hashtitle[titlelength:] and '...')
                        else:
                            shorttitle = submission.title[
                                :titlelength] + (submission.title[titlelength:] and '...')

                        if not post_reddit_title:
                            shorttitle = ""

                        tweeturl = processUrl(submission.url)

                        if ((tweeturl[-4:] == ".jpg" or tweeturl[-5:] == "jpeg" or tweeturl[-4:] == ".png") and (post_images == True)) or ((tweeturl[-4:] == ".gif") and (post_gifs == True)):
                            print "\n\nTwitter Pic Post:\n\t" + (shorttitle + " " + hashtags + " " + subpermalink)
                            if not os.path.exists(img_dir + submission.id + "_" + tweeturl.split('/')[-1]):
                                urllib.urlretrieve(
                                    tweeturl, img_dir + submission.id + "_" + tweeturl.split('/')[-1])
                            #print submission.title, submission.url, submission.id
                            posted = postImage(
                                shorttitle, hashtags, subpermalink, tweeturl, submission.id)
                        else:
                            if (("youtube." in submission.url) or ("youtu.be" in submission.url)) and (post_youtube == True):
                                print "\n\nTwitter YouTube Post:\n\t" + (shorttitle + " " + hashtags + " " + subpermalink + " " + tweeturl)
                                posted = postLink(
                                    shorttitle, hashtags, subpermalink, tweeturl)
                            elif(("vine.co" in submission.url)) and (post_vine == True):
                                print "\n\nTwitter Vine Post:\n\t" + (shorttitle + " " + hashtags + " " + subpermalink + " " + tweeturl)
                                posted = postLink(
                                    shorttitle, hashtags, subpermalink, tweeturl)
                            elif(("soundcloud" in submission.url) or ("snd.sc" in submission.url)) and (post_soundcloud == True):
                                print "\n\nTwitter Soundcloud Post:\n\t" + (shorttitle + " " + hashtags + " " + subpermalink + " " + tweeturl)
                                posted = postLink(
                                    shorttitle, hashtags, subpermalink, tweeturl)
                            else:
                                print "[!] The randomly selected submission is not embeddable media! Trying again! [!]"

                    else:
                        print "[!] The randomly selected submission doesn't meet the minimum score threshold! Trying again! [!]"
                else:
                    print "[!] The randomly selected submission is a self-post and will not be posted. Trying again! [!]"
            else:
                print "[!] The randomly selected submission is NSFW (which is disabled)! Trying again! [!]"

# This saves the logs
file = open(img_dir + "submissions_log.txt", "w+")
newlogs = submission.id + "\n" + prevlogs
newlogs = newlogs[:(7 * repeat_threshold)]
#print newlogs
file.write(newlogs)
file.close()
