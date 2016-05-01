#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tests.base import TestCase
from hegelizer.dialectic import Dialectic
from hegelizer.notion import Notion
import pdb


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

    def test_markdown_graph_representation(self):
        """Tests the markdown tikz representation of the dialectic."""
        expected = """
\\begin{tikzpicture}[auto, node distance=2 cm]
\\node[state] (N1) \{Sinnliches Bewusstsein\};
\\node[state] (N2) [above right of=N1] \{Dieser\};
\\node[state] (N3) [below right of=N1] \{Dieses\};

\\path[-] (N1) node (N2)
(N1) node (N3);
\\end{tikzpicture}
"""
        actual = self.dialectic.make_markdown_graph(2)

        self.assertEqual(expected, actual)

    def test_graphviz_representation(self):
        """Tests the graphviz representation of the dialectic."""
        pdb.set_trace()
        expected = 'graph {\n\t"Sinnliches Bewusstsein"\n\tDieser\n\t'
        expected += 'Dieses\n\t\t"Sinnliches Bewusstsein" -- Dieser\n\t\t'
        expected += '"Sinnliches Bewusstsein" -- Dieses\n}'
        actual = self.dialectic.make_graphviz_graph().source

        self.assertEqual(expected, actual)
