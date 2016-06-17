import re, praw, requests, os, glob, sys, bs4


if len(sys.argv) < 2:
	print('Usage: ')
	print('python {} subreddit'.format(sys.argv[0]))
	sys.exit()
elif len(sys.argv) >= 2:
	subreddit = sys.argv[1]

reddit = praw.Reddit(user_agent='asduddfbergfdagsdafsdsadfaadfsdfsd')

random_submission = reddit.get_subreddit(subreddit).get_random_submission()

while 'http://i.imgur.com/' not in random_submission.url:
	random_submission = reddit.get_subreddit(subreddit).get_random_submission()


f = open('walp', 'wb')
r = requests.get(random_submission.url)
for chunk in r:
	f.write(chunk)

f.close()

os.system('gsettings set org.gnome.desktop.background draw-background false && gsettings set org.gnome.desktop.background picture-uri file://{}/{}'.format(os.path.dirname(os.path.abspath(__file__)), 'walp'))
