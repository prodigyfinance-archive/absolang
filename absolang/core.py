# -*- coding: utf-8 -*-

""" Core utilities. """

import json
import os

import spacy


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
    nlp = spacy.load('en_core_web_sm')
    d = Dictionary.load_by_name("absolute-19")
    wordset = set(d.words)
    doc = nlp(text)
    score = 0
    for token in doc:
        if token.lemma_ in wordset:
            score += 1
    return score
