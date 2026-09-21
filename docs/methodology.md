# Methodology

## Dataset

The analysis uses data/diabetes.csv. The notebook treats the clinical and demographic columns as predictors and Outcome as the binary target. Dataset provenance, cohort definition, collection setting, and licensing should be documented before publication.

## Data-quality assessment

The notebook checks for duplicate rows, missing values, and column data types. It records that the variables are numerical and does not add categorical encoding. The dataset also contains clinically implausible zero values in some biomedical fields in the original research workflow; these are not newly imputed or rewritten here and require domain-informed handling in future work.

## Preprocessing and outliers

The notebook creates an analytical copy and applies sequential IQR-based filtering to selected variables, including Pregnancies, Glucose, BloodPressure, SkinThickness, and BMI. This produces new_df, which is then used for the baseline modeling path. Outlier removal can change the target population and should be justified with clinical context rather than treated as a neutral cleanup step.

## Class imbalance and SMOTE

The target distribution is inspected before SMOTE is applied. SMOTE generates a resampled feature matrix and target (x_sm, y_sm) for a separate experiment. The existing notebook performs resampling before its cross-validation experiment; a stronger future design should place resampling inside each training fold to prevent information leakage.

## Feature selection

The notebook uses chi-squared SelectKBest to rank numerical predictors and explores reduced feature sets. It also examines random-forest feature importance. These methods are useful exploratory diagnostics but are not causal explanations and should be tested for stability across resamples and external cohorts.

## Model training

The preserved notebook evaluates logistic regression, support vector classification, decision tree, and random forest models. It uses model defaults, stratified hold-out splits, and an additional random-forest experiment on SMOTE-resampled data. Random seeds are not fixed in the existing logic, so reruns may produce different splits and metrics.

## Evaluation approach

The notebook reports accuracy, class-specific precision, recall, F1-score, and confusion matrices for the baseline models. It also records maximum fold accuracy from shuffled 10-fold cross-validation in later experiments. ROC-AUC was not computed in the preserved notebook outputs, so the Milestone 2 results table leaves that field unavailable rather than estimating it retrospectively.
