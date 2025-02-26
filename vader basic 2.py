import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# Sample sentences
sentences = [
    "I love this product!",
    "This is the worst experience ever.",
    "It's okay, nothing special.",
]


for sentence in sentences:
    score = sia.polarity_scores(sentence)
    print(f"Sentence: {sentence}")
    print(f"Sentiment Score: {score['compound']}\n")
