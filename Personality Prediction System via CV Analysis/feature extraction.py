from sklearn.feature_extraction.text import TfidfVectorizer

# Define a TfidfVectorizer object to extract features from the preprocessed text
tfidf = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))

# Fit the vectorizer to the preprocessed text data
tfidf.fit(data_df['preprocessed_text'])

# Extract features from the preprocessed text data
X = tfidf.transform(data_df['preprocessed_text']).toarray()
