# -*- coding: utf-8 -*-


class Vertex(object):
    def __init__(self, x, y, z):
        """
        A mesh vertex contains the 3-dimensional cooridnates and the local
        error, if already calculated.
        :param x: Value of the x coordinate.
        :type x: float
        :param y: Value of the y coordinate.
        :type y: float
        :param z: Value of the z coordinate.
        :type z: float
        """
        self._x_ = x
        self._y_ = y
        self._z_ = z
        self._error_ = None
        self._used_ = False

    @property
    def x(self):
        return self._x_

    @property
    def y(self):
        return self._y_

    @property
    def z(self):
        return self._z_

    @property
    def error(self):
        return self._error_

    @property
    def used(self):
        return self._used_


class Triangle(object):
    def __init__(self, vertex_1, vertex_2, vertex_3):
        """
        Represents a mesh triangle consisting of three vertices.
        :param vertex_1: First triangle vertex.
        :type vertex_1: scapely.mesh.Vertex
        :param vertex_2: Second triangle vertex.
        :type vertex_2: scapely.mesh.Vertex
        :param vertex_3: Third triangle vertex.
        :type vertex_3: scapely.mesh.Vertex
        """
        self._v1_ = vertex_1
        self._v2_ = vertex_2
        self._v3_ = vertex_3

    @property
    def vertex_1(self):
        return self._v1_

    @property
    def vertex_2(self):
        return self._v2_

    @property
    def vertex_3(self):
        return self._v3_
