import twitter
import csv


api = twitter.Api(consumer_key= 'XxX',
               consumer_secret= 'XxX',
               access_token_key= 'XxX',
               access_token_secret= 'XxX')

petTweets = api.GetSearch(
    raw_query='q="first%dog"')


csvFile = open('FirstPet.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in petTweets:
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()
