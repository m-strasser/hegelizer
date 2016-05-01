#!/usr/bin/env python
# -*- coding: utf8 -*-


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
