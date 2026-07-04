from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def preprocess_text(text):
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    tokens = word_tokenize(text)

    cleaned = []

    for token in tokens:
        token = token.lower()

        if token.isalpha() and token not in stop_words:
            cleaned.append(
                lemmatizer.lemmatize(token)
            )

    return cleaned