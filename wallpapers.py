#Grzegorz 'maszeczuszets' Pach
#Script takes name of subreddit, looks for imgur link, downloads image and sets wallpaper(Ubuntu only)


import praw, requests, os, sys, bs4


#CONFIG
USER_AGENT = 'SOMERANDOMSHITSSS' 
WALLPAPER_NAME = 'walp'


#gets arguments from user - name of subreddit(source of images)
if len(sys.argv) < 2:
	print('Usage: ')
	print('python {} subreddit'.format(sys.argv[0]))
	sys.exit()
elif len(sys.argv) >= 2:
	subreddit = sys.argv[1]

reddit = praw.Reddit(user_agent=USER_AGENT)

#looking for random imgur link - if there is no imgur link in submission script is looking for diffrent one
while True:
	random_submission = reddit.get_subreddit(subreddit).get_random_submission()
	if 'http://i.imgur.com/' in random_submission.url:
		image_url = random_submission.url
		break
	elif 'http://imgur.com/' in random_submission.url:
		r = requests.get(random_submission.url)
		soup = bs4.BeautifulSoup(r.text, 'html.parser')
		image_url = 'http:' + soup.findAll('img', {'class': 'post-image-placeholder'})[0]['src']
		break

#writing random image as file
f = open(WALLPAPER_NAME, 'wb')
r = requests.get(image_url)
for chunk in r:
	f.write(chunk)

f.close()

#sets wallpaper - tested on ubuntu 16.04 LTS
os.system('gsettings set org.gnome.desktop.background draw-background false && gsettings set org.gnome.desktop.background picture-uri file://{}/{}'.format(os.path.dirname(os.path.abspath(__file__)), WALLPAPER_NAME))
