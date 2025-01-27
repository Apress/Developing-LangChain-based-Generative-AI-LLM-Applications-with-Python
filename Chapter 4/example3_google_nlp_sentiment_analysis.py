from google.cloud import language_v1
import os

# Set up Google Cloud authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/service-account-file.json"

def analyze_text(text):
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    print(f"Text: {text}")
    print(f"Sentiment score: {sentiment.score}")
    print(f"Sentiment magnitude: {sentiment.magnitude}")

text = "Google Cloud AI services are powerful and easy to use."
analyze_text(text)
