from flask import request
from app import app, db
import models
import datetime

db.create_all()


@app.route('/')
def index():
    return "Hello, Welcome!"


@app.route('/tweets')
def get_tweets():
    """
    Returns all the tweets in the app
    :return: a dictionary of the form: {"tweets": output} where output is a list of dictionaries, each one represents
     a tweet with relevant information on it.
    """
    tweets = models.Tweet.query.all()
    output = []

    for tweet in tweets:
        tweet_data = {'id': tweet.id,
                      'content': tweet.text_content,
                      'username': tweet.username,
                      'timestamp': tweet.timestamp.isoformat(),
                      'likes_count': models.Like.query.filter(models.Like.post_id == tweet.id).count(),
                      'retweets_count': models.Retweet.query.filter(models.Retweet.post_id == tweet.id).count()}

        output.append(tweet_data)

    return {"tweets": output}


@app.route('/tweets', methods=['POST'])
def add_tweet():
    """
    Adds tweet to the application, expects "content" and "username" from the request body.
    :return: A dictionary of the form {'id': the id number of the newly inserted tweet}
    """
    tweet = models.Tweet(text_content=request.json['content'], username=request.json['username'],
                         timestamp=datetime.datetime.now())
    db.session.add(tweet)
    db.session.commit()

    return {'id': tweet.id}


@app.route('/tweets/<id>/likes', methods=['POST'])
def add_like(id):
    """
    Adds like to the application, gets id as a parameter in the url, and expects "username" in the request body.
    :param id: the tweet id to like
    :return: the like_id in the system of case of success or in case of re-entering existing like.
    404 page if the original tweet does not exists.
    """
    username = request.json['username']
    duplicate_likes_query = models.Like.query.filter(models.Like.username == username, models.Like.post_id == id)
    # if like from this user to this tweet already exist
    if duplicate_likes_query.count() > 0:
        return {'like_id': duplicate_likes_query.first().like_id}

    # if original tweet does not exist -> 404
    models.Tweet.query.get_or_404(id)

    like = models.Like(post_id=id, username=username, timestamp=datetime.datetime.now())
    db.session.add(like)
    db.session.commit()

    return {'like_id': like.like_id}


@app.route('/tweets/<id>/retweet', methods=['POST'])
def add_retweet(id):
    """
    Adds retweet to the application, gets id as a parameter in the url, and expects "username" in the request body.
    :param id: the tweet id to retweet
    :return: the retweet id in the system of case of success.
    404 page if the original tweet does not exists.
    """
    # if original tweet does not exist -> 404
    models.Tweet.query.get_or_404(id)

    retweet = models.Retweet(post_id=id, username=request.json['username'],
                             timestamp=datetime.datetime.now())

    db.session.add(retweet)
    db.session.commit()

    return {'retweet_id': retweet.retweet_id}


@app.route('/retweets')
def get_retweets():
    """
    Returns all the retweets in the app
    :return: a dictionary of the form: {"retweets": output} where output is a list of dictionaries, each one represents
     a retweet with relevant information on it.
    """

    retweets = models.Retweet.query.all()
    output = []

    for retweet in retweets:
        original_tweet = models.Tweet.query.get(retweet.post_id)
        retweet_data = {
            'content': original_tweet.text_content,
            'retweet_user': retweet.username,
            'tweet_id': original_tweet.id,
            'tweet_user': original_tweet.username,
            'timestamp': retweet.timestamp.isoformat()
        }

        output.append(retweet_data)

    return {"retweets": output}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
