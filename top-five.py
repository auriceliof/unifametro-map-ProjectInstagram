import instaloader;

bot = instaloader.Instaloader()
bot.login(user="auricelio.fm", passwd="")

top_results = instaloader.TopSearchResults(bot.context, 'python')

hashtags = top_results.get_hashtags()
profiles = top_results.get_profiles()

list_hashtags = []
for hashtag in hashtags:
    list_hashtags.append(hashtag.name)

list_profiles = []
for profile in profiles:
    list_profiles.append(profile.full_name)

print(list_hashtags)
print(list_profiles)
