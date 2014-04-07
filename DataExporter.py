from pymongo import MongoClient

mongo = MongoClient()
db = mongo.tweetdataset
tweets = db.sentimentData.find()
f = file('tweets.txt', 'w')
for i in tweets:
    f.write(i['text'].encode('utf-8') + "\n")