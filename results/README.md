# Research evidence

The CSV files in this directory extract metrics from the preserved notebook outputs. Baseline precision, recall, and F1-score are reported for Outcome=1. Blank ROC-AUC fields mean that ROC-AUC was not computed in the original notebook.

The SVG figures are version-controlled research artifacts:

- feature_importance_random_forest.svg visualizes the stored feature-importance values.
- confusion_matrix_*.svg visualizes confusion matrices reconstructed from the stored classification-report counts.
- roc_auc_comparison.svg records that ROC-AUC is unavailable in the preserved experiments; it is not an estimated ROC curve.
