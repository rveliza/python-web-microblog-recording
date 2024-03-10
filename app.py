import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://reyner:WIFUp3FzIiFS6AE3@microblogcluster.eoxsbey.mongodb.net/")
app.db = client.microblog


@app.route('/', methods=["GET", "POST"])
def home():
    entries = [(
        entry["content"],
        entry["date"],
        entry["short_date"]
    ) for entry in app.db.entries.find({})]
 
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        short_date = datetime.datetime.today().strftime("%b %d")
        entries.append((entry_content, formatted_date, short_date))
        app.db.entries.insert_one({
            "content": entry_content, 
            "date": formatted_date,
            "short_date": short_date})
    return render_template('home.html', entries=entries)


if __name__ == "__main__":
    app.run(debug=True)
