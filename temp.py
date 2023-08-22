from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print('Training Data Shape:', X_train.shape)
print('Testing Data Shape:', X_test.shape)

from sklearn.neighbors import KNeighborsClassifier
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X, y)

y_pred = knn_model.predict(X_test)

import pickle

with open('knn_model.pkl', 'wb') as f:
    pickle.dump(knn_model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)



user_input = input("Masukkan Bahan: ")
print('Bahan yang dimasukkan: ', user_input)

user_input_vector = vectorizer.transform([user_input])

# Memprediksi dengan KNN model
y_pred = knn_model.predict(user_input_vector)

# Mendapatkan indeks resep yang cocok dengan user_input
indeks_cocok = y[y == y_pred[0]].index

# Resep yang cocok dicari nearest neighbornya
jarak, indeks = knn_model.kneighbors(X[indeks_cocok])

# Mendapatkan indeks dari KNN nya
indeks_knn = indeks[0]
indeks_acak = np.random.permutation(indeks_knn)

# Mengambil informasi resep yang cocok secara acak
resep_cocok = tf_idf.iloc[indeks_acak]

# Print the recommended recipes
for index, resep in resep_cocok.iterrows():
    nama_resep = resep['Nama_Resep']
    nama_bahan = resep['Bahan_Bahan']
    cara_membuat = resep['Cara_Membuat']
    token_resep = resep['Token']

    print("Rekomendasi Resep:")
    print("Nama Resep:", nama_resep)
    print("Bahan-Bahan:", nama_bahan)
    print("Cara Membuat:", cara_membuat)
    # print("Token:", token_resep)
    # print("Distance:", jarak)
    print("-----")

# %%
import json

rekomendasi_resep = []

for index, resep in resep_cocok.iterrows():
    nama_resep = resep['Nama_Resep']
    nama_bahan = resep['Bahan_Bahan']
    cara_membuat = resep['Cara_Membuat']

    data_resep = {
        'User_Input': user_input,
        'Nama Resep': nama_resep,
        'Bahan-Bahan': nama_bahan,
        'Cara Membuat': cara_membuat,
    }

    rekomendasi_resep.append(data_resep)

json_data = json.dumps(rekomendasi_resep)

print(json_data)


# %% [markdown]
# # Evaluation

# %%
token_aktual_resep = tf_idf['Token'].str.split(' ')
token_aktual_resep_set = token_aktual_resep.apply(set)
user_input_set = set(user_input.split())

# %% [markdown]
# <h4>One-vs-One</h4>

# %%
indeks_cocok_aktual = token_aktual_resep_set.apply(lambda x: len(x.intersection(user_input_set)) == len(user_input_set))
indeks_resep_aktual = tf_idf[indeks_cocok_aktual]

if not indeks_resep_aktual.empty:
    print("Resep dengan bahan yang cocok ditemukan!")
    for index, resep in indeks_resep_aktual.iterrows():
        nama_resep = resep['Nama_Resep']
        print("Nama Resep:", nama_resep)
else:
    print("Tidak ditemukan resep dengan bahan yang cocok. Namun, berikut rekomendasi terdekat dari bahanmu!")
    for index, resep in indeks_resep_aktual.iterrows():
        nama_resep = resep['Nama_Resep']
        print("Nama Resep:", nama_resep)

# akurasi = 1.0 if indeks_resep_aktual.values[0] == y_pred[0] else 0.0

# print("Akurasi:", akurasi)

# %% [markdown]
# <h3>Akurasi</h3>

# %%
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Define the range of k values
k_values = range(1, 3)

# Initialize empty lists for accuracy scores
train_akurasi = []
test_akurasi = []

# Iterate over different k values
for k in k_values:
    knn_model = KNeighborsClassifier(n_neighbors=k)
    knn_model.fit(X_train, y_train)

    # Predict on the training and testing set
    y_train_pred = knn_model.predict(X_train)
    y_test_pred = knn_model.predict(X_test)

    # Compute accuracy scores
    train_acc = accuracy_score(y_train, y_train_pred)
    test_acc = accuracy_score(y_test, y_test_pred)

    # Append accuracy scores to the lists
    train_akurasi.append(train_acc)
    test_akurasi.append(test_acc)

# Plot the accuracy scores
plt.plot(k_values, train_akurasi, label='Train Akurasi')
# plt.plot(k_values, test_accuracy, label='Test Accuracy')
plt.xlabel('k')
plt.ylabel('Akurasi')
plt.title('KNN Akurasi')
plt.legend()
plt.show()


# %%
persentase_akurasi_train = train_akurasi[0] * 100
print("Train Accuracy:", persentase_akurasi_train, "%")


# %%
print("X shape:", X.shape)
print("y_target shape:", y.shape)


# %% [markdown]
# <h3>Cosine Similarity</h3>

# %%
from sklearn.metrics.pairwise import cosine_similarity
kemiripan = cosine_similarity(user_input_vector, X)
indeks_kemiripan_resep = kemiripan.argsort()[0][::-1]

Nilai_N = [5, 10, 15]
list_indeks_kemiripan_resep = {}
# Print the top similar recipes
for N in Nilai_N:
    indeks_kemiripan_resep = indeks_kemiripan_resep[:N]
    list_indeks_kemiripan_resep[N] = indeks_kemiripan_resep

# Print the top similar recipes for each N value
for N, indeks_kemiripan_resep in list_indeks_kemiripan_resep.items():
    print(f"Top-{N} Rekomendasi Resep:")
    for index in indeks_kemiripan_resep:
        resep_mirip = tf_idf.iloc[index]
        nama_resep = resep_mirip['Nama_Resep']
        nama_bahan = resep_mirip['Bahan_Bahan']
        cara_membuat = resep_mirip['Cara_Membuat']

        print(f"Nama Resep: {nama_resep}")
        print(f"Bahan-Bahan: {nama_bahan}")
        print("Cara Membuat:", cara_membuat)
        print("Kemiripan:", kemiripan[0][index])
        print("-----")
    print()

# %% [markdown]
# <h3>Top-N Akurasi</h3>

# %%
banyak_pengguna = len(tf_idf['Nama_Resep'])
rekomendasi_benar = 0

for user_id, rekomendasi in tf_idf['Nama_Resep'].items():
    resep_relevan = tf_idf['Nama_Resep'].get(user_id, set())
    for item in rekomendasi:
        if item in resep_relevan:
            rekomendasi_benar += 1
            break

top_n_akurasi = rekomendasi_benar / banyak_pengguna * 100

print("Top-N Akurasi:", top_n_akurasi, "%")

# %% [markdown]
# <h3>MRR</h3>

# %%
banyak_pengguna = len(tf_idf['Nama_Resep'])
total_reciprocal_rank = 0

for user_id, rekomendasi in tf_idf['Nama_Resep'].items():
    resep_relevan = tf_idf['Nama_Resep'].get(user_id, set())
    
    # Find the rank of the first relevant item in the ranked list
    rank = next((i + 1 for i, item in enumerate(rekomendasi) if item in resep_relevan), 0)
    
    if rank > 0:
        reciprocal_rank = 1 / rank
        total_reciprocal_rank += reciprocal_rank

# Calculate Mean Reciprocal Rank (MRR)
mrr_score = total_reciprocal_rank / banyak_pengguna * 100

print("Mean Reciprocal Rank (MRR):", mrr_score,  "%")


