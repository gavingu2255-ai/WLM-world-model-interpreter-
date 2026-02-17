"""
wlm_emitter.py — Emit a deterministic, human‑readable WLM structural graph.

This module converts the internal WLMGraph representation into a serialized
text format suitable for debugging, logging, visualization, or downstream
consumption by WLM tools.

MVP behavior:
    - Deterministic ordering
    - Clean, readable formatting
    - Stable output shape
"""


def emit_wlm(graph):
    """
    Serialize a WLM structural graph into a deterministic text format.

    Parameters
    ----------
    graph : dict
        A WLMGraph-like structure:
        {
            "nodes": [...],
            "relations": [...],
            "dimensions": {...}
        }

    Returns
    -------
    str
        A human‑readable structural representation.
    """

    # Deterministic ordering
    nodes = graph.get("nodes", [])
    relations = graph.get("relations", [])
    dimensions = graph.get("dimensions", {})

    lines = []
    lines.append("WLMGraph {")

    # --- Nodes ---
    lines.append("  nodes: [")
    for node in nodes:
        lines.append(f"    {repr(node)},")
    lines.append("  ]")

    # --- Relations ---
    lines.append("  relations: [")
    for rel in relations:
        lines.append(f"    {repr(rel)},")
    lines.append("  ]")

    # --- Dimensions ---
    lines.append("  dimensions: {")
    for dim, value in sorted(dimensions.items()):
        lines.append(f"    {dim}: {repr(value)},")
    lines.append("  }")

    lines.append("}")

    return "\n".join(lines)
