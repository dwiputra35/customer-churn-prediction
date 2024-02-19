import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



def run():


    # Membuat Sub Header
    st.subheader('Churn Prediction')

    # Menambahkan Deskripsi
    st.write('Project ini dibuat untuk memenuhi tugas Milestone 1 Phase 2 di Hacktiv8 Indonesia dengan tujuan mengembangkan model prediksi churn yang akurat dan memberikan wawasan berharga kepada perusahaan untuk mengambil tindakan proaktif dalam menjaga kepuasan pelanggan dan meminimalkan risiko churn.')

    # Membuat pembatas
    st.markdown('---')


    st.write('Created by: [Dwi Putra Satria Utama](https://www.linkedin.com/in/dwiputra3500/)')

if __name__ == '__main__':
    run()