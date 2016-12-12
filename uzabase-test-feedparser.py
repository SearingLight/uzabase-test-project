# -*- coding: utf-8 -*-
#必要モジュールをインポート
import feedparser

#フィードを選択・挿入
feed = feedparser.parse('http://tech.uzabase.com/rss')
feed2 = feedparser.parse('http://www.giantbomb.com/feeds/reviews/')
feed3 = feedparser.parse('https://www.panic.com/blog/feed/')

#内容を表示
for post in feed.entries:
	print(post.title[:10] + ": " + post.description[:30] + "")
	
for post in feed2.entries:
	print(post.title[:10] + ": " + post.description[:30] + "")
	
for post in feed3.entries:
	print(post.title[:10] + ": " + post.description[:30] + "")
