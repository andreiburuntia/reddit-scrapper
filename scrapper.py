import praw
import base64
import datetime

import psswd
import analyzer
import crypto
import tldr

# PRAW auth
reddit = praw.Reddit(client_id='Kl1R2En7fluKYw', \
                     client_secret='plGr2Rro6njXJGS9UzUQdhCvcck', \
                     user_agent='reddit-scrapper', \
                     username='buruuu', \
                     password=base64.b64decode(psswd.encoded_passwd).decode())

# helper functions
def get_date(submission):
    time = submission.created
    return datetime.datetime.fromtimestamp(time)

subreddit = reddit.subreddit('cryptocurrency')

top_subreddit = subreddit.hot(limit=1)

crypto_list = crypto.crypto_list()

def evaluate_submission(s):
    coms = []
    s.comments.replace_more(limit=0)
    cnt = 0
    print ("evaluating: " + s.title)
    for top_level_comment in s.comments:
        if cnt > 10:
            break
        cnt = cnt + 1
        for c in crypto_list[0]:
            if c in top_level_comment.body:
                coms.append(top_level_comment)
    coms.sort(key=lambda comment: comment.score, reverse=True)
    top_comments = coms[:25]
    for com in top_comments:
        print (str(com.body))

for tops in top_subreddit:
    evaluate_submission(tops)