#visualisasi streamlit

import numpy
import math
import pandas
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