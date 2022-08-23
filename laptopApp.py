import streamlit as st
import pandas as pd
import numpy as np
import pickle
# import base64
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

st.header('Aplikasi Prediksi Harga Laptop')

st.write("""
Adalah sebuah aplikasi untuk memprediksi harga laptop berdasarkan atribut yang telah disediakan pada sidebar

""")

def user_input_features():
    processor = st.sidebar.selectbox('Processor',('Intel® Celeron® processor',
       '11th Generation Intel® Core i7 processor',
       'AMD Athlon Silver processor', 'AMD Ryzen 5 processor',
       'AMD Ryzen 7 processor',
       '11th Generation Intel® Core i5 processor', 'Intel Core I3',
       'Intel Core I7', 'AMD 7th Gen', 'Intel® Core™ i7 7500U',
       'Intel® Core™ i3 6006U', 'Intel Core i5-8250U',
       'Intel Core i3-8145U', 'Intel Core i7-10510U',
       'Intel Core i3-7020U', 'Intel Core i7-8550U',
       'Intel Core i7-7700HQ', 'AMD A4', 'Intel Core I5',
       'AMD Ryzen 5 5500U', 'AMD Ryzen 5000',
       'Intel Pentium Silver N6000', 'Intel® Core™ i5-1240P',
       'Intel Core i5-1135G7', 'Intel Celeron N5100',
       'Intel Core i5-7300HQ', 'Intel Core i9'))
    os = st.sidebar.selectbox('Os',('Windows 11 Home', 'Windows 10 Home 64',
       'Windows 10 Home Single Language 64', 'Windows 10',
       'Windows 10 Home', 'Windows 11 Home 64'))
    vga = st.sidebar.selectbox('Vga',('Intel® UHD Graphics 600', 'Intel® Iris® Xe Graphics',
       'NVIDIA® GeForce® MX450 (2 GB GDDR5 dedicated)',
       'AMD Radeon Graphics',
       'NVIDIA® GeForce RTX 3060 Laptop GPU (6 GB GDDR6 dedicated)',
       'NVIDIA® GeForce RTX 3070 Laptop GPU (8 GB GDDR6 dedicated)',
       'NVIDIA® GeForce® GTX 1650 (4 GB GDDR6 dedicated)',
       'NVIDIA® GeForce RTX 3050 Laptop GPU (4 GB GDDR6 dedicated)',
       'Intel HD Graphics 520', 'Nvidia GeForce GT930MX', 'AMD Radeon R5',
       'Nvidia GeForce GT 930MX 2 GB', 'NVIDIA GeForce 920MX 2GB',
       'AMD Radeon 530 2GB', 'Nvidia GeForce MX130 2GB',
       'Nvidia GeForce MX230 2GB', 'Intel UHD Graphocs 620',
       'Nvidia GeForce MX150 2GB', 'Nvidia GeForce GTX 1050 Ti 4GB',
       'AMD Radeon R3', 'AMD Radeon M535', 'Nvidia Geforce GT940MX',
       'NVIDIA GeForce RTX 3050', 'Intel UHD Graphics',
       'Intel Iris Xe Graphics', 'NVIDIA GeForce GTX 1050 Ti',
       'NVIDIA GeForce RTX 3070'))
    ram = st.sidebar.selectbox('Ram',('4 GB', '16 GB', '32 GB', '8 GB'))

    data = {'Processor':[processor], 

            'Os':[os],
            'Vga':[vga],
            'Ram':[ram]
            }
    features = pd.DataFrame(data)

    return features

df = user_input_features()
st.subheader('User Input parameters')
processor = {'Intel® Celeron® processor' : 1,
       '11th Generation Intel® Core i7 processor' : 2,
       'AMD Athlon Silver processor' : 3, 'AMD Ryzen 5 processor' : 4,
       'AMD Ryzen 7 processor' : 5,
       '11th Generation Intel® Core i5 processor' : 6, 'Intel Core I3' : 7,
       'Intel Core I7' : 8, 'AMD 7th Gen' : 9, 'Intel® Core™ i7 7500U' : 10,
       'Intel® Core™ i3 6006U' : 11, 'Intel Core i5-8250U' : 12,
       'Intel Core i3-8145U' : 13, 'Intel Core i7-10510U' : 14,
       'Intel Core i3-7020U' : 15, 'Intel Core i7-8550U' : 16,
       'Intel Core i7-7700HQ' : 17, 'AMD A4' : 18, 'Intel Core I5' : 19,
       'AMD Ryzen 5 5500U' : 20, 'AMD Ryzen 5000' : 21,
       'Intel Pentium Silver N6000' : 22, 'Intel® Core™ i5-1240P' : 23,
       'Intel Core i5-1135G7' : 24, 'Intel Celeron N5100' : 25,
       'Intel Core i5-7300HQ' : 26, 'Intel Core i9' : 27}
df['Processor'] = df['Processor'].replace(processor)

os = {'Windows 11 Home' : 1, 'Windows 10 Home 64' : 2,
       'Windows 10 Home Single Language 64' : 3, 'Windows 10' : 4,
       'Windows 10 Home' : 5, 'Windows 11 Home 64' : 6}
df['Os'] = df['Os'].replace(os)

vga = {'Intel® UHD Graphics 600' : 1, 'Intel® Iris® Xe Graphics' : 2,
       'NVIDIA® GeForce® MX450 (2 GB GDDR5 dedicated)' : 3,
       'AMD Radeon Graphics' : 4,
       'NVIDIA® GeForce RTX 3060 Laptop GPU (6 GB GDDR6 dedicated)' : 5,
       'NVIDIA® GeForce RTX 3070 Laptop GPU (8 GB GDDR6 dedicated)' : 6,
       'NVIDIA® GeForce® GTX 1650 (4 GB GDDR6 dedicated)' : 7,
       'NVIDIA® GeForce RTX 3050 Laptop GPU (4 GB GDDR6 dedicated)' : 8,
       'Intel HD Graphics 520' : 9, 'Nvidia GeForce GT930MX' : 10, 'AMD Radeon R5' : 11,
       'Nvidia GeForce GT 930MX 2 GB' : 12, 'NVIDIA GeForce 920MX 2GB' : 13,
       'AMD Radeon 530 2GB' : 14, 'Nvidia GeForce MX130 2GB' : 15,
       'Nvidia GeForce MX230 2GB' : 16, 'Intel UHD Graphocs 620' : 17,
       'Nvidia GeForce MX150 2GB' : 18, 'Nvidia GeForce GTX 1050 Ti 4GB' : 19,
       'AMD Radeon R3' : 20 , 'AMD Radeon M535' : 21, 'Nvidia Geforce GT940MX' : 22,
       'NVIDIA GeForce RTX 3050' : 23, 'Intel UHD Graphics' : 24,
       'Intel Iris Xe Graphics' : 25, 'NVIDIA GeForce GTX 1050 Ti' : 26,
       'NVIDIA GeForce RTX 3070' : 27}
df['Vga'] = df['Vga'].replace(vga)
df['Ram'] = df['Ram'].apply(lambda x: x[:2].strip())

st.write(df)
model = pickle.load(open('dataset_laptop_fix.pkl', 'rb'))

prediction = model.predict(df)
st.subheader('Prediction')
st.write(prediction)