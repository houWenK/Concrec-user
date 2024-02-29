import os

config = {
    'rank_endpoint': os.environ['RANK_ENDPOINT'],
    'recall_endpoint': os.environ['RECALL_ENDPOINT'],
    'dataset_path': os.environ['DATASET_PATH']
}
