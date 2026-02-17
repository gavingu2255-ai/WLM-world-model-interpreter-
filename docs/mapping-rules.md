# Mapping Rules: LWM → WLM Structural Dimensions  
**How world‑model outputs become WLM structural graphs**

This document defines the mapping rules that convert world‑model outputs  
(video, physics, spatial, trajectory signals) into **WLM structural primitives**.

The mapping is deterministic, model‑agnostic, and dimension‑aligned.

---

# 1. Overview

World models (LWM/VLM/3D/physics models) output **latent or numeric signals**:

- bounding boxes  
- segmentation masks  
- depth maps  
- optical flow  
- 3D poses  
- physics engine forces  
- collision events  
- trajectory predictions  
- affordance maps  

WLM requires **explicit structure**:

- nodes  
- relations  
- states  
- tensions  
- spatial/temporal/physical dimensions  
- causal edges  
- closures  

This document defines the rules that bridge the two.

---

# 2. Object Detection → Nodes

| LWM Signal | WLM Structure |
|-----------|----------------|
| bounding box | `node <Object>` |
| segmentation mask | `node <Object>` |
| object class | `type` attribute |
| instance ID | stable node identity |

### Rule
```
For each detected object O:
    create node O {
        type: <class>
    }
```

### Example
```
bbox: {class: "Cup"} → node Cup
bbox: {class: "Ball"} → node Ball
```

---

# 3. Spatial Signals → Spatial Dimension

Spatial signals include:

- bounding box coordinates  
- depth  
- 3D pose  
- relative position  
- segmentation geometry  

### Rules

### 3.1 Absolute position
```
depth → spatial.z
bbox center → spatial.x, spatial.y
```

### 3.2 Relative spatial relations
```
if center(Ball).x < center(Cup).x → relation: left_of(Ball, Cup)
if depth(Ball) < depth(Table) → relation: in_front_of(Ball, Table)
if overlap(Ball, Table) → relation: on(Ball, Table)
```

### 3.3 Containment
```
mask(Ball) inside mask(Box) → relation: inside(Ball, Box)
```

---

# 4. Motion Signals → Temporal Dimension

Motion signals include:

- optical flow  
- trajectory vectors  
- velocity  
- acceleration  

### Rules

### 4.1 Motion state
```
if |flow| > threshold → state: moving
else → state: stationary
```

### 4.2 Directional motion
```
flow vector → trajectory: toward(X)
```

### 4.3 Predicted future motion
```
trajectory model → closure: future_position(node)
```

---

# 5. Physics Signals → Physical Dimension

Physics signals include:

- forces  
- collisions  
- torque  
- stability  
- center of mass  
- friction  
- gravity alignment  

### Rules

### 5.1 Collisions → Tensions
```
collision(A, B) → tension: contact(A, B)
```

### 5.2 Instability
```
if COM outside support polygon → state: unstable
```

### 5.3 Forces
```
force vector → physical.force(node)
```

### 5.4 Gravity
```
if tilt > threshold → tension: gravity
```

---

# 6. Affordances → Causal Dimension

Affordance models output:

- graspable  
- pushable  
- openable  
- reachable  
- obstructed  

### Rules

### 6.1 Action affordances
```
affordance: graspable → causal: can_grasp(Agent, Object)
affordance: pushable → causal: can_push(Agent, Object)
```

### 6.2 Obstruction
```
if raycast blocked → relation: obstructs(A, B)
```

### 6.3 Agent‑object causal edges
```
if affordance probability high → causal edge
```

---

# 7. Trajectory Predictions → Temporal Closure

Trajectory models output:

- predicted positions  
- predicted collisions  
- predicted interactions  

### Rules

### 7.1 Future position
```
trajectory(t+1) → closure: future_position(node)
```

### 7.2 Predicted collision
```
if predicted_collision(A, B) → closure: future_tension(contact(A, B))
```

### 7.3 Predicted relation change
```
if Ball will reach Cup → closure: future_relation(toward(Ball, Cup))
```

---

# 8. Combined Example

### Input (LWM signals)
```
Ball: moving right, depth=2.1
Cup: stationary, depth=2.3
Trajectory: Ball → Cup
```

### Output (WLM structure)
```
node Ball {
    state: moving
    trajectory: toward(Cup)
    spatial: {z: 2.1}
}

node Cup {
    state: stationary
    spatial: {z: 2.3}
}

relation: in_front_of(Ball, Cup)

closure: future_relation(toward(Ball, Cup))
```

---

# 9. Determinism

All mappings must be:

- deterministic  
- reproducible  
- model‑agnostic  
- dimension‑aligned  

Same input → same WLMGraph.

---

# 10. Future Extensions

- multi‑agent observation fusion  
- 3D volumetric mapping  
- real‑time streaming interpretation  
- WLM causal engine integration  
- WLM structural simulator feedback  

