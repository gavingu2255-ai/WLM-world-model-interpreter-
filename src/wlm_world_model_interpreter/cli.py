"""
Command-line interface for WLM‑World‑Model‑Interpreter.

Usage:
    wlm-world interpret-lwm features.json
    wlm-world interpret-lwm '{"boxes": [...]}'
    wlm-world interpret-lwm features.json --out graph.wlm
"""

import argparse
import json
import sys
from pathlib import Path

from .api import interpret_lwm


def load_input(input_arg: str):
    """
    Load input either from a JSON file or from an inline JSON string.
    """
    path = Path(input_arg)
    if path.exists() and path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            raise ValueError(f"File '{input_arg}' is not valid JSON.")
    else:
        try:
            return json.loads(input_arg)
        except json.JSONDecodeError:
            raise ValueError("Input must be a JSON file path or valid JSON string.")


def cmd_interpret_lwm(args):
    """
    Handle the `interpret-lwm` subcommand.
    """
    try:
        lwm_output = load_input(args.input)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    wlm_graph = interpret_lwm(lwm_output)

    if args.out:
        Path(args.out).write_text(wlm_graph, encoding="utf-8")
    else:
        print(wlm_graph)


def main():
    parser = argparse.ArgumentParser(
        prog="wlm-world",
        description="WLM‑World‑Model‑Interpreter CLI"
    )

    sub = parser.add_subparsers(dest="command")

    # -------------------------
    # interpret-lwm
    # -------------------------
    p_interpret = sub.add_parser(
        "interpret-lwm",
        help="Interpret world-model outputs into a WLM structural graph"
    )
    p_interpret.add_argument(
        "input",
        help="JSON file path or inline JSON string"
    )
    p_interpret.add_argument(
        "--out",
        help="Write output to file"
    )
    p_interpret.set_defaults(func=cmd_interpret_lwm)

    # -------------------------
    # Parse and dispatch
    # -------------------------
    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)

    args.func(args)
