import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Define a function to preprocess the text data
def preprocess_text(text):
    # Convert the text to lowercase
    text = text.lower()
    
    # Remove punctuation and special characters
    text = re.sub('[^a-zA-Z0-9]', ' ', text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    # Stemming
    ps = PorterStemmer()
    words = [ps.stem(word) for word in words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Join the words back into a string
    text = ' '.join(words)
    
    return text

# Apply the preprocessing function to the text data
data_df['preprocessed_text'] = data_df['text'].apply(preprocess_text)
