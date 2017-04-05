import feedparser
from flask import Flask
from flask import render_template
# Chapter 4
from flask import request

app = Flask(__name__)

# BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}


@app.route("/")

# def bbc():
#    return get_news('bbc')


# @app.route("/bbc")
# def bbc():
#     return get_news('bbc')
#
#
# @app.route("/cnn")
# def cnn():
#     return get_news('cnn')
#
#
# @app.route("/fox")
# def fox():
#     return get_news('fox')

@app.route("/<pub>")
def get_news():
# Chapter 4
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])


# Chapter 3
"""
def get_news(pub="bbc"):
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    # return render_template("home.html")
    return render_template("home.html", articles=feed['entries'])
                    # title=first_article.get("title"),
                    # published=first_article.get("published"),
                    # summary=first_article.get("summary"))

"""

if __name__ == "__main__":
    app.run(debug=True)
