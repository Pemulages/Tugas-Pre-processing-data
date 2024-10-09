import pandas as pd

# langkah - langkahnyaa
# Memuat dataset dari file valve player data
file_path = 'Valve_Player_Data.csv'
df = pd.read_csv(file_path)

# Menampilkan beberapa baris pertama dari dataset
df.head()

# 1. Mengubah kolom Percent_Gain jadi angka (membersihkan tanda % dan mengubah ke float)
df['Percent_Gain'] = df['Percent_Gain'].str.replace('%', '').astype(float)

# 2. Mengubah kolom Month_Year dan Date jadi tipe datetime
df['Month_Year'] = pd.to_datetime(df['Month_Year'], format='%B %Y')
df['Date'] = pd.to_datetime(df['Date'])

# 3. Menghapus kolom URL dan jika tidak relevan/penting
df_cleaned = df.drop(columns=['URL'])

# 4. Memeriksa apakah ada yg missing values
missing_values = df_cleaned.isnull().sum()

df_cleaned.head(), missing_values

# Mengisi missing values di kolom Gain dan Percent_Gain dengan rata-rata pada masing kolomny
df_cleaned['Gain'] = df_cleaned['Gain'].fillna(df_cleaned['Gain'].mean())
df_cleaned['Percent_Gain'] = df_cleaned['Percent_Gain'].fillna(df_cleaned['Percent_Gain'].mean())
df_cleaned.replace([float('inf'), float('-inf')], pd.NA, inplace=True)
df_cleaned.dropna(inplace=True)  # Jika ingin menghapus baris dengan nilai inf

# Memeriksa kembali apakah masih ada missing values
missing_values_after = df_cleaned.isnull().sum()
df_cleaned.head(), missing_values_after

# Utk Menampilkan 5 baris pertama dari dataset yang sudah diproses
# print(df_cleaned.head())

# Utk Menampilkan semua kolom dari dataset yang sudah diproses
print(df_cleaned)

# Menampilkan informasi apakah masih ada missing values
print("\nMissing values setelah pre-processing data:")
print(df_cleaned.isnull().sum())
