# Visual Contrast Sensitivity (Pelli-Robson) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Visual Contrast Sensitivity Function (CSF), Pelli-Robson chart log scores, and digital display ergonomics.

```mermaid
flowchart TD
    LetterTriplets["Pelli-Robson Chart Letter Triplets (1 m distance)"] --> LogScore["Log Contrast Sensitivity Score (0.00 - 2.25)"]
    LogScore --> WeberFormula["Weber Physical Contrast Percentage (10^-log * 100)"]
    WeberFormula --> AcuityEngine["Visual Contrast Acuity & Glare Resilience Engine"]
    AcuityEngine --> Agent["OpenClaw / Hermes Personal Agent Actions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Clinical Psychophysical Standards**: Implements validated logarithmic Pelli-Robson formulas.
- **Display Readability & Glare Stratification**: Direct quantification of visual edge sharpness under digital screen work.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import OcularContrastSensitivityClient

client = OcularContrastSensitivityClient()
result = client.evaluate_contrast_sensitivity(
    log_contrast_score=1.80
)
print("Weber Contrast Threshold:", result["weber_contrast_threshold_pct"], "%")
print("Classification:", result["classification"])
```

## License
Apache-2.0
