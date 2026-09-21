# Future work

## Explainable AI

Use src/explainability.py to generate SHAP explanations from a serialized or freshly fitted model. The next execution step is to fit a selected model with the repository dataset, retain the exact feature matrix and feature names, and pass those artifacts to the SHAP utilities. Compare global explanations with the stored random-forest importances and inspect individual cases with appropriate clinical review.

## Fairness and subgroup analysis

Evaluate discrimination, calibration, error rates, and threshold behavior across clinically relevant demographic or care-access subgroups when those variables and a defensible cohort definition are available. Fairness analysis should be planned with domain experts and should not rely on a single aggregate parity metric.

## Larger and external clinical datasets

Validate on larger, more diverse, and preferably external clinical datasets. Document missingness mechanisms, measurement timing, label construction, site effects, temporal drift, and the relationship between the research cohort and any intended deployment population.

## Deep learning and alternative approaches

Compare the interpretable tabular baselines with calibrated gradient-boosting methods and, only when data volume and modality justify it, deep-learning approaches. Any added complexity should demonstrate a meaningful and reproducible benefit over simpler models.

## Healthcare deployment

Study calibration, decision thresholds, uncertainty, human factors, workflow integration, monitoring, privacy, security, and governance before considering deployment. Prospective silent evaluation and clinician-centered usability testing should precede any patient-facing use.
