from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
from pyvi import ViTokenizer
import os
import string

def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans('', '', string.punctuation))

def tokenizer(text: str) -> list[str]:
    text = remove_punctuation(text)
    tokens: list[str] = ViTokenizer.tokenize(text).split()
    tokens = [token.strip().lower() for token in tokens]
    return tokens


titles = [
    "Lịch sử trí tuệ nhân tạo",
    "Giới thiệu về học máy",
    "Những tiến bộ trong học sâu",
    "Xử lý ngôn ngữ tự nhiên",
    "Ứng dụng của thị giác máy tính",
    "Robot và tự động hóa",
    "AI trong y tế",
    "AI trong tài chính",
    "Đạo đức của trí tuệ nhân tạo",
    "Tương lai của AI"
]

contents = [
    "Trí tuệ nhân tạo có lịch sử lâu đời, bắt đầu từ những năm 1950 với nhiều nghiên cứu quan trọng đặt nền móng cho lĩnh vực này.",
    "Học máy là một nhánh của trí tuệ nhân tạo tập trung vào việc xây dựng các thuật toán có khả năng học hỏi từ dữ liệu và cải thiện theo thời gian.",
    "Học sâu là một phương pháp học máy dựa trên mạng nơ-ron nhân tạo nhiều lớp, đã mang lại những thành tựu vượt bậc trong thập kỷ qua.",
    "Xử lý ngôn ngữ tự nhiên giúp máy tính hiểu và phân tích ngôn ngữ của con người, từ văn bản cho đến giọng nói.",
    "Thị giác máy tính cho phép máy móc nhận diện, phân loại và phân tích dữ liệu hình ảnh cũng như video một cách chính xác.",
    "Ngành robot hiện đại kết hợp trí tuệ nhân tạo để tạo ra những cỗ máy có thể tự động thực hiện nhiều công việc phức tạp thay cho con người.",
    "Trong lĩnh vực y tế, AI được ứng dụng để chẩn đoán bệnh, phát hiện thuốc mới và hỗ trợ theo dõi sức khỏe bệnh nhân.",
    "Trong tài chính, trí tuệ nhân tạo được dùng để phát hiện gian lận, quản lý rủi ro và tối ưu hóa giao dịch.",
    "Các vấn đề đạo đức của AI bao gồm sự thiên vị trong dữ liệu, quyền riêng tư và tính minh bạch trong các quyết định tự động.",
    "Tương lai của AI được kỳ vọng sẽ tiến gần hơn tới trí tuệ nhân tạo tổng quát và sự hợp tác hiệu quả giữa con người và máy móc."
]

contents_processed = [ tokenizer(content) for content in contents ]

storage_dir = "documents_storage"
if not os.path.exists(storage_dir):
    os.mkdir(storage_dir)

schema = Schema(
    doc_id=ID(stored=True),       
    title=TEXT(stored=True),
    content=TEXT
)

ix = create_in(storage_dir, schema)
writer = ix.writer()

for i in range(len(titles)):
    writer.add_document(
        doc_id=str(i),            
        title=titles[i],
        content=contents_processed[i]
    )

writer.commit()

query_text = input("Nhập câu truy vấn: ")

with ix.searcher() as searcher:
    query_text = tokenizer(query_text)[0]
    query = QueryParser("content", ix.schema).parse(query_text)
    results = searcher.search(query)

    print("Số kết quả:", len(results))
    for idx, hit in enumerate(results):
        print(f"{idx+1}. {hit['title']}")

    if len(results) > 0:
        choice = int(input("Chọn số thứ tự của kết quả: ")) - 1
        if 0 <= choice < len(results):
            doc_id = int(results[choice]['doc_id'])
            
            print("\nNội dung tài liệu:")
            print(contents[doc_id])
        else:
            print("Số thứ tự không hợp lệ.")
