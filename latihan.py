import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Hello, Streamlit!')
st.write('This is a simple Streamlit application.')

st.write('Ini contoh *huruf miring*')
st.write('Ini contoh **huruf tebal**')
st.write('Ini contoh ***huruf tebal & miring***')

penjualan_oktober = 900
penjualan_november = 800
penjualan_desember = 1000

selisih1 = penjualan_desember - penjualan_november
selisih2 = penjualan_november - penjualan_oktober

st.metric(label='Penjualan sekarang', value = penjualan_desember, delta = selisih1)
st.metric(label='Penjualan sebelumnya', value = penjualan_desember, delta = selisih2)

df = pd.read_csv('healthcare-dataset-stroke-data.csv')
st.dataframe(df)

st.write('**Visualisasi Data - Jumlah Pasien Berdasarkan Usia**')
st.line_chart(df['age'].value_counts().sort_index())

st.write('**Visualisasi Data - Tipe Pekerjaan**')
st.bar_chart(df['work_type'].value_counts().sort_index())

st.write('**Visualisasi Data - Jenis Kelamin**')
category_df = df['gender'].value_counts(dropna=False).reset_index()
category_df.columns = ['gender', 'count']
fig = px.pie(category_df, names = 'gender', values = 'count')
st.plotly_chart(fig, use_container_width=True)

st.write('**Visualisasi Data - Penggabungan 2 kolom sekaligus**')
col1, col2 = st.columns([6,4])
with col1:
    st.bar_chart(df['work_type'].value_counts().sort_index())
with col2:
    st.line_chart(df['age'].value_counts().sort_index())

st.write('**Visualisasi Data - Penggabungan 3 kolom sekaligus**')
col1, col2, col3 = st.columns(3)
with col1:
    st.write('Ini contoh *huruf miring*')
    st.write('Ini contoh **huruf tebal**')
    st.write('Ini contoh ***huruf tebal & miring***')
with col2:
    st.metric(label='Penjualan sekarang', value = penjualan_desember, delta = selisih1)
with col3:
    st.metric(label='Penjualan sebelumnya', value = penjualan_desember, delta = selisih2)

#Interaktif Komponen
st.write('**Button**')
st.button('Reset', type = 'primary')
if st.button('Say Hello'):
    st.write('Why hellow there')
else:
    st.write('Goodbye')
if st.button('Aloha', type ='tertiary'):
    st.write('Ciao')

st.write('**Membuat Tab pada visualisasi**')
tab1, tab2 = st.tabs(['line', 'Bar'])
with tab1:
    st.line_chart(df['age'].value_counts().sort_index())
with tab2:
    st.bar_chart(df['work_type'].value_counts().sort_index())

#Checkbox
st.write('**CheckBox**')
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

#Multiselect
st.write('**Multiselect**')
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'],
)
st.write('You selected:', options)
