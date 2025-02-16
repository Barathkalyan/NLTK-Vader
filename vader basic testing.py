from nltk.sentiment import SentimentIntensityAnalyzer

# Sample code to analyse simple word sentence
sia=SentimentIntensityAnalyzer()
text="I am going to die. i am angry"
score=sia.polarity_scores(text)
print(score)