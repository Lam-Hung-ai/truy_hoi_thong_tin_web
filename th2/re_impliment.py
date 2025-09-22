from whoosh.index import create_in
from whoosh.fields import *
import os

schema = Schema(title=TEXT(stored=True), path=ID(stored=True),
content=TEXT)
indexdir = "indexdir"

if not os.path.exists(indexdir):
    os.mkdir(indexdir)
# Đảm bảo thư mục "indexdir" tồn tại trong thư mục hiện hành
ix = create_in(indexdir, schema)
writer = ix.writer()
writer.add_document(title="First document", path="/a",
content="This is the first document we've added!")
writer.add_document(title="Second document", path="/b",
content="The second one is even more interesting!")
writer.commit()
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("first")
    results = searcher.search(query)
    print("Number of results:", len(results))
    if results:
        # Use the Hit object's mapping access instead of dict(...) to avoid type errors
        print(results[0]["title"])