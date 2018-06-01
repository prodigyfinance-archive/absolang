# -*- coding: utf-8 -*-

""" Core utilities. """

import json
import os

import spacy

nlp = spacy.load('en_core_web_sm')


class Dictionary:
    """ Dictionary of words. """

    def __init__(self, metadata, words):
        self.metadata = metadata
        self.words = words

    @classmethod
    def load_by_name(cls, name):
        return cls.load(os.path.join(
            os.path.dirname(__file__), "dictionaries", name + ".json"))

    @classmethod
    def load(cls, path):
        data = json.load(open(path, encoding="utf-8"))
        return cls(metadata=data["metadata"], words=data["words"])

    def save(self, path):
        json.dump({
            "metadata": self.metadata,
            "words": self.words,
        }, open(path, mode="w", encoding="utf-8"), indent=2)


def absolutist_index(text):
    dictionary = Dictionary.load_by_name("absolute-19")
    wordset = set(dictionary.words)
    doc = nlp(text)
    words = 0
    score = 0
    prev = None
    for token in doc:
        if token.is_alpha:
            words += 1
        if token.lemma_ in wordset:
            # ignore absolutist words if the previous word is a
            # negation (e.g. "not"), an adverbial modifier (e.g. "almost"),
            # or an interjection (e.g. "Hello everyone!")
            if ((prev is None) or not (
                    prev.dep_ in ("neg", "advmod", "intj"))):
                score += 1
        prev = token
    return score / float(words)
