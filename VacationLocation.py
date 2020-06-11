import twitter
import csv

api = twitter.Api(consumer_key= 'bb3ogHTO3sBaZU6tV4jfna6E8',
               consumer_secret= 'dizx9v6RAs3YH9v9kCc60YkWXpLJTAoxIFBOBG5hcNql95ppMB',
               access_token_key= '412662979-oPPKCIFn82X8mKF8WOAB9SUnFOSwLpbXWzWE5VKJ',
               access_token_secret= 'OunbJQJoV8lrItY3z0lC67iELNpwMAtv86KwmyFUhzJ2e')

vacationTweets = api.GetSearch(
    raw_query='q="favorite%20place%20to%20go%20on%20vacation"')


csvFile = open('VacationLocation.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in vacationTweets:
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print (tweet.created_at, tweet.text)
csvFile.close()