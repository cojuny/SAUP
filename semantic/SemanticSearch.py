from sentence_transformers import SentenceTransformer, util
from typing import List

class SemanticSearch:

    def __init__(self) -> None:
        self.model = SentenceTransformer('msmarco-distilbert-base-v4')

    def search(self, query: str, target: List[str]) -> None:
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        for sentence in target:
            sentence_embedding = self.model.encode(sentence, convert_to_tensor=True)
            result = self.query_textual_similarity(query_embedding=query_embedding, sentence_embedding=sentence_embedding)
            print("\'{}\' -> \'{}\' similarity: {}".format(query, sentence, result))
            
    def query_textual_similarity(self, query_embedding, sentence_embedding) -> int:
        res = util.semantic_search(query_embedding, sentence_embedding)
        return round(res[0][0]['score'], 2) * 100
