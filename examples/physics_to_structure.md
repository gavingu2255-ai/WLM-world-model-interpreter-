# Example: Physics Engine Output → WLM Structure

This example demonstrates how physics‑based world‑model outputs  
(collisions, forces, stability signals) map into WLM structural dimensions.

---

## Input (LWM physics features)

```json
{
  "objects": [
    {"id": 1, "class": "Block"},
    {"id": 2, "class": "Table"}
  ],
  "collisions": [
    {"a": 1, "b": 2, "force": 12.5}
  ],
  "stability": {
    "1": "unstable"
  }
}
```

---

## Code

```python
from wlm_world_model_interpreter import interpret_lwm

with open("physics_features.json") as f:
    lwm_output = json.load(f)

wlm_graph = interpret_lwm(lwm_output)
print(wlm_graph)
```

---

## Output (MVP placeholder)

```
WLMGraph {
  nodes: [
  ]
  relations: [
  ]
  dimensions: {
    causal: {},
    physical: {},
    spatial: {},
    temporal: {},
  }
}
```

In future versions, this example will produce:

- node Block (state: unstable)  
- node Table  
- tension: contact(Block, Table)  
- physical.force(Block) = 12.5  

This file will evolve as physical mapping rules are implemented.
