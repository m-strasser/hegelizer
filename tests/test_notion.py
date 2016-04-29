#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.base import TestCase
from hegelizer.notion import Notion


class TestNotion(TestCase):
    """Tests for the representation of a notion."""
    def setUp(self):
        name = "Gegenstand"
        name2 = "Langer Name"
        hegelian_type = "Allgemeines"
        hegelian_type2 = "Besonderes"
        other_names = ["Einzelnes", "Dieses"]
        other_names2 = ["Reaaaaaaally long n", "Not so long"]
        notes = ""
        notes2 = "This needs some line breaks."
        self.notion = Notion(name, hegelian_type, other_names, notes)
        self.notion2 = Notion(name2, hegelian_type2, other_names2, notes2)

    def test_to_string(self):
        """Tests the string representation of the notion."""
        expected = """
 ------------------------------
| Name:          | Gegenstand  |
| Hegelian Type: | Allgemeines |
| Other names:   | Einzelnes   |
|                | Dieses      |
| Notes:         |             |
 ------------------------------
"""
        expected_2 = """
 --------------------------------------
| Name:          | Langer Name         |
| Hegelian Type: | Besonderes          |
| Other names:   | Reaaaaaaally long n |
|                | Not so long         |
| Notes:         | This needs some     |
|                | line breaks.        |
 --------------------------------------
"""
        actual = str(self.notion)
        actual2 = str(self.notion2)

        self.assertEqual(expected, actual)
        self.assertEqual(expected_2, actual2)

    def test_make_node(self):
        """Tests the graph representation of the notion."""
        expected = "\\node[state] (N1) \{Gegenstand\}"
        actual = self.notion.makeNode()

        self.fail("Notion needs to be implemented")
        self.assertEqual(expected, actual)
