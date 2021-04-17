import firebase_admin
from firebase_admin import credentials, firestore

import flask
from flask import abort, jsonify, request, redirect

import json
import requests


#------ INIT the Flask APP ------------
app = flask.Flask(__name__)
#------ INIT the Flask APP ENDS -------


cred = credentials.Certificate("lets-food-admin-key.json")
firebase_app = firebase_admin.initialize_app(cred)
store = firestore.client()


@app.route('/addRestaurant', methods=['POST'])
def addRESTAURANT():
    data = request.get_json(force=True)
    dit = {}
    dit["name"] = data.get("name")
    dit["mobile"] = data.get("mobile")
    dit["address"] = data.get("address")
    dit["location"] = {
                        "lat":data.get("lat"), 
                        "long":data.get("lng")
                       }
    dit["type"] = data.get("type")
    dit["rest_id"] = data.get("rest_id")
    dit["imageUrl"] = data.get("imageUrl")
    dit["createdAt"] = firestore.SERVER_TIMESTAMP

    store.collection("RESTAURANTS").add(dit)
    
    return jsonify({"Response":200 })



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=False)