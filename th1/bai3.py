from bai2 import tokenizer

if __name__ == "__main__":
    text = "Xin chào các bạn. Chúc các bạn học tốt Python."
    tokens = tokenizer(text)
    key = set(tokens)
    td = {k: 0 for k in key}
    for t in tokens:
        td[t] += 1
    print("Tần số xuất hiện của các từ:")
    for k, v in td.items():
        print(f"{k}: {v}")