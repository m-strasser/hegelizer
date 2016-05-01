#!/usr/bin/env python
# -*- coding: utf8 -*-
import textwrap


class Notion():
    """Representation of a notion (i.e. a thing in a dialectic, not necessarily
    a notion in the hegelian sense)."""
    def __init__(self, name, hegelian_type, other_names, notes=""):
        self.name = name
        self.hegelian_type = hegelian_type
        self.other_names = other_names
        self.notes = notes

    def __str__(self):
        """Generate string representation of Notion as padded table."""
        attrs = [self.name, self.hegelian_type]
        attrs.extend(self.other_names)

        lens = [len(x) for x in attrs]
        pad_to = max(lens)

        heading = " -------------------"
        heading += "".join(['-'] * pad_to)
        heading += "\n"

        body = "| Name:          | {}{!s}{}".format(
                      self.name,
                      "".join([' '] * (pad_to - len(self.name))),
                      " |\n")

        body += "| Hegelian Type: | {}{!s}{}".format(
                       self.hegelian_type,
                       "".join([' '] * (pad_to - len(self.hegelian_type))),
                       " |\n")

        first = True
        for other_name in self.other_names:
            if first:
                body += "| Other names:   | "
                first = False
            else:
                body += "|                | "

            body += "{}{!s}{}".format(
                           other_name,
                           "".join([' '] * (pad_to - len(other_name))),
                           " |\n")

        # Insert linebreaks into notes
        # wrapped = [self.notes[i:i+pad_to] for i in range(0, len(self.notes), pad_to)]
        wrapped = textwrap.wrap(self.notes, pad_to)

        body += "| Notes:         | "

        if not wrapped:
            body += "{!s}{}".format(
                "".join([' '] * pad_to),
                " |\n"
            )

        first = True
        for line in wrapped:
            if first:
                first = False
            else:
                body += "|                | "

            body += "{}{!s}{}".format(
                line,
                "".join([' '] * (pad_to - len(line))),
                " |\n"
            )

        tostr = "\n" + heading + body + heading

        return tostr

    def make_node(self, number):
        """Returns a graphviz representation of the notion. The number is used to
        give a unique ID to the node in the corresponding graph of the dialectic.
        """

        return "\\node[state] (N1) \{{{}\}}".format(self.name)
