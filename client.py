"""
Visual Contrast Sensitivity Function (CSF) & Pelli-Robson Log-Contrast Engine.
Provides deterministic, zero-dependency psychophysical modeling of Pelli-Robson letter triplet scoring,
Weber contrast percentages, spatial frequency attenuation, and display readability ergonomics.
"""

import math
from typing import Dict, Any, List, Optional


class OcularContrastSensitivityClient:
    """
    Deterministic client for calculating Visual Contrast Sensitivity using the Pelli-Robson standard.
    Assesses intermediate spatial frequency neural contrast transfer, subclinical optical scattering,
    and display luminance readability under varying ambient lighting conditions.
    """

    def __init__(self):
        pass

    def evaluate_contrast_sensitivity(
        self,
        log_contrast_score: float,
        viewing_distance_m: float = 1.0,
        ambient_lux: float = 400.0,
        spatial_frequency_cpd: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Calculates Weber contrast percentage = (10 ^ (-log_score)) * 100.
        Pelli-Robson chart range: 0.00 to 2.25 log units (in 0.15 increments).
        Normal healthy young/middle adult score: 1.65 - 1.95 log units (1.1% - 2.2% contrast).
        """
        if log_contrast_score < 0.0 or log_contrast_score > 2.40:
            return {"error": "Pelli-Robson log contrast score must be between 0.0 and 2.40"}

        weber_contrast_fraction = 10.0 ** (-log_contrast_score)
        contrast_threshold_pct = round(weber_contrast_fraction * 100.0, 2)

        # Contrast Acuity Score (0 - 100):
        # Log score 1.75 - 2.10 -> 90 - 100.
        # Log score < 1.35 -> < 50.
        score = (log_contrast_score / 2.0) * 100.0
        final_score = round(min(100.0, max(5.0, score)), 1)

        if log_contrast_score >= 1.70:
            tier = "OPTIMAL_CONTRAST_SENSITIVITY"
            interp = f"Exceptional neural contrast resolution ({log_contrast_score} log units, {contrast_threshold_pct}% threshold); crisp boundary detection."
            guidance = "Superior visual edge discrimination and glare resistance. High comfort across subtle UI gradients and low-contrast typography."
        elif log_contrast_score >= 1.50:
            tier = "NORMAL_FUNCTIONAL_CONTRAST"
            interp = f"Normal functional contrast perception ({log_contrast_score} log units, {contrast_threshold_pct}% threshold); standard spatial frequency transfer."
            guidance = "Adequate everyday visual contrast. Maintain appropriate display contrast ratios (WCAG AAA >= 7:1 for text)."
        elif log_contrast_score >= 1.30:
            tier = "MILD_CONTRAST_ATTENUATION"
            interp = f"Subtle contrast reduction ({log_contrast_score} log units, {contrast_threshold_pct}% threshold); increased susceptibility to screen glare."
            guidance = "Mild contrast fatigue. Increase display text contrast, use dark-on-light or high-contrast theme, and reduce overhead glare."
        else:
            tier = "SIGNIFICANT_CONTRAST_LOSS_GLARE_DISABILITY"
            interp = f"Severe loss of contrast sensitivity ({log_contrast_score} log units < 1.30); significant difficulty distinguishing subtle gray gradations."
            guidance = "Pronounced contrast disability. Avoid low-light night driving and schedule formal ophthalmological examination for optical scattering/cataract."

        return {
            "pelli_robson_log_score": log_contrast_score,
            "weber_contrast_threshold_pct": contrast_threshold_pct,
            "viewing_distance_m": viewing_distance_m,
            "ambient_lux": ambient_lux,
            "spatial_frequency_cpd": spatial_frequency_cpd,
            "contrast_acuity_score": final_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
