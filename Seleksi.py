from MuatDataset import tempe_loader, telur_loader, udang_loader, sayur_loader, buah_loader

class PilihKolom:
    def __init__(self, dataset, columns):
        self.dataset = dataset
        self.columns = columns
        self.selection = None
    
    def pilih_kolom(self):
        self.selection = self.dataset[self.columns]
    
    def tampil_head(self):
        if self.selection is not None:
            print(self.selection.head())
        else:
            print("Seleksi Belum Dimuat")


seleksi_tempe = PilihKolom(tempe_loader.data, ["Title", "Ingredients", "Steps"])
seleksi_telur = PilihKolom(telur_loader.data, ["Title", "Ingredients", "Steps"])
seleksi_udang = PilihKolom(udang_loader.data, ["Title", "Ingredients", "Steps"])
seleksi_sayur = PilihKolom(sayur_loader.data, ["NAMA_RESEP", "BAHAN", "CARA_MEMBUAT"])
seleksi_buah = PilihKolom(buah_loader.data, ["NAMA_RESEP", "BAHAN", "CARA_MEMBUAT"])

seleksi_tempe.pilih_kolom()
seleksi_telur.pilih_kolom()
seleksi_udang.pilih_kolom()
seleksi_sayur.pilih_kolom()
seleksi_buah.pilih_kolom()

print("=== Selected Tempe Dataset ===")
seleksi_tempe.tampil_head()

print("=== Selected Telur Dataset ===")
seleksi_telur.tampil_head()

print("=== Selected Udang Dataset ===")
seleksi_udang.tampil_head()

print("=== Selected Sayur Dataset ===")
seleksi_sayur.tampil_head()

print("=== Selected Buah Dataset ===")
seleksi_buah.tampil_head()