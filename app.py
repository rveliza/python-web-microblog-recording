import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://reyner:WIFUp3FzIiFS6AE3@microblogcluster.eoxsbey.mongodb.net/")
app.db = client.microblog

entries = []

@app.route('/', methods=["GET", "POST"])
def home():
    # new_entries = app.db.entries.find({})
    # print([e for e in new_entries])
    if request.method == "POST":
        entry_content = request.form.get("content")
        formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
        short_date = datetime.datetime.today().strftime("%b %d")
        entries.append((entry_content, formatted_date, short_date))
        app.db.entries.insert_one({
            "content": entry_content, 
            "date": formatted_date})

    # entries_with_date = [(
    #     entry[0],
    #     entry[1],
    #     datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime('%b %d')) 
    #     for entry in entries]
    

    return render_template('home.html', entries=entries)


if __name__ == "__main__":
    app.run(debug=True)
