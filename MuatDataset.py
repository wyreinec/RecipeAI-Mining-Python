import pandas as pd

class MuatDataset:
    def __init__(self, filename):
        self.filename = filename
        self.data = None
    
    def muat_data(self):
        self.data = pd.read_csv(self.filename)
    
    def tampil_head(self):
        if self.data is not None:
            print(self.data.head())
        else:
            print("Dataset belum dimuat")


dataset_tempe = pd.read_csv('dataset-tempe.csv')
dataset_telur = pd.read_csv('dataset-telur.csv')
dataset_udang = pd.read_csv('dataset-udang.csv')
dataset_sayur = pd.read_csv('dataset-sayur.csv')
dataset_buah = pd.read_csv('dataset-buah.csv')

tempe_loader = MuatDataset('dataset-tempe.csv')
telur_loader = MuatDataset('dataset-telur.csv')
udang_loader = MuatDataset('dataset-udang.csv')
sayur_loader = MuatDataset('dataset-sayur.csv')
buah_loader = MuatDataset('dataset-buah.csv')

tempe_loader.muat_data()
telur_loader.muat_data()
udang_loader.muat_data()
sayur_loader.muat_data()
buah_loader.muat_data()

print("=== Tempe Dataset ===")
tempe_loader.tampil_head()

print("=== Telur Dataset ===")
telur_loader.tampil_head()

print("=== Udang Dataset ===")
udang_loader.tampil_head()

print("=== Sayur Dataset ===")
sayur_loader.tampil_head()

print("=== Buah Dataset ===")
buah_loader.tampil_head()