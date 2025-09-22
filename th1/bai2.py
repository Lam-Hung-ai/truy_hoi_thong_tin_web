from pyvi import ViTokenizer
import string

def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans('', '', string.punctuation))

def tokenizer(text: str) -> list[str]:
    text = remove_punctuation(text)
    tokens: list[str] = ViTokenizer.tokenize(text).split()
    tokens = [token.strip().lower() for token in tokens]
    return tokens

def find_word(tokens: list[str], word: str) -> bool:
    word = tokenizer(word)[0]
    return word in tokens

if __name__ == "__main__":
    sample_text = "Việt Nam là một quốc gia nằm ở khu vực Đông Nam Á, trên bán đảo Đông Dương, với bờ biển dài hơn 3.260 km tiếp giáp Biển Đông"
    print("Văn bản mẫu:")
    print(sample_text)
    tokens = tokenizer(sample_text)
    print("Danh sách từ đã tách:")
    print(tokens)
    print(f"Kết quả tìm kiếm từ 'Việt Nam': {find_word(tokens, 'Việt Nam')}")
    print(f"Kết quả tìm kiếm từ 'Mỹ': {find_word(tokens, 'Mỹ')}")