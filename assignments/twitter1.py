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
        except Exception  as err:
            print err
            exit(1)

    def get_followes_list(self, name):
        followers = self.twiter.get_followers_list(screen_name=name)
        #print [i["screen_name"]for i in followers["users"]]
        self.list1=[i["screen_name"]for i in followers["users"]]
        return self.list1

    def get_common_followers(self, name1, name2):
        followers_name1=self.get_followes_list(name1)
        followers_name2=self.get_followes_list(name2)
#        list_common = [ followers_name2(member) for member in followers_name1 if member in followers_name2 ]
        list_common=list(set(followers_name1) & set(followers_name2))
        print list_common


obj = Twitter()
#obj.get_data('RGVzoomin', 'Children')
#obj.get_followes_list('RGVzoomin')
#obj.get_followes_list('purijagan')
obj.get_common_followers('RGVzoomin', 'purijagan')
