import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


def run():

    # title
    st.title('Churn Prediction')

    # sub header
    st.subheader('Kemungkinan berhenti berlangganan atau tidak pada customer ')

    # gambar
    image = Image.open('image.jpg')
    st.image(image, caption='')

    # deskripsi
    st.write('Created by: [Dwi Putra Satria Utama](https://www.linkedin.com/in/dwiputra3500/)')

    # garis pembatas
    st.markdown('---')

    # dataframe
    df = pd.read_csv('churn.csv')

    # sub header
    st.subheader('Data yang paling berpengaruh terhadap kemungkinan berhenti berlangganan')

    # Membuat clustered bar plot untuk korelasi antara churn_risk_score dan region_category
    fig = plt.figure(figsize=(10, 6))
    sns.countplot(x='region_category', hue='churn_risk_score', data=df, palette='viridis')
    plt.legend(title='Customer berhenti berlangganan atau tidak', loc='upper right', labels=['Tidak berhenti', 'Berhenti'])
    plt.title('Korelasi antara churn_risk_score dan Status region_category')
    plt.xlabel('region_category')
    plt.ylabel('Jumlah')
    st.pyplot(fig)

    st.write('Berdasarkan grafik tersebut, Town memiliki jumlah customer berhenti tertinggi disusul dengan City dan Village.')
    
    # garis pembatas
    st.markdown('---')

    # Membuat clustered bar plot untuk korelasi antara churn_risk_score dan membership_category
    fig = plt.figure(figsize=(10, 6))
    sns.countplot(x='membership_category', hue='churn_risk_score', data=df, palette='viridis')
    plt.legend(title='Customer berhenti berlangganan atau tidak', loc='upper right', labels=['Tidak berhenti', 'Berhenti'])
    plt.title('Korelasi antara churn_risk_score dan membership_category')
    plt.xlabel('membership_category')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

    st.write('Berdasarkan grafik tersebut, hanya platinum membership yang tidak ada customer yang berhenti berlangganan')
    
   # garis pembatas
    st.markdown('---')

    # Membuat clustered bar plot untuk korelasi antara churn_risk_score dan feedback
    fig = plt.figure(figsize=(10, 6))
    sns.countplot(x='feedback', hue='churn_risk_score', data=df, palette='viridis')
    plt.legend(title='Customer berhenti berlangganan atau tidak', loc='upper right', labels=['Tidak berhenti', 'Berhenti'])
    plt.title('Korelasi antara churn_risk_score dan feedback')
    plt.xlabel('feedback')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

    st.write('Berdasarkan grafik tersebut, dapat disimpulkan bahwa terdapat keluhan pada website, customer service, banyaknya iklan, kualitas produk, dan lainnya. Sehingga perlu peninjauan kembali terhadap hal-hal tersebut.')
    
    # garis pembatas
    st.markdown('---')


    # Membuat clustered bar plot untuk korelasi antara churn_risk_score dan avg_transaction_value
    # Membuat kelompok (range) untuk 'avg_transaction_value' berdasarkan deskripsi data
    transaction_bins = [0, 20000, 40000, 60000, 100000]
    transaction_labels = ['< 20k', '20k - 40k', '40k - 60k', '> 60k']
    df['transaction_range'] = pd.cut(df['avg_transaction_value'], bins=transaction_bins, labels=transaction_labels)

    # Mengurutkan kategori range 'avg_transaction_value' secara berurutan
    df['transaction_range'] = pd.Categorical(df['transaction_range'], categories=transaction_labels, ordered=True)

    # Membuat bar plot untuk korelasi antara churn_risk_score dan transaction_range
    fig = plt.figure(figsize=(10, 6))
    sns.countplot(x='transaction_range', hue='churn_risk_score', data=df, palette='viridis')
    plt.legend(title='Customer berhenti berlangganan atau tidak', loc='upper right', labels=['Tidak berhenti', 'Berhenti'])
    plt.title('Korelasi antara churn_risk_score dan avg_transaction_value')
    plt.xlabel('Range Avg Transaction Value')
    plt.ylabel('Jumlah')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

    st.write('Berdasarkan grafik tersebut, bahwa mayoritas customer yang berhenti berlangganan berada pada transaction value antara 0k sampai 60k.')

    # garis pembatas
    st.markdown('---')

if __name__ == '__main__':
    run()
