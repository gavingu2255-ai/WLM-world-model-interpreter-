import pytest
from wlm_world_model_interpreter.lwm_mapper import map_to_wlm


def test_map_to_wlm_structure():
    features = {"objects": []}
    graph = map_to_wlm(features)

    assert isinstance(graph, dict)
    assert "nodes" in graph
    assert "relations" in graph
    assert "dimensions" in graph

    dims = graph["dimensions"]
    assert "spatial" in dims
    assert "temporal" in dims
    assert "physical" in dims
    assert "causal" in dims
