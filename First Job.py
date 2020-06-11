import twitter
import csv

api = twitter.Api(consumer_key= 'bb3ogHTO3sBaZU6tV4jfna6E8',
               consumer_secret= 'dizx9v6RAs3YH9v9kCc60YkWXpLJTAoxIFBOBG5hcNql95ppMB',
               access_token_key= '412662979-oPPKCIFn82X8mKF8WOAB9SUnFOSwLpbXWzWE5VKJ',
               access_token_secret= 'OunbJQJoV8lrItY3z0lC67iELNpwMAtv86KwmyFUhzJ2e')

jobTweets = api.GetSearch(
    raw_query='q="first%job"')


csvFile = open('FirstJob.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in jobTweets:
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()