from JoinData import data_gabung

import pandas as pd
import re

measurements_dict_bahan_1 = {
    'measurement1': r'(fillet|sepotong|adonan|atau|atau sesuai selera|badan bawah|bagian|bagian kepala|bahab|bahan|bahannya|bajan batang|baluri|batang|bauh|bawah|bbrp|beberapa|bersihkan|besek|bgks|bh|bhan|biji|bila perlu|bila suka|biting|bj|bjs|bks|blalo bunga|)',
    'measurement2': r'(blok|bngks|bngkus|bonggol|bongkah|botol|btang|btg|btir|btng|btr|buah|buat|bubuk|bugkus|bulat|bumbu|bungkus|butih|butir|bw|campur jadi satu|cc|centong|cm|cup|cup kecil|dough|ekor|ekr|fillet|gandu|gegam|gelas|genggam|giling kasar|)',
    'measurement3': r'(gls|gr|gram|grm|haluskan|helai|hjari|ibu jari|ibujari|ikan|ikat|iket|iris|irisan|isian|jari|jari kelingking|jari telunjuk|jempol|jerohan|jumput|kaleng|kembung|kepal|kepala|keping|keranjang|kg|kilo|kl|klg|kotak|kuah|kucuri|kulit|kuntum besar|)',
    'measurement4': r'(lb|lbar|lbr|lembah|lembar|liter|lmbar|lmbr|lnb|lonjor|ltr|mangkok|mata|mika|mix|mixed|ml|ons|pack|pak|paket|panci|papan|pc|pcs|pelapis|pelengkap|pembungkus|pentol|penyedap|pindang|piring|plastik|porsi|potong|ppn|prei|ptg|ptong|pucuk)',
    'measurement5': r'(rantang|resep|ruang|ruas|ruas jari|rumpun|sacet|sach|sachet|sachset|saset|sayur|sc|sckpnya|sct|sdk|sdm|sdt|sebatang|sebongkol|secuil|secukup|secukup nya|secukup y|secukupny|secukupnya|sedikit|sedikitttt|sedok|segenggam|seibu jari|)',
    'measurement6': r'(seibujari|seikat|seiket|sejempol|sejemput|sejumput|sejumut|selera|sendok|sendok makan|sendok the|separuh|seperlunya|seporong|sepotng|sepotong|sepotong kecil|seruas|sesuai kebutuhan|sesuai keperluan|sesuai selera|seucil|seujung|seujung jari|)',
    'measurement7': r'(seujung kuku|siapkan|siuang|siung|siunh|slicce|slice|sm|st|stg|sth|tambahan|tambahkan|tangkai|tbso|tbsp|telunjuk|tetes|tin|topping|tsp|ujung sendok the|ukuran|ukuran sedang|ulas|untuk|untuk isian dan toping|wadah|)',
}

class SplitBahan:
    def __init__(self, dataset):
        self.dataset = dataset
        self.pisah_bahan = None
    
    def split_bahan_column(self):
        self.pisah_bahan = self.dataset['Bahan_Bahan'].str.split('--|\n', expand=True)
        self.pisah_bahan = self.pisah_bahan.drop(self.pisah_bahan.columns[5:78], axis=1)
    
    def remove_null_rows(self):
        self.pisah_bahan = self.pisah_bahan.dropna(subset=[0, 1, 2, 3, 4])
    
    def rename_columns(self, column_mapping):
        self.pisah_bahan = self.pisah_bahan.rename(columns=column_mapping)
    
    def display_head(self):
        print(self.pisah_bahan.head())
    
    def get_total_data(self):
        return len(self.pisah_bahan)
    
class DataParsing:
    def __init__(self, combined_dataset, pisah_bahan):
        self.combined_dataset = combined_dataset
        self.pisah_bahan = pisah_bahan
        self.parsing = None
    
    def combine_datasets(self):
        self.parsing = pd.concat([self.combined_dataset, self.pisah_bahan], axis=1)
    
    def remove_null_rows(self):
        self.parsing = self.parsing.dropna(axis=0)
    
    def remove_duplicates(self, subset):
        self.parsing = self.parsing.drop_duplicates(subset=subset, keep='first')
    
    def display_head(self):
        print(self.parsing.head())
    
    def get_total_data(self):
        return len(self.parsing)

class CaseFolding:
    def __init__(self, dataset):
        self.dataset = dataset
    
    def apply_case_folding(self, column_list):
        for column in column_list:
            self.dataset[column] = self.dataset[column].apply(lambda x: x.lower())
    
    def display_head(self):
        print(self.dataset.head())

