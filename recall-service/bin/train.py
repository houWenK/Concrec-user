from pyspark.sql import SparkSession
from recall.dataset.anime import spark_load_ratings
from recall.model import item2vec
from recall.dataset import embedding
from recall.model.seq import simple_seq, deepwalk_seq
import os
os.environ['PYSPARK_PYTHON'] = "E:\\soft\\Anaconda3\\envs\\Concrec\\python.exe"
spark = SparkSession \
    .builder \
    .appName("concrec-recall") \
    .getOrCreate()

rating_df = spark_load_ratings(spark)
anime_seq = deepwalk_seq.build_seq(rating_df, spark)
print('sample gen done.')
(item_emb_df, user_emb_df) = item2vec.train_item2vec(anime_seq, rating_df)
print('embedding trained.')

item_vec = item_emb_df.collect()
item_emb = {}
for row in item_vec:
    item_emb[row.word] = row.vector.toArray()

embedding.save_item_embedding(item_emb)
print(f'{len(item_emb)} Item embedding saved to redis.')

user_vec = user_emb_df.collect()
user_emb = {}
for row in user_vec:
    user_emb[row.user_id] = row.user_emb

embedding.save_user_embedding(user_emb)
print(f'{len(user_emb)} User embedding saved to redis.')

print('item2vec embedding done.')
