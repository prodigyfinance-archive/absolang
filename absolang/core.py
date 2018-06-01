# -*- coding: utf-8 -*-

""" Core utilities. """

import json
import os

import spacy

nlp = spacy.load('en_core_web_sm')


class Dictionary:
    """ Dictionary of words.

        :param dict metadata:
            Metadata about the words.
        :param list words:
            List of words in the dictionary.
    """
    def __init__(self, metadata, words):
        self.metadata = metadata
        self.words = words

    @classmethod
    def load_by_name(cls, name):
        """ Load a dictionary by name from absolang.dictionaries.
        """
        return cls.load(os.path.join(
            os.path.dirname(__file__), "dictionaries", name + ".json"))

    @classmethod
    def load(cls, path):
        """ Load a dictionary from a path.
        """
        data = json.load(open(path, encoding="utf-8"))
        return cls(metadata=data["metadata"], words=data["words"])

    def save(self, path):
        """ Write a dictionary to a path.
        """
        json.dump({
            "metadata": self.metadata,
            "words": self.words,
        }, open(path, mode="w", encoding="utf-8"), indent=2)


def absolutist_index(text):
    """ Return the fraction of absolute words in the given text.

        :param str text:
            The text to examine.
        :return float:
            The fraction of words in the text that are absolutist.
    """
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


def absolutist(text):
    """ Return True if the percentage of absolute words in the text
        is greated than 1.1 percent.

        :param str text:
            Text to check for absolute language.
        :return bool:
            True if the percentage of absolute words in the text
            is greated than 1.1 percent.
    """
    return absolutist_index(text) >= 0.011
