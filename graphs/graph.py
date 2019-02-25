#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from .vertex import Vertex
class Graph:
    """
    A class for simple graphs.
    The graphs are encoded as a adjacency list, with weights on the edges.
    Possibility of adding arcs (i.e. oriented edges) too.
    The question of multigraphs is not dealt yet.
    """

    def __init__(self):
        self.vertices = []

    def get_vertex(self, label):
        """
        Return the instance of the vertex with the label.
        @param label the label of the wanted vertex
        """
        if Vertex(label) not in self.vertices:
            raise Exception("There is no vertex with this label")
        return self.vertices[self.vertices.index(Vertex(label))]

    def add_vertex(self, label):
        """
        Adds a vertex to the current graph.
        The added vertex is isolated, with no neighbors.
        @param label an identifier to the vertex.
        """
        vertex = Vertex(label)
        if vertex in self.vertices:
            raise Exception("A Vertex with the same name is already in the graph")
        self.vertices.append(vertex)

    def remove_vertex(self, label):
        """
        Removes the vertex from the graph, and all incident edges.
        @param label the label of the vertex to remove.
        """
        vertex = Vertex(label)
        if vertex not in self.vertices:
            raise Exception("This Vertex is not in the graph.")
        else:
            self.vertices.remove(vertex)

    def add_edge(self, label_vertex1, label_vertex2, weight=1):
        """
        Adds the edge linking vertex1 to vertex2.
        @param label_vertex1 : one extremity of the edge
        @param label_vertex2 : the other extremity
        @param weight : an optionnal weight to the edge, default value = 1.
        """
        vertex1 = self.get_vertex(label_vertex1)
        vertex2 = self.get_vertex(label_vertex2)
        vertex1.add_neighbour(vertex2, weight)
        vertex2.add_neighbour(vertex1, weight)

    def remove_edge(self, vertex1, vertex2):
        """
        Removes the edge from the graph, with no impact on the vertices.
        """

    def update_edge_weight(self, vertex1, vertex2, new_weight):
        """
        Updates the weight of the edge.
        """

    def add_arc(vertex1, vertex2, weight):
        """
        Adds an arc from vertex1 to vertex2
        @param vertex1 : Origin of the arc.
        @param vertex2 : Destination of the arc.
        @param weight : an optionnal weight to the edge, default value = 1.
        """

    def get_neighbors(vertex):
        """
        Returns a list of the (out)neighbors of the vertex.
        """



    def display(self):
        """
        Display the Vertex's list of the graph. Only for debug purpose.
        """
        for vertex in self.vertices:
            print(vertex)
