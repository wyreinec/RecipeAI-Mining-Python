from HapusNaNDuplicate import tempe_preprocessor, telur_preprocessor, udang_preprocessor, sayur_preprocessor, buah_preprocessor

class DataTransformasi:
    def __init__(self, dataset, column_mapping):
        self.dataset = dataset
        self.column_mapping = column_mapping
    
    def rename_kolom(self):
        self.dataset = self.dataset.rename(columns=self.column_mapping)
    
    def tambah_kolom(self, column_name, column_value):
        self.dataset[column_name] = column_value
    
    def tampil_head(self):
        print(self.dataset.head())

    def export_to_csv(self, filename):
        self.dataset.to_csv(filename, index=False)

column_mapping = {
    'Title': 'NAMA_RESEP',
    'Ingredients': 'BAHAN',
    'Steps': 'CARA_MEMBUAT'
}

dataset_tempe = tempe_preprocessor.dataset
dataset_telur = telur_preprocessor.dataset
dataset_udang = udang_preprocessor.dataset
dataset_sayur = sayur_preprocessor.dataset
dataset_buah = buah_preprocessor.dataset

tempe_transformer = DataTransformasi(dataset_tempe, column_mapping)
telur_transformer = DataTransformasi(dataset_telur, column_mapping)
udang_transformer = DataTransformasi(dataset_udang, column_mapping)
sayur_transformer = DataTransformasi(dataset_sayur, column_mapping)
buah_transformer = DataTransformasi(dataset_buah, column_mapping)

tempe_transformer.rename_kolom()
tempe_transformer.tambah_kolom('Jenis_Resep', 'tempe')
tempe_transformer.tampil_head()
tempe_transformer.export_to_csv('transformasi-tempe.csv')

telur_transformer.rename_kolom()
telur_transformer.tambah_kolom('Jenis_Resep', 'telur')
telur_transformer.tampil_head()
telur_transformer.export_to_csv('transformasi-telur.csv')

udang_transformer.rename_kolom()
udang_transformer.tambah_kolom('Jenis_Resep', 'udang')
udang_transformer.tampil_head()
udang_transformer.export_to_csv('transformasi-udang.csv')

sayur_transformer.rename_kolom()
sayur_transformer.tambah_kolom('Jenis_Resep', 'sayur')
sayur_transformer.tampil_head()
sayur_transformer.export_to_csv('transformasi-sayur.csv')

buah_transformer.rename_kolom()
buah_transformer.tambah_kolom('Jenis_Resep', 'buah')
buah_transformer.tampil_head()
buah_transformer.export_to_csv('transformasi-buah.csv')
