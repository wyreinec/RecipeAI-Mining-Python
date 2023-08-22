import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Load tokenized data from Tokenizing.csv
tokenized_data = pd.read_csv('DatasetFinalWithToken2.csv', encoding='latin1')

class TFIDFProcessor:
    def __init__(self, tokenized_data):
        self.tokenized_data = tokenized_data
        self.vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b[\w&.\-]+\b")
        self.X = None
        self.y = None
        self.terms = None
    
    def fit_transform(self):
        self.X = self.vectorizer.fit_transform(self.tokenized_data['Token'])
        self.y = self.tokenized_data['Nama_Resep']
        self.terms = self.vectorizer.get_feature_names_out()
    
    def display_top_terms(self, num_terms=5):
        assert self.X is not None and self.y is not None
        for idx, recipe in enumerate(self.y):
            tfidf_values = self.X[idx].toarray()[0]
            sorted_indices = tfidf_values.argsort()[::-1]
            
            print(f"Resep: {recipe}")
            print("Istilah yang paling berkorelasi:")
            for index in sorted_indices[:num_terms]:
                term = self.terms[index]
                tfidf = tfidf_values[index]
                print(f"- Term: {term}, TF-IDF: {tfidf}")
            print("----------")
    
    def get_shapes(self):
        return f"Shape of X: {self.X.shape}", f"Shape of y: {self.y.shape}"

tfidf_processor = TFIDFProcessor(tokenized_data)
tfidf_processor.fit_transform()
tfidf_processor.display_top_terms()
print(tfidf_processor.get_shapes())

X_train, X_test, y_train, y_test = train_test_split(tfidf_processor.X, tfidf_processor.y, test_size=0.2, random_state=42)

print('Training Data Shape:', X_train.shape)
print('Testing Data Shape:', X_test.shape)
