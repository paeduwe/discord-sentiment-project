from transformers import pipeline
from src.db.models import SessionLocal, Message

# load model once (important)
classifier = pipeline("sentiment-analysis")

def analyze_messages():
    session = SessionLocal()

    try:
        # get messages not analyzed yet
        messages = session.query(Message).filter(
            Message.sentiment_score == None
        ).all()

        print(f"Found {len(messages)} messages to analyze")

        for msg in messages:
            result = classifier(msg.text)[0]#edw einai to 0 tou classifier
                                            #oxi tou msg.text

            label = result["label"]
            score = result["score"]

            text = msg.text.lower()

            if (# auto einai gia na mh vazei ba8mo sta garbage texts
                not any(c.isalpha() for c in text) or
                not any(c in "aeiou" for c in text)
            ):
                msg.sentiment_score = 0
                continue

            # convert to numeric score
            if label == "POSITIVE":
                msg.sentiment_score = score
            else:
                msg.sentiment_score = -score

        session.commit()
        print("Sentiment updated")

    except Exception as e:
        session.rollback()
        print("ERROR:", e)

    finally:
        session.close()


if __name__ == "__main__":
    analyze_messages()