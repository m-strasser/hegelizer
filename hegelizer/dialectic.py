#!/usr/bin/env python
# -*- coding: utf8 -*-
import graphviz as gv


class Dialectic():
    """Representation of a dialectic, containing two paths and a root."""

    def __init__(self, root, path1, path2):
        self.root = root
        self.path1 = path1
        self.path2 = path2

    def __str__(self):
        """Returns the string representation of the dialectic as a padded table.
        """
        attrs = [self.root.name, self.path1.name, self.path2.name]
        lens = [len(x) for x in attrs]
        pad_to = max(lens)

        heading = " -----------"
        heading += "".join(['-'] * (pad_to + 2))
        heading += "\n"

        body = "| Root:    | {}{!s}{}".format(
            self.root.name,
            "".join([' '] * (pad_to - len(self.root.name))),
            " |\n"
        )

        body += "| Path #1: | {}{!s}{}".format(
            self.path1.name,
            "".join([' '] * (pad_to - len(self.path1.name))),
            " |\n"
        )

        body += "| Path #2: | {}{!s}{}".format(
            self.path2.name,
            "".join([' '] * (pad_to - len(self.path2.name))),
            " |\n"
        )

        tostr = "\n" + heading + body + heading
        return tostr

    def make_markdown_graph(self, distance=1):
        """Generates a markdown tikz representation of the dialectic with the
        given node distance in centimeters."""

        graph = "\n\\begin{{tikzpicture}}[auto, node distance={} cm]\n".format(distance)
        graph += "{};\n{};\n{};\n".format(
            self.root.make_node(1),
            self.path1.make_node(2, 1, "above right"),
            self.path2.make_node(3, 1, "below right")
        )
        graph += "\n\\path[-] (N{}) node (N{})\n(N{}) node (N{});\n".format(
            1, 2, 1, 3
        )

        graph += "\\end{tikzpicture}\n"

        return graph

    def make_graphviz_graph(self, fileformat='jpeg'):
        """Creates a graphviz representation of the dialectic in the given file
        format."""
        g1 = gv.Graph(format=fileformat)
        g1.node(self.root.name)
        g1.node(self.path1.name)
        g1.node(self.path2.name)
        g1.edge(self.root.name, self.path1.name)
        g1.edge(self.root.name, self.path2.name)

        self.graph = g1
        return self.graph
