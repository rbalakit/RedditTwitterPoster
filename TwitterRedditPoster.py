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
import urllib3

'''
IN ORDER TO RUN PROPERLY, THE CONFIGURATION FILE "BotConfig.py" IS NECESSARY

The section below is just temp configs that will be moved into the main config file after functionality testing
'''

# end of temp configs
'''
def postLink

def postImage
'''
# This part opens and loads the previous submissions so it doesn't repeat posts
file = open(img_dir + "submissions_log.txt", "a+")
prevlogs = file.read()
file.close()

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
r = praw.Reddit(user_agent=user_agent)
diditpost = 0
while (diditpost == 0):
    uniquepost = 0
    # for submission in r.get_subreddit('niconiconi').get_new(limit=1000):
    while (uniquepost == 0):
        submission = r.get_random_submission(source_subreddit)
        print submission.title, submission.url, submission.id
        if submission.id in prevlogs:
            uniquepost = 0
            print "This submission has already been posted within the threshold, trying for a new submission..."
        else:
            uniquepost = 1
            print "This is a relatively new submission, it will be posted"

            if (not submission.over_18) or (post_NSFW==True):
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

                        tweeturl = submission.url
                        if "imgur" in submission.url:
                            if not ("i.imgur" in submission.url):
                                iurl = re.sub(
                                    r'(\http://)', r'\1i.', submission.url)
                                iexurl = iurl + ".png"
                            else:
                                iexurl = submission.url
                                iurl = iexurl[:-4]
                            source = urllib.urlopen(iexurl)
                            extension = guess_extension(
                                source.info()['Content-Type'])
                            if extension == ".jpe":
                                tweeturl = iurl + ".jpg"
                            elif extension == ".png":
                                tweeturl = iurl + ".png"
                            elif extension == ".gif":
                                tweeturl = iurl + ".gif"

                        if (tweeturl[-4:] == (".jpg" or tweeturl[-5:] == "jpeg" or tweeturl[-4:] == ".png") and (post_images == True)) or ((tweeturl[-4:] == ".gif") and (post_gifs == True)):
                            if not os.path.exists(img_dir + submission.id + "_" + tweeturl.split('/')[-1]):
                                urllib.urlretrieve(
                                    tweeturl, img_dir + submission.id + "_" + tweeturl.split('/')[-1])
                            print submission.title, submission.url, submission.id
                            print "Twitter Pic Post:\n\t" + (shorttitle + " " + hashtags + " " + subpermalink)
                            photo = open(
                                img_dir + submission.id + "_" + tweeturl.split('/')[-1], 'rb')
                            diditpost = 1
                        else:

                            # print "link post "+submission.title+" is not jpg,
                            # png, or gif"
                            if (("youtube." in submission.url) or ("youtu.be" in submission.url)) and (post_youtube == True):
                                print "Twitter YouTube Post:\n\t" + (shorttitle + " " + hashtags + " " + subpermalink + " " + tweeturl)
                                diditpost = 1
                            elif(("vine.co" in submission.url)) and (post_vine == True):
                                print "Twitter Vine Post:\n\t" + (shorttitle + " " + hashtags + " " + subpermalink + " " + tweeturl)
                                diditpost = 1
                            elif(("soundcloud" in submission.url) or ("snd.sc" in submission.url)) and (post_soundcloud == True):
                                print "Twitter Soundcloud Post:\n\t" + (shorttitle + " " + hashtags + " " + subpermalink + " " + tweeturl)
                                diditpost = 1
                            else:
                                print "[!] The randomly selected submission is not embeddable media! Trying again! [!]"
                                '''
                    else:
                        print "[!]The randomly selected submission doesn't meet the minimum score threshold! Trying again! [!]"
                 else:
                    print "[!]The randomly selected submission is a self-post and will not be posted. Trying again! [!]"
             else:
                print "[!] The randomly selected submission is NSFW (which is disabled)! Trying again! [!]"'''

# This saves the logs
file = open(img_dir + "submissions_log.txt", "w+")
newlogs = submission.id + "\n" + prevlogs
newlogs = newlogs[:(7*repeat_threshold)]
print newlogs
file.write(newlogs)
file.close()
