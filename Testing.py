import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

class RekomendasiResep:
    def __init__(self, dataset_path, vectorizer_path, knn_model_path):
        self.df = pd.read_csv(dataset_path, encoding='latin-1')
        with open(vectorizer_path, 'rb') as file:
            self.vectorizer = pickle.load(file)
        with open(knn_model_path, 'rb') as file:
            self.knn_model = pickle.load(file)

    def get_recommendations(self, list_of_strings):
        joined_string = " ".join(list_of_strings)
        user_input_vector = self.vectorizer.transform([joined_string])
        y_pred = self.knn_model.predict(user_input_vector)
        
        indeks_cocok = self.df['Nama_Resep'][self.df['Nama_Resep'] == y_pred[0]].index
        jarak, indeks = self.knn_model.kneighbors(self.vectorizer.transform(self.df['Token'][indeks_cocok]))
        
        indeks_knn = indeks[0]
        indeks_acak = np.random.permutation(indeks_knn)
        
        resep_cocok = self.df.iloc[indeks_acak]
        
        response_data = []

        for i, index in enumerate(indeks_knn):
            nama_resep = self.df.loc[index, 'Nama_Resep']
            jenis_resep = self.df.loc[index, 'Jenis_Resep']
            similar_recipes = self.df[self.df['Nama_Resep'].str.contains(nama_resep, case=False)]
            distance = jarak[0][i]

            bahan_bahan_list = []
            cara_membuat_list = []

            exact_matches = similar_recipes[similar_recipes['Nama_Resep'] == nama_resep]

            if not exact_matches.empty:
                for idx, (_, exact_match) in enumerate(exact_matches.iterrows(), start=1):
                    bahan_bahan = exact_match['Bahan_Bahan'].split('--')
                    bahan_list = [ingredient.strip() for ingredient in bahan_bahan if ingredient.strip()]
                    bahan_bahan_list.extend(bahan_list)

                    cara_membuat = exact_match['Cara_Membuat'].split('--')
                    cara_membuat_list.extend(cara_membuat)

            recipe_dict = {
                "Nama Resep": nama_resep,
                "Jenis Resep": jenis_resep,
                "Euclidean Distance": distance,
                "Bahan-Bahan": bahan_bahan_list,
                "Cara Membuat": cara_membuat_list
            }

            response_data.append(recipe_dict)

        return response_data

if __name__ == '__main__':
    dataset_path = 'DatasetFinalWithToken2.csv'
    vectorizer_path = 'vectorizer.pkl'
    knn_model_path = 'knn_model.pkl'

    recommender = RekomendasiResep(dataset_path, vectorizer_path, knn_model_path)
    
    test_inputs = [['tempe', 'cabai', 'tomat']]

    for user_input in test_inputs:
        recommendations = recommender.get_recommendations(user_input)
        for recipe in recommendations:
            print(recipe)
            print("--------------------")
