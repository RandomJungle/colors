import spacy
from file_utils import load_emoji_data
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict, List


def test_similarity(emoji_data: Dict, sentence: str) -> Dict:
    nlp = spacy.load('en_core_web_lg')
    vector = nlp(sentence).vector
    results = {}
    for key, value in emoji_data.items():
        emoji_vector = value['vector']
        similarity = cosine_similarity(vector.reshape(1, -1), emoji_vector.reshape(1, -1))
        results[key] = similarity
    sorted_results = {k: v for k, v in reversed(sorted(results.items(), key=lambda item: item[1]))}
    return sorted_results


def sample_best_similarities(emoji_data: Dict, sentence: str, sample_size: int) -> None:
    similarities = test_similarity(emoji_data, sentence)
    samples = list(similarities.keys())[:sample_size]
    print(f"\"{sentence}\" is most similar to : {samples}\n")


def test():
    dataset = load_emoji_data()
    sentences = [
        "a red falcon",
        "the story starts on the hills of hollywood",
        "the moon rises above the ocean",
        "a fresh salad in the summer",
        "dancing in the moonlight"
    ]
    for sent in sentences:
        sample_best_similarities(dataset, sent, 5)


def noun_chunks2emojis(emoji_data: Dict, text: str) -> List:
    output_text = []
    nlp = spacy.load('en_core_web_lg')
    for sent in nlp(text).sents:
        for noun_chunk in sent.noun_chunks:
            vector = noun_chunk.vector
            results = {}
            for key, value in emoji_data.items():
                emoji_vector = value['vector']
                similarity = cosine_similarity(vector.reshape(1, -1), emoji_vector.reshape(1, -1))
                results[key] = similarity
            output_text.append(tuple([noun_chunk.text, str(max(results, key=lambda key: results[key]))]))
    return output_text


def verb_chunks2emojis(emoji_data: Dict, text: str) -> List:
    output_text = []
    nlp = spacy.load('en_core_web_lg')
    doc = nlp(text)
    for token in doc:
        if token.head == token:
            span = doc[token.left_edge.i:token.right_edge.i + 1]
            if span:
                vector = span.vector
                results = {}
                for key, value in emoji_data.items():
                    emoji_vector = value['vector']
                    similarity = cosine_similarity(vector.reshape(1, -1), emoji_vector.reshape(1, -1))
                    results[key] = similarity
                output_text.append(tuple([span.text, str(max(results, key=lambda key: results[key]))]))
    return output_text


def sentences2emojis(emoji_data: Dict, text: str) -> List:
    output_text = []
    nlp = spacy.load('en_core_web_lg')
    for sent in nlp(text).sents:
        vector = sent.vector
        results = {}
        for key, value in emoji_data.items():
            emoji_vector = value['vector']
            similarity = cosine_similarity(vector.reshape(1, -1), emoji_vector.reshape(1, -1))
            results[key] = similarity
        output_text.append(
            tuple([sent.text, str(max(results, key=lambda key: results[key]))]))
    return output_text


def window2emojis(emoji_data: Dict, text: str, window_size: int = 5) -> List:
    output_text = []
    nlp = spacy.load('en_core_web_lg')
    for sent in nlp(text).sents:
        for i in range(0, len(sent), window_size):
            chunk = sent[i:i+window_size]
            vector = chunk.vector
            results = {}
            for key, value in emoji_data.items():
                emoji_vector = value['vector']
                similarity = cosine_similarity(vector.reshape(1, -1), emoji_vector.reshape(1, -1))
                results[key] = similarity
            output_text.append(tuple([chunk.text, str(max(results, key=lambda key: results[key]))]))
    return output_text


if __name__ == '__main__':
    dataset = load_emoji_data()
    text_to_convert = (
        "After winning a trip on the RMS Titanic during a dockside card game, American Jack Dawson "
        "spots the society girl Rose DeWitt Bukater who is on her way to Philadelphia to marry her "
        "rich snob fiancé Caledon Hockley. Rose feels helplessly trapped by her situation and makes"
        " her way to the aft deck and thinks of suicide until she is rescued by Jack. Cal is theref"
        "ore obliged to invite Jack to dine at their first-class table where he suffers through the"
        " slights of his snobbish hosts. In return, he spirits Rose off to third-class for an eveni"
        "ng of dancing, giving her the time of her life. Deciding to forsake her intended future al"
        "l together, Rose asks Jack, who has made his living making sketches on the streets of Pari"
        "s, to draw her in the nude wearing the invaluable blue diamond Cal has given her. Cal find"
        "s out and has Jack locked away. Soon afterwards, the ship hits an iceberg and Rose must fi"
        "nd Jack while both must run from Cal even as the ship sinks deeper into the freezing water.")
    emojis = verb_chunks2emojis(dataset, text_to_convert)
    for emo in emojis:
        print(f"{emo[0]} : {emo[1]}")

