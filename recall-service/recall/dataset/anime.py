from posixpath import join
import pandas as pd
from os.path import join

from pyspark.sql.session import SparkSession
from recall.config import config
from functools import lru_cache

@lru_cache()
def load_dataset():
    anime_df = pd.read_csv(join(config['dataset_path'], 'anime_feature.csv'), index_col='anime_id')
    rating_df = pd.read_csv(join(config['dataset_path'], 'rating.csv'))

    return (anime_df, rating_df)

@lru_cache()
def spark_load_ratings(spark: SparkSession):
    return spark.read.csv(join(config['dataset_path'], 'rating.csv'), header=True, inferSchema=True)
