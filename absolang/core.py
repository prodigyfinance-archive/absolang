# -*- coding: utf-8 -*-

""" Core utilities. """

import json


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
