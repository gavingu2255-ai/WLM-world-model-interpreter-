# Example: Trajectory Prediction → WLM Structure

This example demonstrates how trajectory model outputs  
(predicted positions, predicted collisions, future interactions)  
map into WLM temporal and causal dimensions.

---

## Input (LWM trajectory features)

```json
{
  "objects": [
    {"id": 1, "class": "Ball"},
    {"id": 2, "class": "Cup"}
  ],
  "trajectory": {
    "1": {
      "future_positions": [
        {"t": 1, "pos": [0.2, 0.0]},
        {"t": 2, "pos": [0.4, 0.0]}
      ],
      "target": 2
    }
  }
}
```

---

## Code

```python
from wlm_world_model_interpreter import interpret_lwm

with open("trajectory_features.json") as f:
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

- node Ball  
- node Cup  
- temporal trajectory: toward(Cup)  
- closure: future_position(Ball)  
- closure: future_relation(toward(Ball, Cup))  

This file will evolve as trajectory mapping rules are implemented.
