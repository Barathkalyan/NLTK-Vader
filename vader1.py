from nltk.sentiment import SentimentIntensityAnalyzer

sia=SentimentIntensityAnalayzer()
sentences = ["I love this!", "I hate this!", "Oh great, more work...", "I feel okay today."]
for text in sentences:
    print(f"Sentence: {text}")
    print(sia.polarity_scores(text))



