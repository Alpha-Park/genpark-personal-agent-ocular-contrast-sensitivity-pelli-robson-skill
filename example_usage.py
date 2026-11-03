"""
Example Usage: Visual Contrast Sensitivity Function (Pelli-Robson).
Demonstrates psychophysical calculation of log contrast score and Weber contrast percentage.
"""

from client import OcularContrastSensitivityClient


def main():
    client = OcularContrastSensitivityClient()
    print("=== Visual Contrast Sensitivity (Pelli-Robson) Demo ===")

    # Test Case 1: Healthy normal visual contrast (Young adult)
    res1 = client.evaluate_contrast_sensitivity(
        log_contrast_score=1.80,
        viewing_distance_m=1.0,
        ambient_lux=420.0
    )
    print("\nTest Case 1: Healthy Normal Contrast Acuity")
    print(f"  Pelli-Robson Score: {res1['pelli_robson_log_score']} log units")
    print(f"  Weber Contrast Threshold: {res1['weber_contrast_threshold_pct']}%")
    print(f"  Contrast Acuity Score: {res1['contrast_acuity_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Glare disability / low-contrast visual fatigue
    res2 = client.evaluate_contrast_sensitivity(
        log_contrast_score=1.20,
        viewing_distance_m=1.0,
        ambient_lux=300.0
    )
    print("\nTest Case 2: Contrast Loss & Glare Disability")
    print(f"  Score: {res2['pelli_robson_log_score']} log units | Threshold: {res2['weber_contrast_threshold_pct']}%")
    print(f"  Contrast Score: {res2['contrast_acuity_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
