from pymongo import MongoClient
from bson.son import SON
from pprint import pprint

client = MongoClient()
db = client.tweet
tweets = db.training


def pp_all(col):
    for p in col:
        pprint(p)


def main():
    q_1()
    q_2()
    q_3()
    q_4()
    q_5()


def q_1():
    print('1. How many Twitter users are in the database? ')
    tw = tweets.distinct('user')
    print('Unique users:', len(tw), '\n')


def q_2():
    print('2. Which Twitter users link the most to other Twitter users? (Provide the top ten.)')
    print('Uses the most @:')
    pipeline = [
        {"$match": {"text": {"$regex": "@"}}},
        {"$group": {"_id": "$user", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("user", -1)])},
        {"$limit": 10}
    ]
    tw = tweets.aggregate(pipeline)
    pp_all(tw)
    print()


def q_3(): #does not work
    print('3. Who is are the most mentioned Twitter users? (Provide the top five.)')
    print('Users mentioned the most:')
    pipeline = [
        {"$match": {"text": {"$regex": "@\\w*"}}},
        {"$group": {
            "_id": {"$substrCP": ["$text", {"$indexOfCP": ["$text", "@"]}, {"$indexOfCP": ["$text", " "]}]},
            "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("user", -1)])},
        {"$limit": 5}
    ]
    tw = tweets.aggregate(pipeline)
    pp_all(tw)
    print()


def q_4():
    print('4. Who are the most active Twitter users (top ten)?')
    print('Tweets the most:')
    pipeline = [
        {"$group": {"_id": "$user", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("user", -1)])},
        {"$limit": 10}
    ]
    tw = tweets.aggregate(pipeline)
    pp_all(tw)
    print()


def q_5():
    print('5. Who are the five most grumpy (most negative tweets) and the most happy (most positive tweets)?')
    print('Top 5 negative:')
    pipeline = [
        {"$match": {"polarity": 0}},
        {"$group": {"_id": "$user", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("user", -1)])},
        {"$limit": 5}
    ]
    tw = tweets.aggregate(pipeline)
    pp_all(tw)
    print()

    print('Top 5 positive:')
    pipeline = [
        {"$match": {"polarity": 4}},
        {"$group": {"_id": "$user", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("user", -1)])},
        {"$limit": 5}
    ]
    tw = tweets.aggregate(pipeline)
    pp_all(tw)

if __name__ == "__main__":
    main()
