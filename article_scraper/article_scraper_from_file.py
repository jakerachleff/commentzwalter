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

RSS_FEED_URL_FILE = "rss_feed_urls"
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
	print(rss_feed)

	feed = feedparser.parse(rss_feed)

	for post in feed.entries:
		print("Processing article: \"{title}\"".format(title=post.title))
		text = process_article(post.link)

		file_path = OUTFILE_PATH + "/all_articles/" + post.title

		try:
			new_file = open(file_path, 'w')
			new_file.write(text)
			new_file.close()

		except:
			print('Error creating file {filename}'.format(filename = file_path))

def append_feeds():
	rss_feeds = []
	with open(RSS_FEED_URL_FILE) as f:
		for url in f:
			if url[0] != '#':
				rss_feeds.append(url)
		f.close()
	return rss_feeds


rss_feeds = append_feeds()

data_path = os.path.join(os.getcwd(), OUTFILE_PATH)
if not os.path.exists(data_path):
	os.makedirs(data_path)

data_path = os.path.join(os.getcwd(), OUTFILE_PATH + "/all_articles")
if not os.path.exists(data_path):
		os.makedirs(data_path)

pool = Pool(2)
results = pool.map(process_feed, rss_feeds)





