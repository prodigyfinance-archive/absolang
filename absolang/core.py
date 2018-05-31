# -*- coding: utf-8 -*-

""" Core utilities. """

import json
import spacy


class Dictionary:
    """ Dictionary of words. """

    def __init__(self, metadata, words):
        self.metadata = metadata
        self.words = words

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
    doc = nlp(text)
    for entity in doc.ents:
        print(entity.text, entity.label_)
