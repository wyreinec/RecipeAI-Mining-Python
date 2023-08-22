import numpy as np
import pandas as pd
from Seleksi import seleksi_tempe, seleksi_telur, seleksi_udang, seleksi_sayur, seleksi_buah

class HapusNaNDuplicate:
    def __init__(self, dataset):
        self.dataset = dataset
    
    def dropna(self):
        self.dataset = self.dataset.replace(to_replace='None', value=np.nan).dropna()
    
    def drop_duplikat(self):
        self.dataset = self.dataset.drop_duplicates(keep='last')
    
    def drop_kolom(self, columns_to_drop):
        self.dataset = self.dataset.drop(columns=columns_to_drop)
    
    def tampil_head(self):
        print(self.dataset.head())
    
    def export_to_csv(self, filename):
        self.dataset.to_csv(filename, index=False)

tempe_preprocessor = HapusNaNDuplicate(seleksi_tempe.selection)
telur_preprocessor = HapusNaNDuplicate(seleksi_telur.selection)
udang_preprocessor = HapusNaNDuplicate(seleksi_udang.selection)
sayur_preprocessor = HapusNaNDuplicate(seleksi_sayur.selection)
buah_preprocessor = HapusNaNDuplicate(seleksi_buah.selection)

tempe_preprocessor.dropna()
tempe_preprocessor.drop_duplikat()
tempe_preprocessor.export_to_csv('nanduplicate-tempe.csv')

telur_preprocessor.dropna()
telur_preprocessor.drop_duplikat()
telur_preprocessor.export_to_csv('nanduplicate-telur.csv')

udang_preprocessor.dropna()
udang_preprocessor.drop_duplikat()
udang_preprocessor.export_to_csv('nanduplicate-udang.csv')

sayur_preprocessor.dropna()
sayur_preprocessor.drop_duplikat()
sayur_preprocessor.export_to_csv('nanduplicate-sayur.csv')

buah_preprocessor.dropna()
buah_preprocessor.drop_duplikat()
buah_preprocessor.export_to_csv('nanduplicate-buah.csv')
