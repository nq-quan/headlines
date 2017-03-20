import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

# BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"
RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}


@app.route("/")
@app.route("/<pub>")
def bbc():
    return get_news('bbc')


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


def get_news(pub=bbc):
    feed = feedparser.parse(RSS_FEEDS[pub])
    first_article = feed['entries'][0]
    # return render_template("home.html")
    return render_template("home.html",
                    title=first_article.get("title"),
                    published=first_article.get("published"),
                    summary=first_article.get("summary"))
    # return """<html>
    # <body>
    # <h1> BBC Headlines </h1>
    # <b>{0}</b> <br/>
    # <i>{1}</i> <br/>
    # <p>{2}</p> <br/>
    # </body>
    # </html>""".format(first_article.get("title"), first_article.
    #                   get("published"), first_article.get("summary"))


if __name__ == "__main__":
    app.run(debug=True)
