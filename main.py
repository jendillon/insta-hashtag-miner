from instaloader import instaloader
from numpy import save
import csv
import os

if __name__ == '__main__':
    L = instaloader.Instaloader()

    print(os.environ.keys())

    # Login information goes here.
    username = os.environ.get('INSTA_LOGIN')
    password = os.environ.get('INSTA_PASSWORD')
    L.login(username, password)

    profile_name = 'seekingsomaart'
    profile = instaloader.Profile.from_username(L.context, profile_name)
    post_iterator = profile.get_posts()
    hashtag_dict = {}
    try:
        for post in post_iterator:
            hashtags = post.caption_hashtags
            print(hashtags)
            for tag in hashtags:
                if tag not in hashtag_dict:
                    hashtag_dict[tag] = 1
                else:
                    tag_count = hashtag_dict[tag]
                    hashtag_dict[tag] = tag_count + 1
    except KeyboardInterrupt:
        save("dict.json", post_iterator.freeze())

    hashtag_dict.keys.sort()

    with open('dict.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in hashtag_dict.items():
            writer.writerow([key, value])
