from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from TFIDF import tfidf_processor
from KNNModel import knn_model
from Testing import user_input

class Evaluasi:
    def __init__(self, tfidf_processor, knn_model, user_input_vector, tf_idf):
        self.tfidf_processor = tfidf_processor
        self.knn_model = knn_model
        self.user_input_vector = user_input_vector
        self.tf_idf = tf_idf

    def evaluate_accuracy(self):
        knn_model_k1 = KNeighborsClassifier(n_neighbors=1)
        knn_model_k1.fit(self.knn_model.X_train, self.knn_model.y_train)
        y_pred_k1 = knn_model_k1.predict(self.knn_model.X_test)
        accuracy_k1 = accuracy_score(self.knn_model.y_test, y_pred_k1)

        print("Accuracy with k=1:", accuracy_k1)

evaluation = Evaluasi(tfidf_processor, knn_model, user_input_vector, tf_idf)
evaluation.evaluate_accuracy()
