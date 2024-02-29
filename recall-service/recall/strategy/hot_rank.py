from recall.strategy.recall_strategy import RecallStrategy
import recall.dataset.anime as dataset
from random import sample
from recall.config import config


class HotRank(RecallStrategy):
    def __init__(self):
        super().__init__()
        self.build_pool()

    def name(self):
        return 'HotRating'

    def build_pool(self):
        (anime_df, _) = dataset.load_dataset()
        sorted_df = anime_df.sort_values(by=['rating_count_standard'], ascending=False)
        self.hot_rating = sorted_df['rating_count_standard'].iloc[:10].values.tolist()
        self.pool = sorted_df.iloc[:10].index.to_list()
        # print(self.pool)
        # print(self.hot_rating)
        # self.result = {}
        # for i in range(0, len(self.pool)):
        #     self.result[self.pool[i]] = self.hot_rating[i]
        self.result=[]
        for k, v in zip(self.pool,self.hot_rating):
            index={}
            index['anime_id']=k
            index['ab:hot']=v
            self.result.append(index)
        print(f'{self.name()} pool loaded.')

    def recall(self, context, n):
        return self.result
