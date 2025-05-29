import pandas as pd
import glob
import os

# Caminho para os arquivos CSV
csv_folder = './raw_data/'
csv_files = glob.glob(os.path.join(csv_folder, 'Meganium_Sales_Data_*.csv'))

# Lê e concatena todos os arquivos
df_list = [pd.read_csv(f) for f in csv_files]
df_concat = pd.concat(df_list, ignore_index=True)

# Salva o resultado em um novo arquivo
df_concat.to_csv('./compiled_sales_data.csv', index=False)

print(f'Compilado {len(csv_files)} arquivos em compiled_sales_data.csv')