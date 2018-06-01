# -*- coding: utf-8 -*-

""" Tests for absolutist.code. """

from unittest import TestCase

from absolang.core import absolutist_index


class AbsoluteIndexTests(TestCase):

    def check_index(self, text, value):
        self.assertEqual(absolutist_index(text), value)

    def test_no_absolutist_words(self):
        self.check_index("The bigger dog is running.", 0 / 5.)

    def test_one_absolutist_word(self):
        self.check_index("He was completely bowled over.", 1 / 5.)

    def test_negation_ignored(self):
        self.check_index("He was not completely bowled over.", 0 / 6.)

    def test_quantifier_ignored(self):
        self.check_index("He was almost completely bowled over.", 0 / 6.)

    def test_salutation_ignored(self):
        self.check_index("Hello everyone.", 0 / 2.)
