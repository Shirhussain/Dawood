import pandas as pd
from googletrans import Translator
import time
import random

def translate_to_persian(text, max_retries=5):
    translator = Translator()
    for attempt in range(max_retries):
        try:
            # Add a random delay between 1 and 3 seconds
            time.sleep(random.uniform(1, 3))
            translated = translator.translate(text, dest='fa').text
            print(f"Original: '{text}' -> Translated: '{translated}'")
            return translated
        except Exception as e:
            print(f"Translation error for '{text}': {e}")
            if attempt < max_retries - 1:
                print(f"Retrying... (Attempt {attempt + 2} of {max_retries})")
            else:
                print("Max retries reached. Keeping original text.")
                return text

# Read the CSV file
print("Reading CSV file...")
df = pd.read_csv('dev_sent_emo_dya.csv')

# Columns to translate
columns_to_translate = ['Utterance', 'Speaker', 'Emotion', 'Sentiment']

# Translate specified columns
for column in columns_to_translate:
    print(f"Translating {column}...")
    df[column] = df[column].apply(translate_to_persian)
    print(f"Finished translating {column}")

print("Saving translated CSV...")
# Save the translated CSV
df.to_csv('dev_sent_emo_dya_persian.csv', index=False)

print("Translation complete. Output saved to 'dev_sent_emo_dya_persian.csv'")