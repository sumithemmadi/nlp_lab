# -*- coding: utf-8 -*-
"""UI20CS21_NLP_LAB4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19xY0PsGz5dmMppX-L8IYH1BU0JKLs12_
"""

!pip install nltk numpy
!python -m nltk.downloader popular

import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('punkt')

synonyms = []
antonyms = []

for synset in wordnet.synsets("boy"):
    for l in synset.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print("synonyms = " ,set(synonyms))
print("antonyms = " ,set(antonyms))

word1 = wordnet.synset('girl.n.01')
word2 = wordnet.synset('boy.n.01')
print(word1.wup_similarity(word2)*100)

word = "play"

synsets = wordnet.synsets(word)

if synsets:
    for i, synset in enumerate(synsets):
        print(f"Synset {i + 1}:")
        print(f"Name: {synset.name()}")
        print(f"Definition: {synset.definition()}")
        print(f"Examples: {', '.join(synset.examples()) if synset.examples() else 'No examples available.'}")

        lemmas = synset.lemmas()
        print(f"Synonyms (lemmas): {', '.join(lemma.name() for lemma in lemmas)}")

        antonyms = []
        for lemma in lemmas:
            antonym = lemma.antonyms()
            if antonym:
                antonyms.append(antonym[0].name())
        print(f"Antonyms: {', '.join(antonyms) if antonyms else 'No antonyms available.'}")

        hypernyms = synset.hypernyms()
        print(f"Hypernyms: {', '.join(hypernym.name() for hypernym in hypernyms)}")

        hyponyms = synset.hyponyms()
        print(f"Hyponyms: {', '.join(hyponym.name() for hyponym in hyponyms)}")

        similarity_word = "sport"
        similarity_synset = wordnet.synsets(similarity_word)[0]
        path_similarity = synset.path_similarity(similarity_synset)
        print(f"Path Similarity with '{similarity_word}': {path_similarity}")

        print("=" * 50)

    lemmatizer = WordNetLemmatizer()
    lemma = lemmatizer.lemmatize(word, pos=wordnet.VERB)
    print(f"Lemmatized form of '{word}': {lemma}")
else:
    print(f"No synsets found for '{word}'")