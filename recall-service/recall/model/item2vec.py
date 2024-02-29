from typing import Tuple
from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, collect_list, udf
from pyspark.ml.feature import Word2Vec
from recall.config import config
import numpy as np


def train_item2vec(anime_seq: DataFrame, rating_df: DataFrame) -> Tuple[DataFrame, DataFrame]:
    """
    anime_seq: DataFrame with column 'anime_ids' which is sequence of anime ids

    return (item_emb_df, user_emb_df)
    - item_emb_df: word(anime_id), vector(embedding)
    - user_emb_df: user_id, user_emb
    """
    model_config = config['item2vec']
    word2vec = Word2Vec(vectorSize=model_config['vector_size'], maxIter=model_config['max_iter'], windowSize=model_config['window_size'])
    word2vec.setInputCol('anime_ids')
    word2vec.setOutputCol('anime_ids_vec')

    model = word2vec.fit(anime_seq)
    item_emb_df = model.getVectors()

    item_vec = model.getVectors().collect()
    item_emb = {}
    for item in item_vec:
        item_emb[item.word] = item.vector.toArray()

    @udf(returnType='array<float>')
    def build_user_emb(anime_seq):
        anime_embs = [item_emb[aid] if aid in item_emb else [] for aid in anime_seq]
        anime_embs = list(filter(lambda l: len(l) > 0, anime_embs))
        ret = np.mean(anime_embs, axis=0).tolist()

        return ret

    user_emb_df = rating_df \
        .where('rating > 7') \
        .groupBy('user_id') \
        .agg(
            collect_list(col('anime_id').cast('string')).alias('anime_ids')
        ) \
        .withColumn('user_emb', build_user_emb(col('anime_ids')))

    return (
        item_emb_df,
        user_emb_df.select('user_id', 'user_emb')
    )
