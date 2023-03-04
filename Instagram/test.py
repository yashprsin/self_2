from instabot import Bot
import time
my_bot = Bot()

my_bot.login(username="yash_shorey", password="")

# follower_list = my_bot.get_user_followers("yash_shorey")
#
following_list = my_bot.get_user_following("yash_shorey")

# for each_follower in following_list:
    # time.sleep(300)
    # print(my_bot.get_username_from_user_id(each_follower))

my_bot.logout()