import tweepy

# Variables for keys
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''


#  Variables for setting authorization and receiving api
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# Object called API, used to read from and write to Twitter
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

# Functions that store the ID of the last seen tweet

def retrieveLastID(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def storeLastID(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return




mentions = api.mentions_timeline()

for mention in mentions:
    print(mention.text + ' - ' + str(mention.id))    
    if '#helloworld' in mention.text.lower():
        print('\n\n' + 'Found #helloworld! Responding back...' + '\n\n')
        api.update_status()