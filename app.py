from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todo_item"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():

    data = request.get_json()

    item = {
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }

    collection.insert_one(item)

    return jsonify({
        "message": "Todo item stored successfully"
    }), 201