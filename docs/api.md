# API Specification — WLM‑World‑Model‑Interpreter  
**Public API surface for converting world‑model outputs → WLM structural graphs**

This document defines the official API for the WLM‑World‑Model‑Interpreter.  
The API is intentionally minimal, deterministic, and stable across versions.

---

# 1. High‑Level API

The primary entry point is:

```python
interpret_lwm(lwm_output) -> str
```

### Description
Converts raw world‑model outputs into a deterministic, serialized WLM structural graph.

### Signature

```python
def interpret_lwm(lwm_output: dict) -> str:
    """
    Convert world‑model outputs into a deterministic WLM structural graph.
    """
```

### Parameters

| Name        | Type | Description |
|-------------|------|-------------|
| `lwm_output` | `dict` | Raw output from a world model (video, physics, spatial, trajectory). |

### Returns

| Type | Description |
|------|-------------|
| `str` | A serialized WLM structural graph (WLMGraph). |

### Example

```python
from wlm_world_model_interpreter import interpret_lwm

lwm_output = {
    "objects": [...],
    "flow": [...],
    "depth": [...],
}

graph = interpret_lwm(lwm_output)
print(graph)
```

---

# 2. Pipeline Stages

The interpreter is composed of four internal modules.  
Each stage is isolated and testable.

```
parse_lwm       → normalize raw LWM output
extract_features → canonicalize features
map_to_wlm      → semantic mapping (LWM → WLM)
emit_wlm        → serialize WLMGraph
```

---

## 2.1 `parse_lwm`

```python
from wlm_world_model_interpreter.lwm_parser import parse_lwm
```

### Purpose
Normalize raw world‑model outputs into a consistent intermediate representation.

### Signature

```python
def parse_lwm(lwm_output: dict) -> dict:
    ...
```

---

## 2.2 `extract_features`

```python
from wlm_world_model_interpreter.lwm_extractor import extract_features
```

### Purpose
Extract canonical features from the parsed LWM output.

### Signature

```python
def extract_features(parsed: dict) -> dict:
    ...
```

---

## 2.3 `map_to_wlm`

```python
from wlm_world_model_interpreter.lwm_mapper import map_to_wlm
```

### Purpose
Map canonical LWM features into a WLM structural graph.

### Signature

```python
def map_to_wlm(features: dict) -> dict:
    ...
```

### Output Structure (WLMGraph)

```python
{
    "nodes": [...],
    "relations": [...],
    "dimensions": {
        "spatial": {...},
        "temporal": {...},
        "physical": {...},
        "causal": {...}
    }
}
```

---

## 2.4 `emit_wlm`

```python
from wlm_world_model_interpreter.wlm_emitter import emit_wlm
```

### Purpose
Serialize a WLMGraph into a deterministic, human‑readable text format.

### Signature

```python
def emit_wlm(graph: dict) -> str:
    ...
```

---

# 3. CLI API

The interpreter provides a command‑line interface:

```
wlm-world interpret-lwm <input>
```

### Usage

```
wlm-world interpret-lwm features.json
wlm-world interpret-lwm '{"objects": [...]}'
wlm-world interpret-lwm features.json --out graph.wlm
```

### Arguments

| Argument | Description |
|----------|-------------|
| `input` | JSON file path or inline JSON string |
| `--out` | Optional output file path |

---

# 4. Error Handling

The API guarantees:

- deterministic behavior  
- no silent failures  
- clear error messages  
- no partial graph emission  

Errors are raised as Python exceptions or printed to stderr in CLI mode.

---

# 5. Versioning

The API follows **semantic versioning**:

- `0.x` — experimental  
- `1.x` — stable public API  
- `2.x` — multi‑modal, real‑time extensions  

---

# 6. Extension Points

Developers may extend:

- custom LWM parsers  
- custom feature extractors  
- custom mapping rules  
- custom WLM emitters  
- custom CLI subcommands  

The pipeline is intentionally modular.

---

# 7. Summary

The WLM‑World‑Model‑Interpreter exposes a single stable public API:

```
interpret_lwm(lwm_output) -> WLMGraph (serialized)
```

Internally, it uses a clean four‑stage pipeline:

```
parse → extract → map → emit
```

This API enables world models to produce **interpretable, deterministic, multi‑dimensional WLM structures**.
