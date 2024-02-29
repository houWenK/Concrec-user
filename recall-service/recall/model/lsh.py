from typing import Dict, List
import numpy as np
import faiss
from recall.dataset.embedding import get_one_user_embedding, get_all_item_embedding


class LSH:
    def __init__(self, embeddings: Dict[int, List[float]]) -> None:
        items = embeddings.items()
        self.ids = [i[0] for i in items]
        vectors = [i[1] for i in items]

        d = len(vectors[0])
        print(f'd={d}')
        self.index = faiss.IndexLSH(d, 256)
        array_vec = np.asarray(vectors, dtype=np.float32)
        self.index.add(array_vec)
        assert(self.index.is_trained)
        print(f'LSH index added {self.index.ntotal} vectors')

    def search(self, vec: List[float], n=20) -> List[int]:
        """
        vec is a single embedding vector
        """
        print(vec)
        D, I = self.index.search(np.asarray([vec], dtype=np.float32), n)
        neighbors = I[0]
        res = [self.ids[i] for i in neighbors]

        print('D:')
        print(D)
        print('I:')
        print(I)
        print('neigh:')
        print(res)

        return res

__lsh__ = None

def get_item_lsh() -> LSH:
    global __lsh__

    if __lsh__ is None:
        item_embeddings = get_all_item_embedding()
        __lsh__ = LSH(item_embeddings)

    return __lsh__
