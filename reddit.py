"""
Creates function to retrieve and send a random post from a subreddit
"""

import praw

r = praw.Reddit(client_id='X0VJq7wE00FEYQ',
                client_secret='oQ09GcBauKxPxN2su0o18Xb_EqC6vw',
                user_agent='windows:mnycz04.discord:v1.5.3 (by /u/mnycz04; mnycz04@gmail.com)')


async def reddit_post(subreddit):
    """
    gets a random post from given subreddit
    :param subreddit: the subreddit to get the post from
    :return: returns the link to the post
    """
    try:
        sub = r.subreddit(subreddit)
    except RuntimeError:
        raise ConnectionRefusedError
    try:
        post = sub.random()
        return post
    except RuntimeError:
        raise ConnectionRefusedError
