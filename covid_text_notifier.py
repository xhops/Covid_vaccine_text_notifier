import tweepy
from twilio.rest import Client

'''
IMPORTANT:

Please change all variables labeled CHANGE_THIS in the script. Explanations are commented near each variable.
'''


'''
Twitter authentication. This can be retrieved by creating an account at https://developer.twitter.com/en/portal/projects-and-apps
and creating a project. Keep in mind this may take a few days to get this from Twitter.
'''

consumer_key = "CHANGE_THIS"
consumer_secret = "CHANGE_THIS"

access_token = "CHANGE_THIS"
access_token_secret = "CHANGE_THIS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token = (access_token, access_token_secret)
#authentication end

#declare wrapper for api
api = tweepy.API(auth)

'''
text_message - blank string for twilio sms text. 
num_of_tweets - change this to increase or decrease the number of recent tweets you wish to see
tweet_results - blank array to store tweet data. This will be iterated through and placed in the text_message variable
user_tag - Twitter tag without the @ symbol
'''
text_message = ""
num_of_tweets = 10
tweet_results = []
user_tag = 'IAVaccineAlerts'

#specify user and user properties to look up
user = api.get_user(user_tag)

#Search user's timeline num_of_tweets, exclude replies, and show entire tweet in output
tweets = api.user_timeline(user_tag, count=num_of_tweets, exclude_replies=True, tweet_mode="extended")


#generate num_of_tweets after replies are removed and append to tweet_results array
for status in tweets:
    Possible_covid_tweets = status.full_text
    tweet_results.append(Possible_covid_tweets)

#interate through tweet_results array and add to text_message variable with better formatting
for post in tweet_results:
    text_message = "\n" + post + "\n" + text_message
    #print('\n')
    
        
'''
 Twilio SMS portion to send text with tweet information. SIDs and auth_token can be retrieved once you set up a trial 
 Twilio account, If you want to send to multiple users besides your number, you will have to upgrade the account, or
 get the new number verified as shown in the Verify your personal phone number section in the Twilio documentation. 
 Shown here: https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account    
'''

def send_text_msg():

    #text authorization
    account_sid = 'CHANGE_THIS' 
    auth_token = 'CHANGE_THIS' 
    client = Client(account_sid, auth_token) 
    
    #create message
    message = client.messages.create(  
                                messaging_service_sid='CHANGE_THIS', 
                                body=  "\n" + "Here are the " + str(num_of_tweets) + " most recent tweets from " + str(user_tag) + ": " + "\n" + str(text_message),      
                                to='+YOUR_FULL_NUMBER. Ex. +17181234567' 
                            ) 
    


#call text message function
send_text_msg()
