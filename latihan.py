import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca file CSV
data = pd.read_csv('nilai_siswa.csv')

# Informasi dataset
print("=== INFORMASI DATA ===")
print(data.info())

print("\n=== 5 DATA PERTAMA ===")
print(data.head())

# Statistik deskriptif
print("\n=== STATISTIK DESKRIPTIF ===")
print(data.describe())

# Ukuran pemusatan data
print("\n=== UKURAN PEMUSATAN DATA ===")
print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

# Nilai maksimum & minimum per mapel
print("\n=== NILAI MAKSIMUM & MINIMUM PER MAPEL ===")
print(data.groupby('Mapel')['Nilai'].agg(['max', 'min']))

# Grafik batang rata-rata nilai per mapel
rata = data.groupby('Mapel')['Nilai'].mean()
rata.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Rata-Rata Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.xticks(rotation=30)
plt.show()

# Boxplot sebaran nilai per mapel
sns.boxplot(x='Mapel', y='Nilai', data=data, palette='pastel')
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai')
plt.show()