import nltk
tokenized = nltk.word_tokenize("Vietnam is a Southeast Asian country with a rich history, diverse culture, and stunning natural beauty")
print(tokenized)

posterstem = nltk.PorterStemmer()

tk = [posterstem.stem(t) for t in tokenized]
print(tk)