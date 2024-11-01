from flask import Flask,request,jsonify
import tweepy
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

Client = tweepy.Client(bearer_token=os.getenv("BEARER_TOKEN"),
                       consumer_key=os.getenv("TWITTER_API_KEY"),
                       consumer_secret=os.getenv("TWITTER_API_KEY_SECRET"),
                       access_token=os.getenv("ACCESS_TOKEN"),
                       access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"))

@app.route('/', methods=['GET'])
def hello():
    return "Hello, World!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    print("Data received", data)

    if 'transaction_id' in data:
        support_message = data.get('supporter_message','')
        if support_message:
            try:
                Client.create_tweet(text=support_message)
                print("Tweet sent:", support_message)
                return jsonify({"message": "Tweet sent successfully!"}), 200
            except Exception as e:
                print("Error sending tweet:", e)
                return jsonify({"message": "Failed to send tweet."}), 500
        else:
            return jsonify({"message": "Support message not found."}), 400
    else:
         return jsonify({"message": "Transaction ID not found."}), 400

if __name__ == '__main__':
    app.run(port=5000)