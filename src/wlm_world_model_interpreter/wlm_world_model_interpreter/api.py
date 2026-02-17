"""
API entry point for WLM‑World‑Model‑Interpreter.

This module defines the high‑level function `interpret_lwm`,
which converts world‑model outputs into a deterministic WLM structure graph.
"""

from .lwm_parser import parse_lwm
from .lwm_extractor import extract_features
from .lwm_mapper import map_to_wlm
from .wlm_emitter import emit_wlm


def interpret_lwm(lwm_output):
    """
    Convert world‑model outputs into a deterministic WLM structural graph.

    Parameters
    ----------
    lwm_output : dict or model‑specific structure
        Raw output from a world model (video, physics, spatial, trajectory).

    Returns
    -------
    str
        A serialized WLM structural graph.
    """
    parsed = parse_lwm(lwm_output)
    features = extract_features(parsed)
    wlm_graph = map_to_wlm(features)
    return emit_wlm(wlm_graph)
