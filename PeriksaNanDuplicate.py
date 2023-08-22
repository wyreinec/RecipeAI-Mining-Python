from Seleksi import seleksi_tempe, seleksi_telur, seleksi_udang, seleksi_sayur, seleksi_buah

class PeriksaNaNDuplicate:
    def __init__(self, dataset, column_mapping):
        self.dataset = dataset
        self.column_mapping = column_mapping
        self.null_counts = {}
        self.total_duplicates = None
        self.duplicate_counts = {}
    
    def cek_nilai_null(self):
        for column_name, display_name in self.column_mapping.items():
            self.null_counts[display_name] = self.dataset[column_name].isnull().sum()
    
    def tampil_total_null(self):
        for column_name, null_count in self.null_counts.items():
            print(f'Data Kosong di {column_name}: {null_count}')
        print(f'Total Data Kosong: {sum(self.null_counts.values())}')

    def cek_duplikat(self):
        self.total_duplicates = self.dataset.duplicated().sum()
        
        for column_name, display_name in self.column_mapping.items():
            self.duplicate_counts[display_name] = self.dataset[column_name].duplicated().sum()
    
    def tampil_total_duplikat(self):
        print(f'Duplikasi Resep Total: {self.total_duplicates}')
        for column_name, duplicate_count in self.duplicate_counts.items():
            print(f'Duplikasi {column_name}: {duplicate_count}')

kolom_tempe = {'Title': 'Nama Resep', 'Ingredients': 'Bahan', 'Steps': 'Cara Membuat'}
kolom_telur = {'Title': 'Nama Resep', 'Ingredients': 'Bahan', 'Steps': 'Cara Membuat'}
kolom_udang = {'Title': 'Nama Resep', 'Ingredients': 'Bahan', 'Steps': 'Cara Membuat'}
kolom_sayur = {'NAMA_RESEP': 'Nama Resep', 'BAHAN': 'Bahan', 'CARA_MEMBUAT': 'Cara Membuat'}
kolom_buah = {'NAMA_RESEP': 'Nama Resep', 'BAHAN': 'Bahan', 'CARA_MEMBUAT': 'Cara Membuat'}

cek_null_tempe = PeriksaNaNDuplicate(seleksi_tempe.selection, kolom_tempe)
cek_null_telur = PeriksaNaNDuplicate(seleksi_telur.selection, kolom_telur)
cek_null_udang = PeriksaNaNDuplicate(seleksi_udang.selection, kolom_udang)
cek_null_sayur = PeriksaNaNDuplicate(seleksi_sayur.selection, kolom_sayur)
cek_null_buah = PeriksaNaNDuplicate(seleksi_buah.selection, kolom_buah)

cek_null_tempe.cek_nilai_null()
cek_null_tempe.tampil_total_null()

cek_null_telur.cek_nilai_null()
cek_null_telur.tampil_total_null()

cek_null_udang.cek_nilai_null()
cek_null_udang.tampil_total_null()

cek_null_sayur.cek_nilai_null()
cek_null_sayur.tampil_total_null()

cek_null_buah.cek_nilai_null()
cek_null_buah.tampil_total_null()

tempe_columns = {'Title': 'Nama Resep', 'Ingredients': 'Bahan', 'Steps': 'Cara Membuat'}
telur_columns = {'Title': 'Nama Resep', 'Ingredients': 'Bahan', 'Steps': 'Cara Membuat'}
udang_columns = {'Title': 'Nama Resep', 'Ingredients': 'Bahan', 'Steps': 'Cara Membuat'}
sayur_columns = {'NAMA_RESEP': 'Nama Resep', 'BAHAN': 'Bahan', 'CARA_MEMBUAT': 'Cara Membuat'}
buah_columns = {'NAMA_RESEP': 'Nama Resep', 'BAHAN': 'Bahan', 'CARA_MEMBUAT': 'Cara Membuat'}

cek_duplikat_tempe = PeriksaNaNDuplicate(seleksi_tempe.selection, tempe_columns)
cek_duplikat_telur = PeriksaNaNDuplicate(seleksi_telur.selection, telur_columns)
cek_duplikat_udang = PeriksaNaNDuplicate(seleksi_udang.selection, udang_columns)
cek_duplikat_sayur = PeriksaNaNDuplicate(seleksi_sayur.selection, sayur_columns)
cek_duplikat_buah = PeriksaNaNDuplicate(seleksi_buah.selection, buah_columns)

cek_duplikat_tempe.cek_duplikat()
cek_duplikat_tempe.tampil_total_duplikat()

cek_duplikat_telur.cek_duplikat()
cek_duplikat_telur.tampil_total_duplikat()

cek_duplikat_udang.cek_duplikat()
cek_duplikat_udang.tampil_total_duplikat()

cek_duplikat_sayur.cek_duplikat()
cek_duplikat_sayur.tampil_total_duplikat()

cek_duplikat_buah.cek_duplikat()
cek_duplikat_buah.tampil_total_duplikat()