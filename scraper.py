import praw
from prawcore.exceptions import ResponseException
import os
from dotenv import load_dotenv


load_dotenv()

print(os.getenv("reddit_client_id"))
reddit = praw.Reddit(
    client_id=f"{os.getenv('reddit_client_id')}", 
    client_secret=f"{os.getenv('reddit_client_secret')}", 
    user_agent=f"{os.getenv('reddit_user_agent')}"
  )

print(reddit.user.me())

subreddit_posts = reddit.subreddit('wallstreetbets').new()

f = open("./posts.txt", "a")

for post in subreddit_posts:
    splitPost = post.title.split(" ")
    for word in splitPost:
      if len(word) == 4:
        f.write(f"{word}")
        f.write("\n")
    # f.writelines([f"{post.title}", f"{post.selftext}", f"{post.created_utc}", "\n"])
    #f.writelines(f"\n{post.title}"{post.selftext}\n{post.created_utc}\n")

print('scraping has finished')