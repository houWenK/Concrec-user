from flask import Flask, jsonify, request
import api.rank_service_client as rank_client
from api.anime import get_anime
from mysql.consumer_data import get_consumerByName, add_consumer, get_consumerById, update_consumer
from result.JsonResponse import JsonResponse
import datetime

# from flask_cors import CORS, cross_origin

app = Flask('api-service', static_folder='img')


@app.route("/")
def get_recommends():
    user_id = request.args.get('user_id', type=int)
    rec_animes = rank_client.get_anime(user_id)
    for item in rec_animes:
        item['anime'] = get_anime(item['anime_id'])
    res = rec_animes

    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/sim")
def get_similar_animes():
    anime_id = request.args.get('anime_id', type=int)
    if anime_id is None:
        return 'bad anime id', 400

    sim_animes = rank_client.get_similar_anime(anime_id)
    for item in sim_animes:
        item['anime'] = get_anime(item['anime_id'])
    res = sim_animes

    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/hot")
def get_hot_animes():
    rec_animes = rank_client.get_hot_anime()
    for item in rec_animes:
        item['anime'] = get_anime(item['anime_id'])
    res = rec_animes

    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/high")
def get_high_animes():
    rec_animes = rank_client.get_high_anime()
    for item in rec_animes:
        item['anime'] = get_anime(item['anime_id'])
    res = rec_animes

    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/anime/<id>")
def get_anime_by_id(id):
    res = get_anime(id)
    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/consumer/login", methods=['POST'])
# @cross_origin()
def consumer_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = get_consumerByName(username)
    userMsg = {}
    if user != None and password == user[1]:
        userMsg['id'] = user[0]
        userMsg['username'] = username
        userMsg['avator'] = user[2]
        return JsonResponse.success(userMsg).to_dict()
    else:
        return JsonResponse.error().to_dict()


@app.route("/consumer/add", methods=['POST'])
def consumer_add():
    username = request.form.get('username')
    password = request.form.get('password')
    sex = request.form.get('sex')
    phoneNum = request.form.get('phoneNum')
    email = request.form.get('email')
    birth = request.form.get('birth')
    introduction = request.form.get('introduction')
    location = request.form.get('location')
    avator = request.form.get('avator')
    createTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    member_information = {
        "username": username,
        "password": password,
        "sex": sex,
        "phoneNum": phoneNum,
        "email": email,
        "birth": birth,
        "introduction": introduction,
        "location": location,
        "avator": avator,
        "createTime": createTime,
        "updateTime": updateTime
    }
    add_consumer(member_information)
    return JsonResponse.success().to_dict()


@app.route("/consumer/selectByPrimaryKey", methods=['GET'])
def consumer_selectByPrimaryKey():
    userId = request.args.get('id', type=int)
    user = get_consumerById(userId)
    if user != None:
        userMsg = {}
        userMsg['username'] = user[0]
        userMsg['password'] = user[1]
        userMsg['sex'] = user[2]
        userMsg['phoneNum'] = user[3]
        userMsg['email'] = user[4]
        userMsg['birth'] = user[5]
        userMsg['introduction'] = user[6]
        userMsg['location'] = user[7]
        return JsonResponse.success(userMsg).to_dict()
    else:
        return JsonResponse.error().to_dict()


@app.route("/consumer/update", methods=['POST'])
def consumer_update():
    id = request.form.get('id')
    username = request.form.get('username')
    password = request.form.get('password')
    sex = request.form.get('sex')
    phoneNum = request.form.get('phoneNum')
    email = request.form.get('email')
    birth = request.form.get('birth')
    introduction = request.form.get('introduction')
    location = request.form.get('location')
    updateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    member_information = {
        "id": id,
        "username": username,
        "password": password,
        "sex": sex,
        "phoneNum": phoneNum,
        "email": email,
        "birth": birth,
        "introduction": introduction,
        "location": location,
        "updateTime": updateTime
    }
    update_consumer(member_information)
    return JsonResponse.success().to_dict()
