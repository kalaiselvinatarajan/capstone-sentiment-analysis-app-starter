from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    print("Hi")
    sentiment = None
    # TODO: Write the code that calls the sentiment analysis functions here.
    if request.method == "POST" :
        ext = request.form.get("user_text")
        sid = SentimentIntensityAnalyzer()
        sentiment = sid.polarity_scores(ext)
        print(sentiment)
    return render_template('form.html',sentiment=sentiment)
if __name__ == "__main__":
    app.run()
