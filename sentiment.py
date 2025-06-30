from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

if __name__ == "__main__":
    sentences = [
        "I love this product!",
        "This is terrible.",
        "I'm feeling okay about this.",
        "Absolutely fantastic experience.",
        "Not happy with the results."
    ]

    for sentence in sentences:
        score = analyze_sentiment(sentence)
        print(f"'{sentence}' → Sentiment Score: {score}")
