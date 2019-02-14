#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Graph:
    """
    A class for simple graphs.
    The graphs are encoded as a adjacency list, with weights on the edges.
    Possibility of adding arcs (i.e. oriented edges) too.
    The question of multigraphs is not dealt yet.
    """

    def add_vertex(label):
        """
        Adds a vertex to the current graph.
        The added vertex is isolated, with no neighbors.
        @param label an identifier to the vertex.
        """
    
    def remove_vertex(vertex):
        """
        Removes the vertex from the graph, and all incident edges.
        @param vertex the vertex to remove.
        """

    def add_edge(vertex1, vertex2, weight=1):
        """
        Adds the edge linking vertex1 to vertex2.
        @param vertex1 : one extremity of the edge
        @param vertex2 : the other extremity
        @param weight : an optionnal weight to the edge, default value = 1.
        """

    def remove_edge(vertex1, vertex2):
        """ 
        Removes the edge from the graph, with no impact on the vertices.
        """

    def update_edge_weight(vertex1, vertex2, new_weight):
        """
        Updates the weight of the edge.
        """

    # Do the same for arcs.

    def get_neighbors(vertex):
        """
        Returns a list of the (out)neighbors of the vertex.
        """

    
class Vertex:
    """
    A class or the vertices of a graph.
    """

    def color_vertex(color):
        """
        Sets a color to the current vertex.
        """

    
