import pytest
from wlm_world_model_interpreter.wlm_emitter import emit_wlm


def test_emit_wlm_deterministic():
    graph = {
        "nodes": [],
        "relations": [],
        "dimensions": {
            "spatial": {},
            "temporal": {},
            "physical": {},
            "causal": {},
        },
    }

    out1 = emit_wlm(graph)
    out2 = emit_wlm(graph)

    assert isinstance(out1, str)
    assert out1 == out2  # deterministic
    assert "WLMGraph" in out1
