---
name: genpark-personal-agent-ocular-contrast-sensitivity-pelli-robson-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating visual contrast sensitivity (CSF), Pelli-Robson log scores, and display ergonomics.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Visual Contrast Sensitivity (Pelli-Robson) Skill

A sovereign personal agent capability for evaluating visual contrast sensitivity function (CSF), Pelli-Robson logarithmic triplet scoring, and optimizing display text legibility under ambient lighting.

## Core Capabilities
- **Pelli-Robson Logarithmic Scaling**: Maps letter triplet scores (0.00 to 2.25) into clinical log contrast sensitivity units.
- **Weber Contrast Threshold**: Converts log units to exact physical luminance contrast percentages ($C_W \times 100\%$).
- **Visual Contrast Acuity Score**: 0-100 index rating edge detection fidelity and glare vulnerability.
- **Display UI Ergonomics**: Recommends WCAG contrast ratios, ambient bias lighting, and dark/light mode switching thresholds.

## Fast Invocation
```python
from client import OcularContrastSensitivityClient

client = OcularContrastSensitivityClient()
res = client.evaluate_contrast_sensitivity(
    log_contrast_score=1.80
)
print("Weber Threshold:", res["weber_contrast_threshold_pct"], "%")
print("Acuity Score:", res["contrast_acuity_score"])
```
