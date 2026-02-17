"""
lwm_parser.py — Parse raw world‑model outputs (video/physics/spatial features)
into a normalized intermediate representation.

This module defines the first step of the LWM → WLM pipeline.
It does NOT interpret meaning — it only normalizes structure.
"""


def parse_lwm(lwm_output):
    """
    Normalize raw world‑model outputs into a consistent intermediate structure.

    Parameters
    ----------
    lwm_output : dict or model‑specific structure
        Raw output from a world model (video features, physics signals, spatial maps).

    Returns
    -------
    dict
        A normalized intermediate representation.
    """
    # MVP: pass-through
    return lwm_output
