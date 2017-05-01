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
