import pickle
import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import load_model

# Load model
model_sequential2 = load_model('model_sequential2_Churn.h5')


#load preprocessor
with open('prepocessor.pkl', 'rb') as file_1: 
  preprocessor = pickle.load(file_1)

def run():
    with st.form('key=default_predict'):

        region_category_options = ['City', 'Village', 'Town']
        region_category = st.selectbox('Region Category', region_category_options, help='')

        membership_category_options = ['No Membership', 'Basic Membership', 'Silver Membership', 'Premium Membership', 'Gold Membership', 'Platinum Membership']
        membership_category = st.selectbox('Membership Category', membership_category_options, help='')

        joined_through_referral_options = ['Yes', 'No']
        joined_through_referral = st.selectbox('Joined Through Referral', joined_through_referral_options, help='')

        preferred_offer_types_options = ['Without Offers', 'Credit/Debit Card Offers', 'Gift Vouchers/Coupons']
        preferred_offer_types = st.selectbox('Preferred Offer Types', preferred_offer_types_options, help='')

        medium_of_operation_options = ['Desktop', 'Smartphone', 'Both']
        medium_of_operation = st.selectbox('Medium of Operation', medium_of_operation_options, help='')

        avg_transaction_value = st.number_input('Average Transaction Value', min_value=800.46, max_value=99914.05, value=800.46, step=0.01, format="%.2f", help='')

        avg_frequency_login_days = st.number_input('Average Frequency Login Days', min_value=0.0, max_value=73.06199459430009, value=0.0, step=0.01, format="%.2f", help='')

        points_in_wallet = st.number_input('Points in Wallet', min_value=0.0, max_value=2069.069760814851, value=0.0, step=0.01, format="%.2f", help='')


        offer_application_preference_options = ['Yes', 'No']
        offer_application_preference = st.selectbox('Offer Application Preference', offer_application_preference_options, help='')

        feedback_options = ['Poor Website', 'Poor Customer Service', 'Too many ads', 'Poor Product Quality', 'No reason specified', 'Products always in Stock', 'Reasonable Price', 'Quality Customer Care', 'User Friendly Website']
        feedback = st.selectbox('Feedback', feedback_options, help='')



        st.markdown('---')

        if st.form_submit_button('Predict'):

            # Create the new_data dictionary
            new_data = [{'region_category': region_category,
                'membership_category': membership_category,
                'joined_through_referral': joined_through_referral,
                'preferred_offer_types': preferred_offer_types,
                'medium_of_operation': medium_of_operation, 
                'avg_transaction_value': avg_transaction_value,
                'avg_frequency_login_days': avg_frequency_login_days, 
                'points_in_wallet': points_in_wallet, 
                'offer_application_preference': offer_application_preference, 
                'feedback': feedback
            }]

            new_data = pd.DataFrame(new_data)

            final_data_inf = preprocessor.transform(new_data)
            st.dataframe(final_data_inf)



            pred = model_sequential2.predict(final_data_inf)

            # Menampilkan hasil prediksi
            st.subheader('Hasil Prediksi')
            if pred[0][0] > 0.5:
                st.write("Kemungkinan Berhenti Berlangganan")
            else:
                st.write("Tidak Berhenti Berlangganan")

if __name__ == '__main__':
    run()