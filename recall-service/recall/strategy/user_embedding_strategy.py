from recall.context import Context
from typing import List
from recall.strategy.recall_strategy import RecallStrategy
from recall.model.lsh import get_item_lsh
from recall.dataset.embedding import get_one_user_embedding, get_all_item_embedding


class UserEmbeddingStrategy(RecallStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.lsh = get_item_lsh()

    def name(self):
        return 'UserEmbedding'

    def recall(self, context: Context, n) -> List[int]:
        if context.user_id is None:
            return []

        user_emb = get_one_user_embedding(context.user_id)
        if user_emb is None:
            print(f'user {context.user_id} emb not found.')
            return []

        print(f'user {context.user_id} emb: {user_emb}')
        return self.lsh.search(user_emb, n=n)
