#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.base import TestCase
from hegelizer.model.notion import Notion


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
        expected_above = "\\node[state] (N2) [above of=N0] \{Gegenstand\}"
        expected_below = "\\node[state] (N3) [below of=N1] \{Gegenstand\}"
        expected_right = "\\node[state] (N4) [right of=N2] \{Gegenstand\}"
        expected_left = "\\node[state] (N5) [left of=N3] \{Gegenstand\}"
        expected_above_left = "\\node[state] (N6) [above left of=N4] \{Gegenstand\}"
        expected_above_right = "\\node[state] (N7) [above right of=N5] \{Gegenstand\}"
        expected_below_left = "\\node[state] (N8) [below left of=N6] \{Gegenstand\}"
        expected_below_right = "\\node[state] (N9) [below right of=N7] \{Gegenstand\}"
        expected_right_above = "\\node[state] (N10) [right above of=N8] \{Gegenstand\}"
        expected_right_below = "\\node[state] (N11) [right below of=N9] \{Gegenstand\}"
        expected_left_above = "\\node[state] (N12) [left above of=N10] \{Gegenstand\}"
        expected_left_below = "\\node[state] (N13) [left below of=N11] \{Gegenstand\}"
        expected_negative_number = "\\node[state] (N-1) \{Gegenstand\}"
        expected_negative_2nd_number = "\\node[state] (N1) [above of=N-1] \{Gegenstand\}"

        actual = self.notion.make_node(1)
        actual_above = self.notion.make_node(2, 0, "above")
        actual_below = self.notion.make_node(3, 1, "below")
        actual_right = self.notion.make_node(4, 2, "right")
        actual_left = self.notion.make_node(5, 3, "left")
        actual_above_left = self.notion.make_node(6, 4, "above left")
        actual_above_right = self.notion.make_node(7, 5, "above right")
        actual_below_left = self.notion.make_node(8, 6, "below left")
        actual_below_right = self.notion.make_node(9, 7, "below right")
        actual_right_above = self.notion.make_node(10, 8, "right above")
        actual_right_below = self.notion.make_node(11, 9, "right below")
        actual_left_above = self.notion.make_node(12, 10, "left above")
        actual_left_below = self.notion.make_node(13, 11, "left below")
        actual_negative_number = self.notion.make_node(-1)
        actual_negative_2nd_number = self.notion.make_node(1, -1, "above")

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
        self.assertEqual(expected_negative_number, actual_negative_number)
        self.assertNotEqual(expected_negative_2nd_number, actual_negative_2nd_number)
