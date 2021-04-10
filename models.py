from app import db

# no need for class __init__ methods
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models

class Tweet(db.Model):
    """
    A class representing a Tweet in the application.
    Attributes:
        id: The tweet ID
        text_content: the content of the tweet
        username: the username of the person who tweeted this tweet
        timestamp: datetime object of the time the tweet was tweeted
    """
    id = db.Column(db.Integer, primary_key=True)
    text_content = db.Column(db.String(280))
    username = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        """
        Computes a string representation for Tweet objects.
        :return: String representation for Tweet Objects
        """
        return f"\ntweet id: {self.id}, by {self.username}. text: {self.text_content}"


class Like(db.Model):
    """
    A class representing a Like in the application.
    Attributes:
        like_id: The like ID in the db
        username: the username of the person who did the like
        post_id: the liked tweet id
        timestamp: datetime object of the time the like was done
    """
    like_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    post_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        """
        Computes a String representation for Like objects.
        :return: String representation for Like Objects
        """
        return f"\nlike id: {self.like_id}, by {self.username} to {self.post_id}"


class Retweet(db.Model):
    """
    A class representing a Retweet (RT) in the application.
    Attributes:
        retweet_id: The retweet ID in the db
        username: the username of the person who did the retweet
        post_id: the original post id
        timestamp: datetime object of the time the retweet was done
    """
    retweet_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    post_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        """
        Computes a String representation for RT objects.
        :return: String representation for RT Objects
        """
        return f"\nrt id: {self.retweet_id}, by {self.username} to {self.post_id}"