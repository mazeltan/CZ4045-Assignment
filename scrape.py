from google_play_scraper import Sort, reviews_all, reviews
import pickle
import json
import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip',
                      'install', 'google_play_scraper'])


result, continuation_token = reviews(
    'com.zhiliaoapp.musically',
    lang='en',  # defaults to 'en'
    country='us',  # defaults to 'us'
    sort=Sort.NEWEST,  # defaults to Sort.NEWEST
    count=100000,  # defaults to 100
    filter_score_with=None  # defaults to None(means all score)
)

# store result as pickle
with open('result2.pkl', 'wb') as f:
    pickle.dump(result, f)
