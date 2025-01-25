# Twitter Sentiment Analysis on Apple and Google Products

## Introduction

This project aims to analyze public sentiment towards Apple and Google products using Twitter data. By building and evaluating sentiment classification models, we aim to:

 - Gain insights into consumer perceptions of Apple and Google products.
 - Identify key drivers of positive and negative sentiment.
 - Inform marketing strategies and product development decisions for both companies.
 
## Data

**Dataset**: Utilized a dataset of approximately 9,000 tweets collected during the SXSW conference, labeled with sentiment (positive, negative, neutral).

**Data Sources**: Sourced from CrowdFlower (https://data.world/crowdflower/brands-and-product-emotions).

## Data Preparation:
- Cleaned data by handling missing values, removing duplicates, and renaming columns.
- Preprocessed text data by following the steps below:
  - Lowercasing, tokenization, punctuation removal, stop word removal.
  - Removed irrelevant words (e.g., "sxsw," "link," "RT").
  - Performed lemmatization using NLTK.

## Exploratory Data Analysis:
- Analyzed sentiment distribution (neutral dominant, followed by positive, then negative).
- Investigated brand distribution (Apple received more attention).
- Analyzed sentiment distribution by brand (Apple showed slightly higher positive sentiment).
 - Analyzed top words associated with each sentiment category.

## Modelling

### Binary Classification (Positive vs. Negative):

**Baseline Model**: Multinomial Naive Bayes was used and it achieved baseline accuracy.
 - **Hyperparameter Tuning**: Improved Multinomial Naive Bayes performance using Grid Search.
 - **Oversampling (SMOTE)**: Led to decreased performance, particularly in recall.
 
**Neural Network**: Achieved slightly lower performance than the best Multinomial Naive Bayes model.

### Multi-class Classification (Positive, Negative, Neutral):

**Baseline Model**: Multinomial Naive Bayes was used and it achieved moderate accuracy.
 - **Hyperparameter Tuning**: Improved Multinomial Naive Bayes performance.
 
**XGBoost**: Outperformed Multinomial Naive Bayes with higher accuracy, precision, and recall.

  - **Oversampling (SMOTE)**: Improved precision but decreased accuracy and recall.

### Key Findings:

- Class imbalance significantly impacted model performance.
- **Multinomial Naive Bayes** excelled in binary classification.
- **XGBoost** outperformed **Multinomial Naive Bayes** in multi-class classification.
- Challenges in accurately classifying negative sentiment were observed.

### Model Selection:
- **Tuned Multinomial Naive Bayes** was chosen for the best binary classification model.
- **XGBoost** without oversampling was selected as the best model for multi-class classification.

## Recommendations

- **Improve negative sentiment classification**: Explore techniques like class-weighting, and specialized algorithms for imbalanced datasets.
- **Consider data source diversity**: Collect data from sources beyond SXSW to obtain a more representative sample of user sentiment.
- **Granular product analysis**: Analyze sentiment for specific products (e.g., iPhone vs. Pixel 7) for more targeted insights.
- **Explore advanced techniques**: Investigate deep learning models and advanced text representation methods.
- **Actionable insights**: Leverage findings to inform marketing strategies, product development, and customer experience initiatives.

## Conclusion

This analysis provides valuable insights into consumer sentiment towards Apple and Google products. While the models achieved promising results, further research and refinement are necessary to improve accuracy and address the challenges posed by class imbalance and data limitations.


