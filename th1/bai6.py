import os
from bai2 import tokenizer, find_word

docs_path = "/media/lamhung/D/code/python/truy_hoi_thong_tin_web/th1/docs"
docs_files = os.listdir(docs_path)
docs = []
map_id_title = {}
for i, file in enumerate(docs_files):
    with open(os.path.join(docs_path, file), "r", encoding="utf-8") as f:
        docs.append(f.read())
        map_id_title[i] = file
print(f"Số tài liệu: {len(docs)}")
# hiện ra màn hình chỉ số id và tiêu đề tài liệu
print("Danh sách tài liệu:")
for k, v in map_id_title.items():
    print(f"{k}: {v}")

tokens_list = [tokenizer(doc) for doc in docs]
td = {k: [] for t in tokens_list for k in set(t)}

for key in td.keys():
    for i in range(len(tokens_list)):
        if find_word(tokens_list[i], key):
            td[key].append(i)

print("Nhập từ khóa tìm kiếm:")
keyword = input().strip()
keyword = tokenizer(keyword)[0]

result = []
if keyword in td:
    doc_ids = td[keyword]
    print(f"Từ '{keyword}' xuất hiện trong {len(doc_ids)} tài liệu:")
    for doc_id in doc_ids:
        print(f"{doc_id} - {map_id_title[doc_id]}")
        result.append(doc_id)

    print("Nhập id tài liệu bạn muốn xem (hoặc nhập -1 để thoát):")
    doc_id = int(input().strip())
    if doc_id == -1:
        exit(0)
    if doc_id in result:
        print(f"Nội dung tài liệu {doc_id} - {map_id_title[doc_id]}:")
        print(docs[doc_id])
    else:
        print("Tài liệu không hợp lệ.")
else:
    print(f"Từ '{keyword}' không xuất hiện trong tài liệu nào.")


    