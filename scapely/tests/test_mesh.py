# -*- coding: utf-8 -*-
from scapely.mesh import Vertex


def test_vertex_init():
    vertex = Vertex(0.0, 1.0, 2.0)
    assert vertex.x == 0.0 and vertex.y == 1.0 and vertex.z == 2.0 \
        and vertex.error is None and not vertex.used
