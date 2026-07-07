def predict_sentiment(text):
    text = text.lower()

    if "good" in text or "happy" in text or "great" in text:
        return "Positive"
    elif "bad" in text or "sad" in text or "hate" in text:
        return "Negative"
    else:
        return "Neutral"
