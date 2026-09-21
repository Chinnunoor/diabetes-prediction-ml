"""Explainability utilities for the diabetes prediction research portfolio.

The current repository does not include a serialized fitted model. These
utilities therefore provide a preparation layer for the next execution:
fit or load a model, preserve the feature matrix and feature names, and then
call the functions below to generate SHAP-based explanations.
"""

from __future__ import annotations

from typing import Any, Sequence

import numpy as np
import pandas as pd

try:
    import shap
except ImportError:
    shap = None


def shap_available() -> bool:
    """Return whether the optional SHAP dependency is installed."""

    return shap is not None


def create_shap_explainer(model: Any, background_data: Any = None) -> Any:
    """Create a SHAP explainer for a fitted model."""

    if shap is None:
        raise ImportError(
            "SHAP is not installed. Install requirements.txt, then rerun "
            "this utility with a fitted model."
        )

    if hasattr(model, "feature_importances_"):
        return shap.TreeExplainer(model)
    return shap.Explainer(model, background_data)


def compute_shap_values(
    model: Any, features: pd.DataFrame, background_data: Any = None
) -> tuple[Any, Any]:
    """Return the explainer and SHAP values for a feature matrix."""

    explainer = create_shap_explainer(model, background_data)
    return explainer, explainer(features)


def shap_feature_importance(
    shap_values: Any, feature_names: Sequence[str]
) -> pd.DataFrame:
    """Summarize mean absolute SHAP magnitude by feature."""

    values = getattr(shap_values, "values", shap_values)
    if isinstance(values, list):
        values = values[-1]
    values = np.asarray(values)
    if values.ndim == 3:
        values = values[:, :, -1]
    importance = np.abs(values).mean(axis=0)
    return (
        pd.DataFrame({"Feature": list(feature_names), "MeanAbsSHAP": importance})
        .sort_values("MeanAbsSHAP", ascending=False)
        .reset_index(drop=True)
    )


def plot_shap_summary(
    shap_values: Any, features: pd.DataFrame, max_display: int = 10
) -> Any:
    """Create a SHAP global summary plot for a future fitted-model run."""

    if shap is None:
        raise ImportError("Install SHAP before generating a summary plot.")
    values = shap_values
    if isinstance(values, list):
        values = values[-1]
    return shap.summary_plot(values, features, max_display=max_display, show=False)


def explain_prediction(
    model: Any,
    observation: pd.DataFrame,
    background_data: Any = None,
) -> Any:
    """Return a local SHAP explanation for one or more observations."""

    explainer = create_shap_explainer(model, background_data)
    return explainer(observation)
