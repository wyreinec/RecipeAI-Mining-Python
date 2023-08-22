from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from TFIDF import X_train, X_test, y_train, y_test, tfidf_processor
import pickle

class KNNModel:
    def __init__(self, X_train, X_test, y_train, y_test, vectorizer, n_neighbors=5):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.vectorizer = vectorizer
        self.n_neighbors = n_neighbors
        self.knn_model = KNeighborsClassifier(n_neighbors=n_neighbors)
    
    def train_model(self):
        self.knn_model.fit(self.X_train, self.y_train)
    
    def predict(self):
        y_pred = self.knn_model.predict(self.X_test)
        return y_pred
    
    def save_model(self, model_filename='knn_model.pkl', vectorizer_filename='vectorizer.pkl'):
        with open(model_filename, 'wb') as f:
            pickle.dump(self.knn_model, f)
        
        with open(vectorizer_filename, 'wb') as f:
            pickle.dump(self.vectorizer, f)


knn_model = KNNModel(X_train, X_test, y_train, y_test, tfidf_processor.vectorizer, n_neighbors=5)
knn_model.train_model()
y_pred = knn_model.predict()
knn_model.save_model()

