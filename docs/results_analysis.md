# Results analysis

## Model comparison

The extracted baseline results are stored in results/model_comparison.csv. Among the preserved stratified hold-out experiments, the random forest recorded the highest accuracy at 0.7500. Its Outcome=1 precision was 0.53, recall was 0.66, and F1-score was 0.58. The SMOTE random-forest hold-out experiment recorded 0.8162 accuracy, but the original notebook did not store a full classification report for that run, so the remaining metrics are intentionally unavailable.

The later cross-validation cells report maximum fold accuracies of 0.9140 for the SMOTE experiment, 0.9043 for the reduced-feature experiment, and 0.8404 for the feature-importance experiment. These are maximum fold values, not mean cross-validation performance, and should not be presented as unbiased generalization estimates.

## Important features

The preserved random-forest importance output ranks Glucose highest, followed by BMI, Age, and DiabetesPedigreeFunction. The plot in results/feature_importance_random_forest.svg visualizes those stored values. Feature importance indicates contribution to this fitted model; it does not show that a feature causes diabetes or that it is sufficient for individual risk assessment.

## Confusion matrices and ROC-AUC

The baseline confusion-matrix figures are provided for inspection. The notebook called confusion_matrix with the prediction array as its first argument, so the figures are labeled to preserve that existing orientation rather than silently changing the experiment. ROC-AUC was not present in the notebook outputs and is shown as unavailable in results/roc_auc_comparison.svg.

## Limitations

- The dataset context and provenance are not sufficiently documented for clinical claims.
- Zero values in biomedical fields may represent missingness or invalid measurements.
- Outlier filtering and SMOTE can alter the effective population and class distribution.
- Resampling is not nested inside validation folds in the existing workflow.
- Random seeds are not fixed and the reported cross-validation summary emphasizes maximum fold accuracy.
- No calibration, external validation, fairness analysis, confidence intervals, or decision-curve analysis is available.

## Healthcare interpretation

For screening-oriented research, recall for the positive class and calibration may be more clinically relevant than accuracy alone, but the appropriate trade-off depends on the intended use and harms of false positives and false negatives. These results are therefore best treated as hypothesis-generating evidence for a more rigorous, clinically contextualized study.
