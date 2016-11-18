from twython import Twython
import ConfigParser


class Twitter:
    def __init__(self):
        config_ptr = ConfigParser.ConfigParser()
        config_ptr.read('twitter.cfg')
        self.cust_key = config_ptr.get('Twitter', 'Consumer_Key')
        self.cust_secret = config_ptr.get('Twitter', 'Consumer_Secret')
        self.twiter = Twython(self.cust_key, self.cust_secret)

    def get_data(self, name, key_word):
        try:
            user_timeline = self.twiter.get_user_timeline(screen_name=name)
            for teweet in user_timeline:
                if key_word in teweet['text']:
                    print teweet['text']
        except TwythonError as err:
            print err

    def get_followes_list(self, name):
        followers = self.twiter.get_followers_list(screen_name=name)
        print [i["screen_name"]for i in followers["users"]]

obj = Twitter()
obj.get_data('RGVzoomin', 'Children')
obj.get_followes_list('RGVzoomin')
