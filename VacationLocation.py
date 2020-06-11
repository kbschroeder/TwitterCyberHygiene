import twitter
import csv

api = twitter.Api(consumer_key= 'XxX',
               consumer_secret= 'XxX',
               access_token_key= 'XxX',
               access_token_secret= 'XxX')

vacationTweets = api.GetSearch(
    raw_query='q="favorite%20place%20to%20go%20on%20vacation"')


csvFile = open('VacationLocation.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in vacationTweets:
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()
