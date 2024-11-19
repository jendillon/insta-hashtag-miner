import csv
import os
from instaloader import instaloader
PROFILE_NAME = 'seekingsomaart'

def save_sorted_csv( unsorted_dict ):
    """
    Takes a dictionary, sorts it, and writes it to a .csv 
    """""
    sorted_hashtag_dict = dict(sorted(unsorted_dict.items()))
    with open('dict.csv', 'w', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in sorted_hashtag_dict.items():
            writer.writerow([key, value])

def login():
    """
    Logs into instagram using locally stored credentials
    """
    loader = instaloader.Instaloader()
    username = os.environ.get('INSTA_LOGIN')
    password = os.environ.get('INSTA_PASSWORD')
    L.login(username, password)
    return loader

if __name__ == '__main__':
    """Using locally stored instagram credentials, counts instances of 
    hashtags on a given instagram account, and outputs them to a .csv"""

    L = login()
    profile = instaloader.Profile.from_username(L.context, PROFILE_NAME)
    post_iterator = profile.get_posts()

    hashtag_dict = {}
    try:
        for post in post_iterator:
            hashtags = post.caption_hashtags
            #print(hashtags)
            for tag in hashtags:
                if tag not in hashtag_dict:
                    hashtag_dict[tag] = 1
                else:
                    tag_count = hashtag_dict[tag]
                    hashtag_dict[tag] = tag_count + 1
    except KeyboardInterrupt:
        save_sorted_csv(hashtag_dict)
    finally:
        save_sorted_csv(hashtag_dict)


