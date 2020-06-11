import twitter
import csv


api = twitter.Api(consumer_key= 'XxX',
               consumer_secret= 'XxX',
               access_token_key= 'XxX',
               access_token_secret= 'XxX')

bookTweets = api.GetSearch(
    raw_query='q="favorite%20book"%20since%3A2020-05-01')


csvFile = open('FavoriteBook.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in bookTweets:
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()
