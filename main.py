from flask import Flask
import pymongo

app = Flask(__name__)

connection_url="mongodb://localhost:27017/"
client=pymongo.MongoClient(connection_url)
collection_name="face-auth"
collection = client[collection_name]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run(debug=True)    