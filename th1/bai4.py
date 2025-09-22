from bai2 import tokenizer, find_word

if __name__ == "__main__":
    # 4 tài liệu liên quan chủ đề ai 
    document = [
        "Trí tuệ nhân tạo (AI) là một lĩnh vực nghiên cứu nhằm tạo ra các hệ thống máy tính có khả năng thực hiện các nhiệm vụ mà thường đòi hỏi trí tuệ con người, như nhận diện giọng nói, học hỏi, lập kế hoạch và giải quyết vấn đề.",
        "Học máy (Machine Learning) là một nhánh của AI tập trung vào việc phát triển các thuật toán và mô hình cho phép máy tính học từ dữ liệu và cải thiện hiệu suất theo thời gian mà không cần lập trình rõ ràng.",
        "Học sâu (Deep Learning) là một phần của học máy sử dụng các mạng nơ-ron nhân tạo với nhiều lớp để mô hình hóa các mối quan hệ phức tạp trong dữ liệu, đặc biệt trong các lĩnh vực như nhận diện hình ảnh và xử lý ngôn ngữ tự nhiên.",
        "Xử lý ngôn ngữ tự nhiên (NLP) là một lĩnh vực của AI tập trung vào việc giúp máy tính hiểu, diễn giải và tạo ra ngôn ngữ con người, bao gồm cả văn bản và giọng nói."  
    ]

    tokens_list = [tokenizer(doc) for doc in document]
    td = {k: [] for t in tokens_list for k in set(t)}

    for key in td.keys():
        for i in range(len(tokens_list)):
            if find_word(tokens_list[i], key):
                td[key].append(i)

    print("Ma trận tần số xuất hiện từ trong các tài liệu:")
    print(f"{'Từ':<15}", end="")
    for i in range(len(document)):
        print(f"Doc{i+1:<5}", end="")
    print()
    for k, v in td.items():
        print(f"{k:<15}", end="")
        for i in range(len(document)):
            if i in v:
                print(f"{1:<8}", end="")
            else:
                print(f"{0:<8}", end="")
        print()