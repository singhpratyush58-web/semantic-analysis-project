from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

def predict_sentiment(text):

    result = classifier(text)[0]

    return {
        "label": result["label"],
        "score": round(result["score"]*100,2)
    }