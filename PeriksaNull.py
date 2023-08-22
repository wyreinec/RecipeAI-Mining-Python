from Seleksi import seleksi_tempe, seleksi_telur, seleksi_udang, seleksi_sayur, seleksi_buah

class PeriksaNull:
    def __init__(self, dataset, column_mapping):
        self.dataset = dataset
        self.column_mapping = column_mapping
        self.null_counts = {}
    
    def cek_nilai_null(self):
        for column_name, display_name in self.column_mapping.items():
            self.null_counts[display_name] = self.dataset[column_name].isnull().sum()
    
    def tampil_total_null(self):
        for column_name, null_count in self.null_counts.items():
            print(f'Data Kosong di {column_name}: {null_count}')
        print(f'Total Data Kosong: {sum(self.null_counts.values())}')

kolom_tempe = {'Title': 'Nama Resep', 'Ingredients': 'Bahan', 'Steps': 'Cara Membuat'}
kolom_telur = {'Title': 'Nama Resep', 'Ingredients': 'Bahan', 'Steps': 'Cara Membuat'}
kolom_udang = {'Title': 'Nama Resep', 'Ingredients': 'Bahan', 'Steps': 'Cara Membuat'}
kolom_sayur = {'NAMA_RESEP': 'Nama Resep', 'BAHAN': 'Bahan', 'CARA_MEMBUAT': 'Cara Membuat'}
kolom_buah = {'NAMA_RESEP': 'Nama Resep', 'BAHAN': 'Bahan', 'CARA_MEMBUAT': 'Cara Membuat'}

cek_null_tempe = PeriksaNull(seleksi_tempe.selection, kolom_tempe)
cek_null_telur = PeriksaNull(seleksi_telur.selection, kolom_telur)
cek_null_udang = PeriksaNull(seleksi_udang.selection, kolom_udang)
cek_null_sayur = PeriksaNull(seleksi_sayur.selection, kolom_sayur)
cek_null_buah = PeriksaNull(seleksi_buah.selection, kolom_buah)

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