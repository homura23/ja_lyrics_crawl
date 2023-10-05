import pickle
import re

def clean_text(text):
    # Remove non-Japanese characters except for '\n'
    cleaned_text = re.sub(r'[^\nぁ-んァ-ヶ一-龯]', '', text)
    cleaned_text = re.sub(r'([^。！？\n]+[。！？])', r'\1\n', cleaned_text)  # Add '\n' after each sentence
    cleaned_text = cleaned_text.replace(' ', '')  # Remove whitespace
    cleaned_text += '\n'  # Add '\n' at the end of the lyrics
    return cleaned_text

# Read the input .pkl file
with open('out2.pkl', 'rb') as f:
    data = pickle.load(f)

# Clean each song's lyrics
for song in data:
    cleaned_lyric = clean_text(song['lyric'])
    song['lyric'] = cleaned_lyric

# Save the cleaned data to the output .pkl file
with open('lyrics_only_ja.pkl', 'wb') as f:
    pickle.dump(data, f)

