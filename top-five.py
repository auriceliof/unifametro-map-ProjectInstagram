import instaloader;
import pandas as pd;


bot = instaloader.Instaloader()
# bot.login(user="auricelio.fm", passwd="")

top_results = instaloader.TopSearchResults(bot.context, 'python')

hashtags = top_results.get_hashtags()
profiles = top_results.get_profiles()

list_hashtags = []
for hashtag in hashtags:
    list_hashtags.append(hashtag.name)

list_profiles = []
for profile in profiles:
    list_profiles.append(profile.full_name)

lenght_hashtags = len(list_hashtags)
lenght_profiles = len(list_profiles)

if lenght_hashtags < lenght_profiles:
    dif = lenght_profiles - lenght_hashtags
    for i in range(dif):
        list_hashtags.append("null")

else:
    dif = lenght_hashtags - lenght_profiles
    for i in range(dif):
        list_profiles.append("null")

dict = {"Hashtag": list_hashtags, "Profiles": list_profiles}

dados_insta = pd.DataFrame(data=dict)
dados_insta.to_csv('pupulares.csv', sep=';')

print(dados_insta)
#print(dados_insta["Profiles"][2])
