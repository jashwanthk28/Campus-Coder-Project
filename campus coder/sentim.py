import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
def analyze_sentiment(text):
    # Initializing the sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Getting the sentiment polarity scores
    sentiment_scores = sid.polarity_scores(text)

    # Determining the sentiment based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == "__main__":
    text_to_analyze = "I love this product! It's amazing."
    sentiment = analyze_sentiment(text_to_analyze)

    print(f"Text: {text_to_analyze}")
    print(f"Sentiment: {sentiment}")