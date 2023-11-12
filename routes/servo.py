from flask import Blueprint, request, jsonify

servo = Blueprint("servo", __name__)

@servo.route('/', methods=['GET'])
def home():
    my_query = request.args.get("number", "")
    print("the number of my query is " + my_query)
    data = {"number": my_query}
    return data