#! /usr/bin/env python3
# -*- coding: utf-8 -*-
class Vertex:
    """
    A class for the vertices of a graph.
    """

    def __init__(self, name):
        self.color = "#FFFFFF"
        self.name = name
        self.neighbors = []
        self.edge_weight = []

    def add_neighbour(self, vertex, weight):
        self.neighbors.append(vertex)
        self.edge_weight.append(weight)

    def __str__(self):
        """
        Returns a description of the vertex
        """
        neighbours = ""
        for i in range(0, len(self.neighbors)):
            neighbours += "(" + self.neighbors[i].name +":" + str(self.edge_weight[i]) +  ")"
        return self.name + " voisins : " + neighbours

    def __eq__(self, o):
        """
        @param o object to test
        Return true if the two vertex have the same name.
        """
        return isinstance(o, Vertex) and self.name == o.name

    def color(self, color):
        """
        Sets a color to the current vertex.
        """
        self.color = color
