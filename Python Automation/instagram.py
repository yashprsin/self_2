from instabot import Bot

bot = Bot()
bot.login(username="feelingis_everything", password="hello yash")

# bot.upload_photo("yoda.jgp", caption="Cute biscuit eating yoda")
# bot.follow("yaaahko")
# bot.send_message("hey", ["yash_shorey"])

bot.unfollow_non_followers(n_to_unfollows=None)
