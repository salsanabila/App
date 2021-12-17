# Salsa Nabila
# 12220111
# UAS Pemrograman Komputer

from numpy.lib.function_base import append
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import streamlit as st

file = pd.read_csv("produksi_minyak_mentah.csv")
print (file)

kode_unique = list(file["kode_negara"].unique())
print(kode_unique)

jumlah_produksi = []
for kode_negara in kode_unique:
    produksi = file.replace(",","")[file["kode_negara"]==kode_negara].shape[0]
    jumlah_produksi.append(produksi)
print("Jumlah produksi:", jumlah_produksi)

produksi_max = []
for kode_negara in kode_unique:
    produksi = file[file["kode_negara"]==kode_negara]["produksi"]
    produksi_max = np.asarray(produksi).max()
print(produksi_max)

year = []
for tahun in file:
    tahun = file[file["tahun"]==tahun].shape[0]
    year.append(tahun)
print(year)

plt.bar(kode_unique,jumlah_produksi)
plt.legend(labels = ["tahun"])
plt.title("Grafik Jumlah Produksi suatu Negara terhadap Tahun")
plt.xlabel("negara")
plt.ylabel("produksi")
plt.show()

plt.scatter(tahun, produksi_max)
plt.legend(labels = ["produksi maksimal"])
plt.title("Grafik Produksi Maksimal suatu Negara terhadap Tahun")
plt.xlabel("tahun")
plt.ylabel("maksimal produksi")
plt.show()

plt.scatter(kode_negara, produksi_max)
plt.legend(labels = ["produksi maksimal kumulatif"])
plt.title("Grafik Produksi Maksimal suatu Negara terhadap Tahun")
plt.xlabel("negara")
plt.ylabel("maksimal produksi")
plt.show()