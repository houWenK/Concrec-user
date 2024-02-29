from recall.strategy.recall_strategy import RecallStrategy
import recall.dataset.anime as dataset
from random import sample
from recall.config import config


class HighRatingStrategy(RecallStrategy):
    def __init__(self):
        super().__init__()
        self.build_pool()

    def name(self):
        return 'HighRating'

    def build_pool(self):
        (anime_df, _) = dataset.load_dataset()
        sorted_df = anime_df.sort_values(by=['ave_rating_minmax'], ascending=False)
        self.pool = sorted_df.iloc[:500].index.to_list()
        print(f'{self.name()} pool loaded.')

    def recall(self, context, n):
        if config['high_rating']['shuffle_sample']:
            return sample(self.pool, n)

        return self.pool[:n]
