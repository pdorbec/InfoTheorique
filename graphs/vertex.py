#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vertices

Mostly intended to be used by the graph module
"""

class Vertex(object):
    """
    A class for the vertices of a graph.
    """

    def __init__(self, name):
        """Initializes a vertex with a given name.
        """
        self.color = "#FFFFFF"
        self.name = name
        self.neighbors = []
        self.edge_weight = []

    def add_neighbor(self, vertex, weight=1, directed=False):
        """Adds a neighbor to the current vertex.

        Default weight is 1.
        If undirected (default), also adds the current vertex as a neighbor
        to the other vertex.
        """
        self.neighbors.append(vertex)
        self.edge_weight.append(weight)
        if not directed:
            vertex.add_neighbor(self, weight, True)

    def __str__(self):
        """
        Returns a description of the vertex
        """
        neighbors = ""
        for i in range(0, len(self.neighbors)):
            neighbors += "(" + self.neighbors[i].name +":" + str(self.edge_weight[i]) +  ")"
        return self.name + " voisins : " + neighbors

    def __eq__(self, other):
        """
        @param o object to test
        Return true if the two vertex have the same name.
        """
        return isinstance(other, Vertex) and self.name == other.name

    def set_color(self, color):
        """
        Sets a color to the current vertex.
        """
        self.color = color
