# Diabetes Prediction Using Supervised and Unsupervised Machine Learning

This repository contains the implementation, analysis, and supporting materials for the published research work on diabetes prediction using supervised and unsupervised machine learning approaches.

The repository is organized as a reproducible research portfolio: the notebook preserves the modeling workflow, `src/` contains reusable explainability utilities, `results/` contains extracted evidence and figures, and `docs/` records the methodology, interpretation, and limitations. The checked-in notebook currently provides the reproducible supervised-modeling path; the broader supervised and unsupervised scope reflects the published research title.

## Research Achievement

> **Best Paper Award**
> **“Diabetes Prediction Using Supervised and Unsupervised Machine Learning”**

| Detail | Information |
| --- | --- |
| **Award recipient** | Noor Mohammed Vempalli |
| **Conference** | International Conference on Embracing The Digital Horizon (EDH 2024) |
| **Institution** | Madanapalle Institute of Technology & Science |
| **Date** | March 13–14, 2024 |

| Research link | Reference |
| --- | --- |
| **GitHub repository** | [Chinnunoor/diabetes-prediction-ml](https://github.com/Chinnunoor/diabetes-prediction-ml) |
| **Publication** | [ResearchGate publication record](https://www.researchgate.net/publication/408187952_Diabetes_Prediction_Using_Supervised_and_Unsupervised_Machine_Learning) |
| **DOI** | [10.2174/9798898814441126060026](https://doi.org/10.2174/9798898814441126060026) |
| **Award certificate** | No certificate file or public certificate link is currently included in this repository. |

## My Contributions

My contribution is represented through the implementation and research artifacts maintained in this repository:

- Designed and organized the end-to-end machine-learning research workflow in [`notebooks/diabetes_prediction_modeling.ipynb`](notebooks/diabetes_prediction_modeling.ipynb), including data inspection, exploratory analysis, preprocessing, model training, and evaluation.
- Implemented the data-quality and preprocessing path, including duplicate and missing-value checks, sequential IQR-based outlier filtering, class-balance inspection, and SMOTE experimentation; see [`docs/methodology.md`](docs/methodology.md).
- Developed the model-evaluation workflow for logistic regression, support vector classification, decision tree, and random-forest baselines, with stratified hold-out metrics, classification reports, confusion matrices, and cross-validation experiments.
- Performed feature analysis using chi-squared `SelectKBest` selection and random-forest feature importance; the preserved analysis identifies Glucose, BMI, Age, and DiabetesPedigreeFunction as leading features in the recorded fitted model.
- Structured a reproducible research repository with source data, notebook, extracted CSV evidence, version-controlled SVG figures, documentation, and exported reports.
- Created technical visualizations and research documentation, including the workflow, results dashboard, project architecture, explainability direction, methodology, results interpretation, and future-work materials.
- Added reusable SHAP preparation and explanation utilities in [`src/explainability.py`](src/explainability.py), while documenting that a serialized fitted model is required before generating model-specific SHAP outputs.

## Research Implementation

The research workflow is summarized below. The published work spans supervised and unsupervised approaches; the current checked-in notebook provides the supervised model-comparison path and associated exploratory analyses.

```text
Research Problem
        ↓
Clinical Dataset Analysis
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Supervised & Unsupervised ML Models
        ↓
Model Evaluation
        ↓
Feature Interpretation
        ↓
Research Insights
```

### Research architecture and workflow

![Research project visualization](results/figures/project_visualization.svg)

*Research architecture connecting the healthcare motivation, predictive task, machine-learning workflow, evidence, and interpretation.*

![Machine-learning workflow](results/figures/ml_workflow.svg)

*Implementation workflow from dataset inspection through preprocessing, exploratory analysis, model evaluation, and explainability.*

![Results dashboard](results/figures/results_dashboard.svg)

*Evidence dashboard summarizing preserved model metrics, confusion-matrix examples, feature importance, and unavailable metrics.*

![Explainable AI direction](results/figures/explainable_ai.svg)

*Explainability path from global feature importance toward future local explanations after a compatible fitted model is available.*

## Results Showcase

The repository preserves the recorded outputs of the exploratory study rather than presenting them as clinical validation:

| Visualization | What it demonstrates |
| --- | --- |
| [Model comparison](results/model_comparison.csv) | Baseline accuracy, precision, recall, and F1-score comparisons for the preserved classifier experiments. |
| [Feature importance](results/feature_importance_random_forest.svg) | Relative feature importance in the stored random-forest output; this is model-specific and not causal evidence. |
| [Confusion matrices](results/confusion_matrix_logistic_regression.svg) · [SVM](results/confusion_matrix_svm.svg) · [decision tree](results/confusion_matrix_decision_tree.svg) · [random forest](results/confusion_matrix_random_forest.svg) | Class-level prediction counts for the baseline experiments, preserving the orientation of the original notebook output. |
| [Evaluation visualizations](results/roc_auc_comparison.svg) · [metrics table](results/evaluation_metrics.csv) | Recorded evaluation evidence and an explicit indication that ROC-AUC was not computed in the preserved notebook outputs. |

Among the preserved stratified hold-out experiments, random forest recorded the highest baseline accuracy at 0.7500. A separate SMOTE random-forest hold-out experiment recorded 0.8162 accuracy, but its complete classification report was not preserved. These values are split- and dataset-specific; they should not be interpreted as clinical performance estimates. See [`docs/results_analysis.md`](docs/results_analysis.md) for the full interpretation and caveats.

## Publication

**Title:** Diabetes Prediction Using Supervised and Unsupervised Machine Learning

**Authors:**

- Noor Mohammed Vempalli
- BSH. Shayeez Ahamed
- Shaik Fazeelunnisa
- Obulam Vinisha
- K. Yeswanth

**Publication and conference details:**

- [ResearchGate publication record](https://www.researchgate.net/publication/408187952_Diabetes_Prediction_Using_Supervised_and_Unsupervised_Machine_Learning)
- [DOI: 10.2174/9798898814441126060026](https://doi.org/10.2174/9798898814441126060026)
- International Conference on Embracing The Digital Horizon (EDH 2024)
- Madanapalle Institute of Technology & Science
- March 13–14, 2024

## Repository Structure

```text
data/       Source dataset used by the notebook
notebooks/  Reproducible exploratory analysis and modeling notebook
src/        Reusable explainability utilities
results/    Extracted metrics, tables, confusion matrices, and research figures
docs/       Research question, methodology, results analysis, and future work
reports/    Exported HTML analysis and presentation artifacts
```

## Reproducibility

Create an environment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

Launch Jupyter from the repository root:

```bash
jupyter notebook notebooks/diabetes_prediction_modeling.ipynb
```

The notebook reads the dataset from `data/diabetes.csv` using a repository-relative path. Extracted evidence is available in [`results/model_comparison.csv`](results/model_comparison.csv) and [`results/evaluation_metrics.csv`](results/evaluation_metrics.csv), while the exported analysis and presentation are preserved under [`reports/`](reports/).

## Research Scope and Limitations

This is an exploratory research implementation, not a validated clinical decision-support system. The current workflow uses model defaults and unseeded random splits; resampling is not nested inside validation folds; the dataset provenance and cohort definition require further documentation; and the preserved outputs do not include calibration, external validation, fairness analysis, confidence intervals, or decision-curve analysis. Biomedical zero values and outlier filtering also require domain-informed review.

The repository does not provide medical advice and must not be used for patient-level decisions. See [`docs/methodology.md`](docs/methodology.md) and [`docs/results_analysis.md`](docs/results_analysis.md) for detailed caveats.

## Future Research

- **Explainable AI:** Generate global and local SHAP explanations from a serialized or freshly fitted model, with clinical review of interpretation.
- **Clinical interpretability:** Evaluate calibration, thresholds, uncertainty, and clinically meaningful error trade-offs.
- **Larger healthcare datasets:** Validate on larger, more diverse, and external datasets with documented cohort and label construction.
- **Model robustness:** Use leakage-safe resampling, fixed seeds, subgroup analysis, confidence intervals, and sensitivity analyses.
- **Real-world healthcare deployment:** Study privacy, governance, workflow integration, monitoring, prospective silent evaluation, and human factors before any patient-facing use.

## License and Data Use

### Dataset note

The dataset source and provenance should be documented before reuse or redistribution. It contains clinical attributes used for research experimentation; the repository does not claim that it contains private patient data. Confirm the dataset's licensing and privacy status before using it in a public or operational setting.

No software license has been added yet. Before public distribution, add an appropriate code license and document the dataset license, provenance, privacy, and redistribution constraints.
