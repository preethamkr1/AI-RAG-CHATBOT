from rank_bm25 import BM25Okapi

bm25_index = None
bm25_chunks = []


def build_bm25_index(chunks):
    global bm25_index, bm25_chunks

    bm25_chunks = chunks

    tokenized_chunks = [
        chunk.lower().split()
        for chunk in chunks
    ]

    bm25_index = BM25Okapi(tokenized_chunks)


def search_bm25(question, top_k=5):
    global bm25_index, bm25_chunks

    if bm25_index is None:
        return []

    tokenized_query = question.lower().split()

    scores = bm25_index.get_scores(
        tokenized_query
    )

    ranked_indices = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )[:top_k]

    return [
        bm25_chunks[i]
        for i in ranked_indices
    ]