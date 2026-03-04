def retrieve_chunks(vector_store, query):

    docs = vector_store.similarity_search(
        query,
        k=3
    )

    return docs