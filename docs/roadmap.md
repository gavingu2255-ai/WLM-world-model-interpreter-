# Roadmap — WLM‑World‑Model‑Interpreter  
**From MVP → multimodal → real‑time structural intelligence**

This roadmap outlines the evolution of the WLM‑World‑Model‑Interpreter from  
a minimal deterministic pipeline into a fully multimodal, real‑time,  
agent‑integrated structural explanation layer for world models.

The roadmap is divided into four phases:

1. MVP (deterministic pipeline)
2. Multimodal expansion (video, physics, 3D, trajectories)
3. Real‑time streaming interpreter
4. Agent‑integrated structural intelligence

---

# Phase 1 — MVP (Current)
**Goal:** Establish a clean, deterministic, testable pipeline.

### Deliverables
- `parse_lwm` — normalize raw LWM output  
- `extract_features` — canonicalize features  
- `map_to_wlm` — produce empty but structurally valid WLMGraph  
- `emit_wlm` — deterministic serialization  
- CLI: `wlm-world interpret-lwm`  
- Documentation: overview, mapping rules, API, roadmap  

### Success Criteria
- End‑to‑end pipeline runs deterministically  
- No model‑specific assumptions  
- Clean extension points for all future phases  

---

# Phase 2 — Multimodal Expansion
**Goal:** Support the major world‑model modalities.

### 2.1 Video Models
- bounding boxes → nodes  
- segmentation → nodes  
- depth → spatial dimension  
- optical flow → motion state  
- temporal consistency across frames  

### 2.2 Physics Models
- collisions → tensions  
- forces → physical dimension  
- stability → state: unstable  
- COM → physical attributes  

### 2.3 3D / Spatial Models
- 3D pose → spatial dimension  
- volumetric occupancy → containment relations  
- raycasting → obstruction relations  

### 2.4 Trajectory Models
- predicted positions → closures  
- predicted collisions → future tensions  
- predicted interactions → future relations  

### Success Criteria
- All four modalities produce consistent WLMGraphs  
- Deterministic mapping rules across models  
- No cross‑modal contradictions  

---

# Phase 3 — Real‑Time Streaming Interpreter
**Goal:** Convert continuous world‑model streams into continuous WLM structural updates.

### Deliverables
- streaming parser  
- incremental feature extractor  
- structural diff engine  
- temporal coherence module  
- real‑time CLI mode  
- optional WebSocket interface  

### Capabilities
- frame‑by‑frame structural updates  
- temporal smoothing  
- structural persistence across frames  
- event‑driven WLMGraph deltas  

### Success Criteria
- <50ms per‑frame interpretation  
- stable structural identity across time  
- no structural flicker  

---

# Phase 4 — Agent‑Integrated Structural Intelligence
**Goal:** Make WLMGraph the shared substrate for multi‑agent reasoning.

### Deliverables
- agent observation fusion  
- multi‑agent structural consensus  
- causal reasoning hooks  
- planning‑ready structural outputs  
- WLM structural simulator integration  

### Capabilities
- agents share a unified structural world  
- agents reason over tensions, closures, causal edges  
- agents can predict structural futures  
- agents can act based on structural deltas  

### Success Criteria
- multi‑agent tasks solved via shared WLMGraph  
- stable structural consensus across agents  
- causal reasoning validated in simulation  

---

# Phase 5 — Structural‑Native World Models (Long‑Term)
**Goal:** World models that output structure natively.

### Research Directions
- structure‑aware latent spaces  
- structural priors in video models  
- causal‑dimension alignment  
- tension‑aware physics models  
- WLMGraph as a training target  

### Vision
World models stop being pixel‑predictors.  
They become **structure‑predictors**.

---

# Summary

The WLM‑World‑Model‑Interpreter evolves through:

1. **MVP** — deterministic pipeline  
2. **Multimodal** — video, physics, 3D, trajectories  
3. **Real‑time** — streaming structural interpretation  
4. **Agent‑integrated** — shared structural substrate  
5. **Structural‑native** — world models that output structure directly  

This roadmap transforms world models from **prediction machines** into  
**explanation machines**, fully aligned with the WLM ecosystem.
