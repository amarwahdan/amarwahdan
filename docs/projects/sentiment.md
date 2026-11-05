# Sentiment Analysis App — Architecture Brief

[Back to profile](../../README.md#featured-projects)

## System purpose

An end-to-end English tweet classifier covering preprocessing, feature extraction, model fitting, artifact serialization, and interactive inference.

## Engineering challenge

Remove social-media noise, preserve the fitted vectorizer/model contract at inference, and distinguish the custom classifier from a separate pretrained multilingual demonstration.

## Documented data flow

```mermaid
flowchart LR
    D[Sentiment140 corpus] --> S[20k sample before deduplication]
    S --> C[Clean tweets and deduplicate]
    C --> T[TF-IDF representation]
    T --> N[Multinomial Naive Bayes]
    N --> A[Serialized model and vectorizer]
    A --> G[Gradio prediction]
```

## Numeric evidence and status

**20,000 sampled rows before deduplication**, a TF-IDF cap of **5,000 features**, and an **80/20 split configuration**. Accuracy/F1 outputs are not preserved publicly, so no score is invented.

Public source with a local Gradio inference path; no persistent hosted demo is linked. The 1.6M figure describes the source corpus, not the training run.

## Technologies

Python · pandas · NLTK · scikit-learn · TF-IDF · Multinomial Naive Bayes · joblib · Gradio · Transformers

### Custom-model path

KaggleHub obtains Sentiment140. The script samples 20,000 rows with seed 42, removes duplicates, and cleans URLs, mentions, hashtags, punctuation, case, and stop words. `TfidfVectorizer` uses `max_features=5000`, unigram/bigram features, `min_df=5`, and `max_df=0.8`. A `test_size=0.2` split precedes fitting a default `MultinomialNB`.

### Artifact-backed inference

joblib saves `vectorizer.pkl` and `naivebayes_Model.pkl`; Gradio reloads these artifacts for positive/negative predictions. A separate interface wraps `tabularisai/multilingual-sentiment-analysis` through Transformers. That pretrained model is a second demonstration, not the custom TF-IDF model.

### Evaluation boundary

The script computes train/test accuracy, five-fold cross-validation, a confusion matrix, and a classification report. Numeric outputs are not committed, and the final row count after deduplication is not reported. The vocabulary is fitted before the train/test split in the checked-in workflow; a leakage-safe future benchmark should split text first and fit the vectorizer on training text only. No accuracy, F1, measured speedup, or exact final train/test count is claimed here.

## Original artifacts

- [Code repository](https://github.com/amarwahdan/Buliding-Sentiment-Analysis-App)
- [Implementation source](https://github.com/amarwahdan/Buliding-Sentiment-Analysis-App/blob/main/buliding_sentiment_analysis_app.py)
- [Source dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)
