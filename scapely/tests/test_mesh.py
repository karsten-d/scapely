# -*- coding: utf-8 -*-
from scapely.mesh import Vertex, Triangle


def test_vertex_init():
    vertex = Vertex(0.0, 1.0, 2.0)
    assert vertex.x == 0.0 and vertex.y == 1.0 and vertex.z == 2.0 \
        and vertex.error is None and not vertex.used


def test_triangle_init():
    v1 = Vertex(0.0, 0.0, 0.0)
    v2 = Vertex(1.0, 0.0, 0.0)
    v3 = Vertex(1.0, 1.0, 1.0)
    triangle = Triangle(v1, v2, v3)
    assert triangle.vertex_1 == v1 and triangle.vertex_2 == v2 \
        and triangle.vertex_3 == v3
