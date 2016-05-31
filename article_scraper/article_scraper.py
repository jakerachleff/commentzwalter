"""
File: article_scraper.py
-------------------
Final Project: Commentz-Walter String Matching Algorithm
Course: CS 166
Authors: Christina Gilbert
Group: Christina Gilbert, Eric Ehizokhale, Jake Rachleff

Pulls articles from RSS feeds and saves text to disk.
"""

import requests
import bs4
import feedparser
from collections import namedtuple
import os
from multiprocessing import Pool

OUTFILE_PATH = "articles"

#if ORGANIZED, puts articles in folders by feed. otherwise,
#puts all files in one folder all_articles
ORGANIZED = False

def process_article(article_url):

	response = requests.get(article_url)

	soup = bs4.BeautifulSoup(response.text, "html.parser")

	# Get all <p> divs
	page_divs = soup.find_all('p')

	div_text = []
	for div in page_divs:
		text = div.getText()
		div_text.append(text)

	return ' '.join(div_text)

def process_feed(rss_feed):
	curr_directory = OUTFILE_PATH + "/" + rss_feed.name
	data_path = os.path.join(os.getcwd(), curr_directory)
	if not os.path.exists(data_path):
	    os.makedirs(data_path)

	feed = feedparser.parse(rss_feed.url)

	for post in feed.entries:
		print("Processing article: \"{title}\"".format(title=post.title))
		text = process_article(post.link)

		file_path = curr_directory + "/" + post.title if ORGANIZED else OUTFILE_PATH + "/all_articles/" + post.title

		try:
			new_file = open(file_path, 'w')
			new_file.write(text)
			new_file.close()

		except:
			print('Error creating file {filename}'.format(filename = curr_directory + "/" + post.title))

def append_feeds():
	rss_feeds = []
	rss_feeds.append(RSS_Feed(name="Bloomberg_Politics", url="feed://www.bloomberg.com/politics/feeds/site.xml"))

	rss_feeds.append(RSS_Feed(name="Google_US_News", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&topic=b&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Technology", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&topic=tc&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Entertainment_News", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&topic=e&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Sports", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&topic=s&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Health", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&topic=m&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Science", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&topic=snc&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Elections", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&topic=el&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_China_News", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&csid=c68abdab5e4f18cf&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Chad", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&csid=c68abdab5e4f18cf&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Kurdistan_Workers_Party", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&q=Kurdistan+Workers%5Cx27+Party&output=rsss"))
	rss_feeds.append(RSS_Feed(name="Google_UAE", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&q=United+Arab+Emirates&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Edward_Snowden", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&q=Edward+Snowden&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Baltimore", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&q=Baltimore&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Bernie_Sanders", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&q=Bernie+Sanders&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_Fallujah", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&q=Fallujah&output=rss"))
	rss_feeds.append(RSS_Feed(name="Google_European_Migrant_Crisis", url="feed://news.google.com/news?cf=all&hl=en&pz=1&ned=us&q=European+migrant+crisis&output=rss"))
	return rss_feeds

RSS_Feed = namedtuple('RSS_Feed', ['name', 'url'])
rss_feeds = append_feeds()

data_path = os.path.join(os.getcwd(), OUTFILE_PATH)
if not os.path.exists(data_path):
    os.makedirs(data_path)

data_path = os.path.join(os.getcwd(), OUTFILE_PATH + "/all_articles")
if not os.path.exists(data_path):
	    os.makedirs(data_path)

pool = Pool(4)
results = pool.map(process_feed, rss_feeds)





