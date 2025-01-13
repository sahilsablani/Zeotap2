def search_docs(docs, query):
    """
    Searches the documentation for the given query.
    """
    if query.lower() in docs.lower():
        return f"Found relevant information for your query: '{query}'"
    return "Sorry, no relevant information found in the documentation for your query."
