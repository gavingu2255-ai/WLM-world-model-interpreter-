# Example: Video Model Output → WLM Structure

This example demonstrates how raw outputs from a video world model  
(bounding boxes, segmentation, depth, optical flow) flow through the  
WLM‑World‑Model‑Interpreter pipeline.

---

## Input (LWM video features)

```json
{
  "objects": [
    {"id": 1, "class": "Ball", "bbox": [120, 200, 160, 240], "depth": 2.1},
    {"id": 2, "class": "Cup",  "bbox": [300, 210, 340, 260], "depth": 2.3}
  ],
  "flow": {
    "1": [0.8, 0.0],
    "2": [0.0, 0.0]
  }
}
```

---

## Code

```python
from wlm_world_model_interpreter import interpret_lwm

with open("video_features.json") as f:
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

As the mapper becomes semantic, this example will produce:

- nodes for Ball and Cup  
- spatial relations (left_of, in_front_of)  
- motion state for Ball  
- temporal dimension from flow  
- future closure if trajectory is predicted  

This file will evolve as the interpreter evolves.
