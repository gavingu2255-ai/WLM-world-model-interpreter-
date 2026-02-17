import pytest
from wlm_world_model_interpreter.lwm_parser import parse_lwm


def test_parse_lwm_pass_through():
    sample = {"objects": [{"id": 1, "class": "Ball"}]}
    out = parse_lwm(sample)
    assert out == sample
