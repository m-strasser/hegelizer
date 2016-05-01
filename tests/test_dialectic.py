#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.base import TestCase
from hegelizer.dialectic import Dialectic
from hegelizer.notion import Notion


class TestDialectic(TestCase):
    """Tests for the representation of a dialectic."""
    def setUp(self):
        path1 = Notion("Dieser", "Allgemeines", ["Ich", "Einzelner"])
        path2 = Notion("Dieses", "Allgemeines", ["Gegenstand", "Einzelnes"])
        root = Notion("Sinnliches Bewusstsein", "Unknown", ["Wissen des " +
                                                            "Seienden"])

        self.dialectic = Dialectic(root, path1, path2)

    def test_string_representation(self):
        """Tests if the string representation of the dialectic is correct."""
        expected = """
 -----------------------------------
| Root:    | Sinnliches Bewusstsein |
| Path #1: | Dieser                 |
| Path #2: | Dieses                 |
 -----------------------------------
"""
        actual = str(self.dialectic)

        self.assertEqual(expected, actual)
