"""
MCP Server for Visual Contrast Sensitivity (Pelli-Robson) Skill.
Exposes JSON-RPC Model Context Protocol tools for assessing visual contrast acuity, Weber thresholds, and display ergonomics.
"""

import sys
import json
from typing import Dict, Any
from client import OcularContrastSensitivityClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_contrast_sensitivity",
                "description": "Calculates Pelli-Robson log contrast score, Weber contrast threshold percentage, and visual contrast acuity score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "log_contrast_score": {
                            "type": "number",
                            "description": "Pelli-Robson score in log units from 0.0 to 2.25 (e.g. 1.80 for healthy adult)."
                        },
                        "viewing_distance_m": {
                            "type": "number",
                            "description": "Chart viewing distance in meters (standard is 1.0 m).",
                            "default": 1.0
                        },
                        "ambient_lux": {
                            "type": "number",
                            "description": "Ambient room illuminance in lux (typically 300 - 500 lux).",
                            "default": 400.0
                        },
                        "spatial_frequency_cpd": {
                            "type": "number",
                            "description": "Optional spatial frequency in cycles per degree."
                        }
                    },
                    "required": ["log_contrast_score"]
                }
            }
        ]
    }


def handle_request(client: OcularContrastSensitivityClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_contrast_sensitivity":
            sf = args.get("spatial_frequency_cpd")
            if sf is not None:
                sf = float(sf)

            res = client.evaluate_contrast_sensitivity(
                log_contrast_score=float(args.get("log_contrast_score", 1.80)),
                viewing_distance_m=float(args.get("viewing_distance_m", 1.0)),
                ambient_lux=float(args.get("ambient_lux", 400.0)),
                spatial_frequency_cpd=sf
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method {name} not found"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": "Invalid request"
            }
        }


def main():
    client = OcularContrastSensitivityClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32700, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
