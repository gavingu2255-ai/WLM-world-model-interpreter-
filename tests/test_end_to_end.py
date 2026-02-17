import pytest
from wlm_world_model_interpreter import interpret_lwm


def test_end_to_end_pipeline_runs():
    lwm_output = {
        "objects": [{"id": 1, "class": "Ball"}],
        "flow": {},
        "depth": {},
    }

    result = interpret_lwm(lwm_output)

    assert isinstance(result, str)
    assert "WLMGraph" in result
