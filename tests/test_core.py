# -*- coding: utf-8 -*-

""" Tests for absolutist.code. """

from unittest import TestCase

from absolang.core import absolutist_index


class AbsoluteIndexTests(TestCase):
    def test_absolutist_index(self):
        absolutist_index("My name is Simon.")
