import twitter
import csv

api = twitter.Api(consumer_key= 'XxX',
               consumer_secret= 'XxX',
               access_token_key= 'XxX',
               access_token_secret= 'XxX')

carTweets = api.GetSearch(
    raw_query='q="first%20car"%20since%3A2020-05-01')


csvFile = open('CarColor.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in carTweets:
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()
