import os

config = {
    'dataset_path': os.environ['DATASET_PATH'],
    'deepwalk': {
        'sample_length': 10,
        'sample_count': 100 * 1000
    },
    'item2vec': {
        'vector_size': 5,
        'max_iter': 5,
        'window_size': 10
    },
    'redis': {
        'host': '192.168.200.141',
        'port': 6379,
        'db': 0
    },
    'most_rating': {
        'shuffle_sample': True
    },
    'high_rating': {
        'shuffle_sample': True
    }
}
