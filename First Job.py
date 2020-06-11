import twitter
import csv


api = twitter.Api(consumer_key= 'XxX',
               consumer_secret= 'XxX',
               access_token_key= 'XxX',
               access_token_secret= 'XxX')

jobTweets = api.GetSearch(
    raw_query='q="first%job"')


csvFile = open('FirstJob.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in jobTweets:
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()
