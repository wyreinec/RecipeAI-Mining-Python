import pandas as pd
from DataTransformasi import tempe_transformer, telur_transformer, udang_transformer, sayur_transformer, buah_transformer

class JoinData:
    def __init__(self, transformers):
        self.transformers = transformers
        self.combined_dataset = None
    
    def join_dataset(self):
        datasets = [transformer.dataset for transformer in self.transformers]
        self.combined_dataset = pd.concat(datasets, ignore_index=True)
    
    def rename_kolom(self, column_mapping):
        self.combined_dataset = self.combined_dataset.rename(columns=column_mapping)
    
    def tampil_head(self):
        print(self.combined_dataset.head())
    
    def get_total_data(self):
        return len(self.combined_dataset)
    
    def export_to_csv(self, filename):
        self.combined_dataset.to_csv(filename, index=False)

transformers = [tempe_transformer, telur_transformer, udang_transformer, sayur_transformer, buah_transformer]

combined_column_mapping = {
    'NAMA_RESEP': 'Nama_Resep',
    'BAHAN': 'Bahan_Bahan',
    'CARA_MEMBUAT': 'Cara_Membuat'
}

data_gabung = JoinData(transformers)

data_gabung.join_dataset()
data_gabung.rename_kolom(combined_column_mapping)
data_gabung.tampil_head()

total_dataset_gabung = data_gabung.get_total_data()
print("Total data:", total_dataset_gabung)

# Export the combined dataset to CSV
data_gabung.export_to_csv('dataset-gabung.csv')
