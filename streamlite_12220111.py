#visualisasi streamlit

from numpy.lib.function_base import append
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout="wide")
st.title("Tren Produksi Minyak Mentah")
st.sidebar.title("Pengaturan")
left_col, mid_col, right_col = st.columns(3)
st.sidebar.subheader("Pengaturan Tampilan")
list_negara = ['AUS', 'AUT', 'BEL', 'CAN', 'CZE', 'DNK', 'FIN', 'FRA', 'DEU', 
'GRC', 'HUN', 'ISL', 'IRL', 'ITA', 'JPN', 'KOR', 'LUX', 'MEX', 'NLD', 'NZL', 
'NOR', 'POL', 'PRT', 'SVK', 'ESP', 'SWE', 'CHE', 'TUR', 'GBR', 'USA', 'OEU', 
'ALB', 'DZA', 'ARG', 'ARM', 'AZE', 'BGD', 'BLR', 'BIH', 'BRA', 'BRN', 'BGR', 
'KHM', 'CHL', 'CHN', 'COL', 'HRV', 'CYP', 'EGY', 'EST', 'ETH', 'GEO', 'GHA', 
'HTI', 'HKG', 'IND', 'IDN', 'IRN', 'ISR', 'KAZ', 'LVA', 'LTU', 'MKD', 'MYS', 
'MLT', 'MDA', 'MOZ', 'NGA', 'PAK', 'PRY', 'PER', 'PHL', 'ROU', 'RUS', 'SAU', 
'SGP', 'SVN', 'ZAF', 'SDN', 'TWN', 'TZA', 'THA', 'UKR', 'ARE', 'URY', 'VNM', 
'ZMB', 'WLD', 'SRB', 'MNE', 'EU28', 'G20', 'OECD', 'AGO', 'BHR', 'BEN', 'BOL', 
'BWA', 'CMR', 'COG', 'CRI', 'CIV', 'CUB', 'PRK', 'COD', 'DOM', 'ECU', 'SLV', 
'ERI', 'GAB', 'GTM', 'HND', 'IRQ', 'JAM', 'JOR', 'KEN', 'KWT', 'KGZ', 'LBN', 
'LBY', 'MNG', 'MAR', 'MMR', 'NAM', 'NPL', 'NIC', 'NER', 'OMN', 'PAN', 'QAT', 
'SEN', 'LKA', 'SYR', 'TJK', 'TGO', 'TTO', 'TUN', 'TKM', 'UZB', 'VEN', 'YEM', 
'ZWE']
negara = st.sidebar.selectbox("pilih negara", list_negara)

from numpy.lib.function_base import append
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

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