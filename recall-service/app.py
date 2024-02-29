from recall.context import Context
from flask import Flask, jsonify, request
from recall.service import recall_service


app = Flask('recall-service')



@app.route("/")
def get_anime():
    user_id = request.args.get('user_id', type=int)
    print(f'Calling user {user_id}...')
    context = Context(user_id)
    res = recall_service.anime_recall(context)
    print(res)
    return jsonify(res)

@app.route("/sim")
def get_sim_anime():
    anime_id = request.args.get('anime_id', type=int)
    print(anime_id)
    if anime_id is None:
        return 'bad anime id', 400

    context = Context(None, anime_id)
    res = recall_service.similar_animes(context)
    return jsonify(res)

@app.route("/hot")
def get_hot_anime():
    context = Context()
    res=recall_service.hot_rank(context)
    return  jsonify(res)

@app.route("/high")
def get_high_anime():
    context = Context()
    res=recall_service.high_rank(context)
    return  jsonify(res)