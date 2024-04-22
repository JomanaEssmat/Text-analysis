import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

nltk.download('stopwords')
nltk.download('punkt')

def preprocess_text(text):

    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    return text

with open("random_paragraphs.txt", "r") as file:
    text = file.read()

text = preprocess_text(text)

tokens = nltk.word_tokenize(text)

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

word_freq = Counter(filtered_tokens)

for word, freq in word_freq.items():
    print(f"{word}: {freq}")
