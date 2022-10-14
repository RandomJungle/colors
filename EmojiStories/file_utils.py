import csv
from typing import Dict
import spacy


def read_emoji_data(data_path: str) -> Dict:
    emoji_data = {}
    with open(data_path, 'r+') as csv_emoji_file:
        csv_reader = csv.DictReader(csv_emoji_file, delimiter=',', quotechar='"')
        for row in csv_reader:
            emoji_data[row['emoji']] = row
    return emoji_data


def add_spacy_vectors_to_emoji_data(emoji_data: Dict) -> Dict:
    nlp = spacy.load("en_core_web_lg")
    for key, value in emoji_data.items():
        doc = nlp(value['name'])
        value.update({'vector': doc.vector})
    return emoji_data


def load_emoji_data(
        data_path: str = "/home/juliette/Projects/EmojiStories/data/emoji_df.csv") -> Dict:
    data = read_emoji_data(data_path)
    return add_spacy_vectors_to_emoji_data(data)