class RegexTransformation:
    def __init__(self, dataset, measurements_dict):
        self.dataset = dataset
        self.measurements_dict = measurements_dict
    
    def apply_regex_transformation(self):
        self.dataset['Nama_Resep'] = self.dataset['Nama_Resep'].astype(str).str.replace(r"[^a-zA-Z]+", " ")
        self.dataset['Bahan_Bahan'] = self.dataset['Bahan_Bahan'].astype(str).str.replace("\n|Ã¢Â®", " ")
        self.dataset['Cara_Membuat'] = self.dataset['Cara_Membuat'].astype(str).str.replace(r"[^a-zA-Z]+", " ")
        self.dataset['Bahan_1'] = self.dataset['Bahan_1'].astype(str).str.replace(r"[^a-zA-Z]+", " ")
        self.dataset['Bahan_2'] = self.dataset['Bahan_2'].astype(str).str.replace(r"[^a-zA-Z]+", " ")
        self.dataset['Bahan_3'] = self.dataset['Bahan_3'].astype(str).str.replace(r"[^a-zA-Z]+", " ")
        self.dataset['Bahan_4'] = self.dataset['Bahan_4'].astype(str).str.replace(r"[^a-zA-Z]+", " ")
        self.dataset['Bahan_5'] = self.dataset['Bahan_5'].astype(str).str.replace(r"[^a-zA-Z]+", " ")
        
        self.dataset['Bahan_1'] = self.dataset['Bahan_1'].apply(self.remove_measurements)
        self.dataset['Bahan_2'] = self.dataset['Bahan_2'].apply(self.remove_measurements)
        self.dataset['Bahan_3'] = self.dataset['Bahan_3'].apply(self.remove_measurements)
        self.dataset['Bahan_4'] = self.dataset['Bahan_4'].apply(self.remove_measurements)
        self.dataset['Bahan_5'] = self.dataset['Bahan_5'].apply(self.remove_measurements)
    
    def remove_measurements(self, text):
        for measurements_type, pattern in self.measurements_dict.items():
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)
        return text.strip()
    
    def display_head(self):
        print(self.dataset.head())

class PhraseDetection:
    def __init__(self, tokenizing_path):
        self.tokenizing_path = tokenizing_path
        self.phrase_detection = None
    
    def load_tokenizing_data(self):
        self.phrase_detection = pd.read_csv(self.tokenizing_path, encoding='latin-1')
    
    def replace_spaces_with_dash(self):
        self.phrase_detection['Bahan_1'] = self.phrase_detection['Bahan_1'].str.replace(' ', '-')
        self.phrase_detection['Bahan_2'] = self.phrase_detection['Bahan_2'].str.replace(' ', '-')
        self.phrase_detection['Bahan_3'] = self.phrase_detection['Bahan_3'].str.replace(' ', '-')
        self.phrase_detection['Bahan_4'] = self.phrase_detection['Bahan_4'].str.replace(' ', '-')
        self.phrase_detection['Bahan_5'] = self.phrase_detection['Bahan_5'].str.replace(' ', '-')
    
    def generate_token_column(self):
        self.phrase_detection['Token'] = self.phrase_detection.apply(
            lambda x: x['Bahan_1'] + ' ' + x['Bahan_2'] + ' ' + x['Bahan_3'] + ' ' + x['Bahan_4'] + ' ' + x['Bahan_5'],
            axis=1
        )
    
    def display_head(self):
        print(self.phrase_detection.head())

pisah_bahan_processor = SplitBahan(data_gabung.combined_dataset)

pisah_bahan_processor.split_bahan_column()
pisah_bahan_processor.remove_null_rows()

pisah_bahan_column_mapping = {
    0: 'Bahan_1',
    1: 'Bahan_2',
    2: 'Bahan_3',
    3: 'Bahan_4',
    4: 'Bahan_5'
}

pisah_bahan_processor.rename_columns(pisah_bahan_column_mapping)

pisah_bahan_processor.display_head()

total_dataset_pisahbahan = pisah_bahan_processor.get_total_data()
print("Total data:", total_dataset_pisahbahan)

data_parser = DataParsing(data_gabung.combined_dataset, pisah_bahan_processor.pisah_bahan)

data_parser.combine_datasets()
data_parser.remove_null_rows()

duplicate_columns = ['Nama_Resep', 'Bahan_Bahan']

data_parser.remove_duplicates(duplicate_columns)
data_parser.display_head()

total_dataset_parsing = data_parser.get_total_data()
print("Total data:", total_dataset_parsing)

case_folding_columns = ['Nama_Resep', 'Bahan_Bahan', 'Cara_Membuat', 'Bahan_1', 'Bahan_2', 'Bahan_3', 'Bahan_4', 'Bahan_5']

case_folder = CaseFolding(data_parser.parsing)
case_folder.apply_case_folding(case_folding_columns)
case_folder.display_head()

regex_transformer = RegexTransformation(case_folder.dataset, measurements_dict_bahan_1)
regex_transformer.apply_regex_transformation()
regex_transformer.display_head()

tokenizing_path = 'Tokenizing.csv'
phrase_detection_processor = PhraseDetection(tokenizing_path)

phrase_detection_processor.load_tokenizing_data()
phrase_detection_processor.replace_spaces_with_dash()
phrase_detection_processor.generate_token_column()
phrase_detection_processor.display_head()
