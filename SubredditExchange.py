import praw
from flask import Flask
from flask import render_template


app_client_id=''
app_client_secret=''
app_redirect_uri='http://localhost:8080/reddit_callback',
app_user_agent='subreddit_exchange_testing by /u/karldreher'

reddit = praw.Reddit(client_id=app_client_id,
                     client_secret=app_client_secret,
                     redirect_uri=app_redirect_uri,
                     user_agent=app_user_agent)


#figure out what "random" means
#scope may need to include subscribe in the future.  For now, get the "read" working.
#fix redirect
authorize_url = "https://www.reddit.com/api/v1/authorize?client_id=" + app_client_id+"&response_type=code&state=RANDOM_STRING&redirect_uri=http://localhost:8080/reddit_callback&duration=temporary&scope=mysubreddits"



app = Flask(__name__)

@app.route("/")
def subreddit_exchange_app():
    return render_template('index.html', url=authorize_url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

@app.route("/reddit_callback")
def Auth():
    return "You are authorized"
    

    
