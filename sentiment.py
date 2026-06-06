from textblob import TextBlob

def predict_sentiment(text):

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0.1:
        label = "positive"
    elif polarity < -0.1:
        label = "negative"
    else:
        label = "neutral"

    score = round(abs(polarity) * 100, 2)

    return {
        "label": label,
        "score": score
    }