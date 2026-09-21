# Diabetes Prediction Using Machine Learning

Research portfolio for an exploratory machine-learning study of diabetes outcome prediction using clinical and demographic features.

## Research question

How effectively can standard supervised-learning models distinguish diabetes outcomes in the included dataset, and which features contribute most to model performance?

## Repository structure

\`\`\`text
data/       Source dataset used by the notebook
notebooks/  Reproducible exploratory analysis and modeling notebook
src/        Space for reusable project code as the study is extended
results/    Reserved for generated metrics, figures, and model outputs
reports/    Presentation and exported HTML research artifacts
\`\`\`

## Analysis workflow

The notebook documents the current research workflow:

- dataset inspection and data-quality checks
- exploratory visualization and outlier filtering
- class-balance inspection and SMOTE experimentation
- train/test evaluation of logistic regression, SVM, and tree-based models
- random-forest cross-validation
- univariate feature selection and feature-importance analysis

The analysis is intentionally retained in its original notebook form. Results should be interpreted as an educational/research investigation, not as clinical validation or a diagnostic system.

## Getting started

Create an environment and install the dependencies:

\`\`\`bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
\`\`\`

Launch Jupyter from the repository root:

\`\`\`bash
jupyter notebook notebooks/diabetes_prediction_modeling.ipynb
\`\`\`

The notebook reads the dataset from \`data/diabetes.csv\` using a repository-relative path.

## Reproducibility and limitations

- Several notebook cells use model defaults and unseeded random splits; exact metrics may vary between runs.
- The notebook contains both the original imbalanced-data experiments and subsequent SMOTE experiments. Resampling strategy and validation design should be revisited before drawing conclusions.
- The dataset provenance, cohort definition, and clinical applicability should be documented further before publication.
- This repository does not provide medical advice and must not be used for patient-level decisions.

## Research artifacts

The \`reports/\` directory contains the existing exported analysis HTML and presentation. Generated figures, tables, and additional reports can be added under \`results/\` and \`reports/\` without changing the source notebook.

## License and data use

No license has been added yet. Before public distribution, add an appropriate code license and document the dataset license/provenance and any applicable privacy or redistribution constraints.
