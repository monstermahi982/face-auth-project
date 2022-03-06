from flask import Flask,Response,request, jsonify
# import pymongo
import json
from flask_serialize import FlaskSerialize
from flask_pymongo import PyMongo, ObjectId
from bson.json_util import dumps

app = Flask(__name__)
app.secret_key = "secret key"
app.config['MONGO_URI'] = "mongodb://localhost:27017/face_auth"
mongo = PyMongo(app)
db = mongo.db.face_auth

@app.route("/user",methods=["GET", "POST"])
def users():
    if request.method == "POST":
        try:
            result = db.insert_one(request.json)
            return jsonify({'msg': 'data inserted'})
        except Exception as ex:
            print(ex)
            return jsonify({'Message':"Something went wrong"})
    elif request.method == "GET":
        try:
            data =list(db.find())
            for user in data:
                user["_id"]= str(ObjectId(user["_id"]))
            return jsonify(data)
        except Exception as ex:
            print(ex)
            return jsonify({'Message':"Something went wrong"})

@app.route("/user/<id>",methods=["GET", "PUT", "DELETE"])
def one_user(id):
    if request.method == "PUT":
        try:
            db.update_one({'_id':ObjectId(id)}, {'$set': {
                'name':request.json['name'],
                'gmail':request.json['gmail']
            }})
            return jsonify({'Message':"User Updated"})
        except Exception as ex:
            print(ex)
            return jsonify({'Message':"Something went wrong"})
    elif request.method == "GET":
        try:
            user = db.find_one({'_id':ObjectId(id)})
            return jsonify({
                '_id':str(ObjectId(user['_id'])),
                'name':user['name']
            })
        except Exception as ex:
            print(ex)
            return jsonify({'Message':"Something went wrong"})
    elif request.method == "DELETE":
        try:
            db.delete_one({'_id':ObjectId(id)})
            return jsonify({'Message':"User Deleted"})
        except Exception as ex:
            print(ex)
            return jsonify({'Message':"Something went wrong"})

if __name__ == '__main__':
    app.run(debug=True)    


# from flask import Flask, redirect, url_for
# from pymongo import MongoClient
# from flask_cors import CORS, cross_origin
# import json

# app = Flask(__name__)
# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'


# mongoClient = MongoClient('mongodb://127.0.0.1:27017')
# db = mongoClient.get_database('face_auth')
# names_col = db.get_collection('users')

# @app.route('/addname/<name>/', methods=["POST"])
# def addname(name):
#     names_col.insert_one({"name": name.lower()})
#     return redirect(url_for('getnames'))

# @app.route('/getnames/')
# def getnames():
#     names_json = []
#     if names_col.find({}):
#         for name in names_col.find({}).sort("name"):
#             names_json.append({"name": name['name'], "id": str(name['_id'])})
#     return json.dumps(names_json)

# if __name__ == "__main__":
#     app.run(debug=True)