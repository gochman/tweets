#  Tweets

from root folder run with 

```
docker-compose up --build -d
```

app runs on - http://localhost:5000


___

Implements the following API:
```
GET 
/tweets 
[ 
 { 
   "id": [INT], 
   "content": [STRING], 
   "username: [STRING], 
   "timestamp": [ISO_FORMATED_STRING], 
   "likes_count: [INT] 
    "retweets_count": [INT] 
 } 
]

POST 
/tweets 
{ 
 "content": [STRING], 
  "username: [STRING] 
}

POST 
/tweets/[:id]/likes 
{ 
  "username": [STRING] 
} 

POST 
/tweets/[:id]/retweet 
{ 
  "username": [STRING] 
}
 
GET 
/retweets 
[ 
 { 
 "content",[STRING] 
 "retweet_user": [STRING] 
  "tweet_id": [INT] 
  "tweet_user": [STRING] 
  "timestamp": [ISO_FORMATED_STRING] 
```


> author: gochman6@gmail.com