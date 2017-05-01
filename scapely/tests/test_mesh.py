# -*- coding: utf-8 -*-
from scapely.mesh import Vertex


def test_vertex_init():
    vertex = Vertex(0.0, 1.0, 2.0)
    assert vertex.x == 0.0
    assert vertex.y == 1.0
    assert vertex.z == 2.0
    assert vertex.error is None
    assert not vertex.used
