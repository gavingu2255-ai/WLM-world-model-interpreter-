# WLM‑World‑Model‑Interpreter — Overview  
**Convert world‑model outputs → deterministic WLM structural graphs**

The **WLM‑World‑Model‑Interpreter** is the structural explanation layer for world models.  
It transforms raw outputs from LWM/VLM/3D/physics/trajectory models into  
**interpretable, deterministic, multi‑dimensional WLM structures**.

This interpreter is the second structural entry point into the WLM ecosystem:

- **SLP‑World‑Interpreter**: Language → Structure  
- **WLM‑World‑Model‑Interpreter**: World Model → Structure  

Together, they unify natural‑language and world‑model signals into a single  
**WLM structural substrate**.

---

## Why this exists

Modern world models can:

- predict the next frame  
- predict object motion  
- predict collisions  
- predict trajectories  
- predict affordances  

But they cannot explain:

- what entities exist  
- how they relate  
- what states they are in  
- what tensions are present  
- what dimensions are active  
- what causal structure is unfolding  

World models **predict** the world.  
WLM **explains** the world.

This interpreter provides the missing layer:

> **Latent → Structure**  
> **Prediction → Explanation**  
> **World Model → WLMGraph**

---

## What this interpreter does

Given world‑model outputs such as:

- bounding boxes  
- segmentation masks  
- depth maps  
- optical flow  
- 3D poses  
- physics engine signals  
- trajectory predictions  
- affordance maps  

It produces **WLM structural primitives**:

- nodes  
- relations  
- spatial dimensions  
- physical dimensions  
- temporal dimensions  
- tensions  
- closures  
- causal edges  

The output is a deterministic **WLMGraph** that can be consumed by:

- WLM reasoning engines  
- WLM structural simulators  
- multi‑agent systems  
- planning modules  
- embodied agents  
- robotics stacks  

---

## Architecture

The interpreter follows a clean, layered pipeline:

```
Raw LWM Output
      ↓
Parser (normalize)
      ↓
Extractor (canonicalize)
      ↓
Mapper (LWM → WLM semantics)
      ↓
Emitter (deterministic WLMGraph)
```

Each stage is isolated, testable, and extensible.

---

## Design principles

- **Deterministic** — same input → same structure  
- **Interpretable** — explicit nodes, relations, dimensions  
- **Modular** — each stage can evolve independently  
- **Model‑agnostic** — works with any world model  
- **Multi‑agent‑ready** — shared structural substrate  
- **Future‑proof** — supports new WLM dimensions  

---

## Status

MVP architecture complete.  
Mapping rules and dimensional semantics under development.

See `docs/roadmap.md` for upcoming milestones.

