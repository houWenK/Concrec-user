from pyspark.sql.dataframe import DataFrame
from pyspark.sql.functions import col, collect_list, udf
from collections import defaultdict
import numpy as np
from pyspark.sql.session import SparkSession
from recall.config import config
import dill
import os.path


rng = np.random.default_rng()

def build_seq(rating_df: DataFrame, spark: SparkSession):
    entrance_items = None
    entrance_probs = None
    transfer_probs = None

    if os.path.isfile('output/entrance_items.dill'):
        with open('output/entrance_items.dill', 'rb') as f:
            entrance_items = dill.load(f)
        with open('output/entrance_probs.dill', 'rb') as f:
            entrance_probs = dill.load(f)
        with open('output/transfer_probs.dill', 'rb') as f:
            transfer_probs = dill.load(f)
        print('loaded model from file')
    else:
        rating_df = rating_df.where('rating > 7')

        # 1. group by user_id
        watch_seq_df = rating_df \
            .groupBy('user_id') \
            .agg(
                collect_list(col('anime_id').cast('string')).alias('anime_ids') \
            )

        # 2. build anime matrix
        watch_seq = watch_seq_df.collect()
        watch_seq = [s['anime_ids'] for s in watch_seq]
        matrix = defaultdict(lambda: defaultdict(int))

        for i in range(len(watch_seq)):
            if i % 1000 == 0:
                print(f'matrix add seq {i}')
            seq = watch_seq[i]
            add_seq_to_matrix(seq, matrix)

        # 3. build prob transfer matrix
        transfer_probs = {k: get_transfer_prob(v) for k, v in matrix.items()}
        print(f'transfer probs built. {len(transfer_probs)} entrances')

        # 4. entrance
        counts = {k: sum(neibors.values()) for k, neibors in matrix.items()}
        entrance_items = list(transfer_probs.keys())
        total_count = sum(counts.values())
        entrance_probs = [counts[k] / total_count for k in entrance_items]
        print('entrance probs built.')

        with open('output/entrance_items.dill', 'wb') as f:
            dill.dump(entrance_items, f)
        with open('output/entrance_probs.dill', 'wb') as f:
            dill.dump(entrance_probs, f)
        with open('output/transfer_probs.dill', 'wb') as f:
            dill.dump(transfer_probs, f)
        print('saved model to file')

    # 5. do random walk
    n = config['deepwalk']['sample_count']
    length = config['deepwalk']['sample_length']
    samples = []
    for i in range(n):
        if i % 1000 == 0:
            print(f'random walk done {i}')
        s = one_random_walk(length, entrance_items, entrance_probs, transfer_probs)
        samples.append(s)
    print(f'Random walk generated {n} samples.')

    return spark.createDataFrame([[row] for row in samples], ['anime_ids'])

def add_seq_to_matrix(seq, m):
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            a = seq[i]
            b = seq[j]
            
            if a == b:
                continue
                
            m[a][b] += 1
            m[b][a] += 1


def get_transfer_prob(vs):
    neighbours = vs.keys()
    
    total_weight = sum(vs.values())
    
    probs = [vs[k]/total_weight for k in neighbours]
    try:
        assert( abs(1.0 - sum(probs)) < 0.000000001 )
    except:
        print(sum(probs))
        print(vs)
    
    return {
        'neighbours': list(neighbours),
        'probs': probs
    }

def one_random_walk(length, entrance_items, entrance_probs, transfer_probs):
    start_vertex = rng.choice(entrance_items, 1, p=entrance_probs)[0]
    path = [str(start_vertex)]
    
    curr_vertex = start_vertex
    for _ in range(length):
        if curr_vertex not in transfer_probs:
            print(f"bad vertex {curr_vertex}")
            break
            
        neighbours = transfer_probs[curr_vertex]['neighbours']
        trans_prob = transfer_probs[curr_vertex]['probs']
        
        try:
            next_vertex = rng.choice(neighbours, 1, p=trans_prob)[0]
            path.append(str(next_vertex))

            curr_vertex = next_vertex
        except Exception as e:
            print(curr_vertex)
            print(e)
            break
        
    return path
