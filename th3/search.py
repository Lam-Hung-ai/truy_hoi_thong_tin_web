from typing import Any
from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir

from sys import path
path.append("..")
from retrival_web.logic import AND, OR, AND_NOT

def update_td(td: dict[str, int], doc: Any) -> dict[str, int]:
    """Cập nhật từ điển td với doc mới.
    
    Args:
        td: Từ điển hiện tại.
        doc: Tài liệu mới cần thêm vào từ điển.
    
    Returns:
        Từ điển đã được cập nhật.
    """
    
    for i in range(len(doc)):
        if doc[i]['path'] not in td:
            td[doc[i]['path']] = len(td)
    return td

def map_results(results: Any, td: dict[str, int]) -> list[int]:
    """Lấy các tài liệu trong results và ánh xạ chúng với từ điển td.
    
    Args:
        results: Kết quả tìm kiếm.
        td: Từ điển ánh xạ số thứ tự với đường dẫn tài liệu.
    
    Returns:
        Từ điển đã được cập nhật.
    """
    arr: list[int] = []
    for i in range(len(results)):
        arr.append(td[results[i]['path']])
    return arr

def reverse_map_results(arr: list[int], td: dict[str, int]) -> list[str]:
    """Lấy các số thứ tự trong arr và ánh xạ chúng với từ điển td để lấy đường dẫn tài liệu.
    
    Args:
        arr: Mảng các số thứ tự.
        td: Từ điển ánh xạ số thứ tự với đường dẫn tài liệu.
    
    Returns:
        Mảng các đường dẫn tài liệu.
    """
    rev_td = {v: k for k, v in td.items()}
    paths: list[str] = []
    for i in arr:
        paths.append(rev_td[i])
    return paths

# Mở chỉ mục đã xây dựng trước đây
ix = open_dir('indexdir')
# Yêu cầu người dùng nhập vào câu truy vấn
query_str = input('Enter a query: ')
or_str = input("Enter relevant keywords(split by space) if not just press Enter: ")
not_str = input("Enter irrelevant keywords(split by space) if not just press Enter: ")
td: dict[str, int] = {}

# Chấm điểm các tài liệu theo số lần các từ truy vấn xuất hiện
# trong mỗi tài liệu (weighting=scoring.Frequency).
with ix.searcher(weighting=scoring.Frequency) as searcher:
    # Tìm kiếm trong trường content
    query = QueryParser('content', ix.schema).parse(query_str)
    results_query = searcher.search(query)
    td = update_td(td, results_query)
    query_arr = map_results(results_query, td)
    
    # Lọc kết quả theo từ khóa "or"
    if or_str:
        or_keywords = or_str.split()
        for keyword in or_keywords:
            query = QueryParser('content', ix.schema).parse(keyword)
            results = searcher.search(query)
            td = update_td(td, results)
            or_arr = map_results(results, td)
            query_arr = OR(query_arr, or_arr)

    # Lọc kết quả theo từ khóa "not"
    if not_str:
        not_keywords = not_str.split()
        for keyword in not_keywords:
            query = QueryParser('content', ix.schema).parse(keyword)
            results = searcher.search(query)
            td = update_td(td, results)
            not_arr = map_results(results, td)
            query_arr = AND_NOT(query_arr, not_arr)

    # Số kết quả trả về
    num_results = len(query_arr)
    if (num_results == 0):
        print('No results')
    else:
        td_reversed = reverse_map_results(query_arr, td)	
        # Hiện các kết quả, mỗi dòng gồm số thứ tự, tiêu đề, điểm số
        for idx, path in enumerate(td_reversed):
            doc = searcher.document(path=path)
            print(f"{idx + 1} - {doc['title']} ({results_query.score(idx)})")
        # for i in range(len(results)):
        #     print(i + 1, '-', results[i]['title'], '(' + str(results[i].score) + ')')
        
        # Yêu cầu người dùng chọn kết quả muốn xem chi tiết
        k = int(input('Which result do you want to show? '))
        
        # Mở và hiển thị nội dung file tương ứng với kết quả đã chọn
        fp = open(td_reversed[k - 1], 'r', encoding='utf-8')
        print()
        print(fp.read())    
        fp.close()
