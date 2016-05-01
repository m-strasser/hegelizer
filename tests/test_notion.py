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
        expected_above = "\\node[state] (N1) [above of=N0] \{Gegenstand\}"
        expected_below = "\\node[state] (N1) [below of=N0] \{Gegenstand\}"
        expected_right = "\\node[state] (N1) [right of=N0] \{Gegenstand\}"
        expected_left = "\\node[state] (N1) [left of=N0] \{Gegenstand\}"
        expected_above_left = "\\node[state] (N1) [above left of=N0] \{Gegenstand\}"
        expected_above_right = "\\node[state] (N1) [above right of=N0] \{Gegenstand\}"
        expected_below_left = "\\node[state] (N1) [below left of=N0] \{Gegenstand\}"
        expected_below_right = "\\node[state] (N1) [below right of=N0] \{Gegenstand\}"
        expected_right_above = "\\node[state] (N1) [right above of=N0] \{Gegenstand\}"
        expected_right_below = "\\node[state] (N1) [right below of=N0] \{Gegenstand\}"
        expected_left_above = "\\node[state] (N1) [left above of=N0] \{Gegenstand\}"
        expected_left_below = "\\node[state] (N1) [left below of=N0] \{Gegenstand\}"

        actual = self.notion.make_node(1)
        actual_above = self.notion.make_node(1, 0, "above")
        actual_below = self.notion.make_node(1, 0, "below")
        actual_right = self.notion.make_node(1, 0, "right")
        actual_left = self.notion.make_node(1, 0, "left")
        actual_above_right = self.notion.make_node(1, 0, "above right")
        actual_above_left = self.notion.make_node(1, 0, "above left")
        actual_below_right = self.notion.make_node(1, 0, "below right")
        actual_below_left = self.notion.make_node(1, 0, "below left")
        actual_right_above = self.notion.make_node(1, 0, "right above")
        actual_right_below = self.notion.make_node(1, 0, "right below")
        actual_left_above = self.notion.make_node(1, 0, "left above")
        actual_left_below = self.notion.make_node(1, 0, "left below")

        self.assertEqual(expected, actual)
        self.assertEqual(expected_above, actual_above)
        self.assertEqual(expected_below, actual_below)
        self.assertEqual(expected_right, actual_right)
        self.assertEqual(expected_left, actual_left)
        self.assertEqual(expected_above_right, actual_above_right)
        self.assertEqual(expected_below_right, actual_below_right)
        self.assertEqual(expected_above_left, actual_above_left)
        self.assertEqual(expected_below_left, actual_below_left)
        self.assertEqual(expected_right_above, actual_right_above)
        self.assertEqual(expected_right_below, actual_right_below)
        self.assertEqual(expected_left_above, actual_left_above)
        self.assertEqual(expected_left_below, actual_left_below)
