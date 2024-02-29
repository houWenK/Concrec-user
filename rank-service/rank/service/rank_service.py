import rank.util.recall_service_client as recall_client
import rank.dataset.feature as dataset
from rank.model.mlp import RankModel
from rank.util.ab_test import bucketize
import numpy as np

model = RankModel()

def anime_rank(context):
    user_id = context.user_id
    recall_items = recall_client.get_recall(user_id)

    bucket = bucketize(user_id, 2)
    recall_res = [item['anime_id'] for item in recall_items]
    recall_mapping = {item['anime_id']: item for item in recall_items}

    rank_results = recall_res
    if bucket == 1:
        rank_results = mlp_rank(user_id, recall_res)

    return [{**recall_mapping[aid], 'ab:rank': bucket} for aid in rank_results]


def mlp_rank(user_id, recall_res):

    user_num_features = dataset.get_user_numeric_features(user_id)
    user_cat_features = dataset.get_user_categorical_features(user_id)

    if user_num_features is None or user_cat_features is None:
        return recall_res

    item_num_feature_list = [dataset.get_item_numeric_features(item_id) for item_id in recall_res]
    item_cat_feature_list = [dataset.get_item_categorical_features(item_id) for item_id in recall_res]

    # merge features
    model_inputs = __build_features(item_cat_feature_list,
                                    user_cat_features,
                                    item_num_feature_list,
                                    user_num_features    
    )

    scores = model.predict(model_inputs) 
    scores = [s[0] for s in scores]
    item_with_score = list(zip(recall_res, scores))
    item_with_score = sorted(item_with_score, key=lambda x: x[1], reverse=True)

    # remove items with score < 0.5
    item_with_score = list(filter(lambda x: x[1] >= 0.5, item_with_score))

    # print(item_with_score)

    return [x[0] for x in item_with_score]

def __get_item_nums(item_num):
    return np.nan_to_num(np.array([
        item_num['all_rating_min_max'],
        item_num['members_min_max'],
        item_num['aired_from_min_max'],
        item_num['aired_to_min_max']
    ]))

def __get_user_nums(user_num):
    return np.nan_to_num(np.array([
        user_num['user_rating_ave_min_max'],
        user_num['user_rating_std_min_max'],
        user_num['user_aired_from_ave_min_max'],
        user_num['user_aired_to_ave_min_max'],
    ]))

def __build_features(item_cats, user_cats, item_nums, user_nums):
    # x1: item cat
    x1 = [np.nan_to_num(np.array(item['genres_multihot'])) for item in item_cats]

    # x2: user cat
    x2 = [np.nan_to_num(np.array(user_cats['user_liked_genres_multihot'])) for _ in item_cats]

    # x3: item num
    x3 = [np.array(__get_item_nums(item_num)) for item_num in item_nums]

    # x4: user num
    x4 = [np.array(__get_user_nums(user_nums)) for _ in item_nums]

    return [ np.array(x1), np.array(x2), np.array(x3), np.array(x4) ]
