import pickle
import pandas as pd
import streamlit as st

with open ("prediksi_harga_rumah.pkl", "rb") as f:
    model = pickle.load(f)

def prediksi(LT,LB,JKT,JKM,GRS):
    predict = pd.DataFrame()
    predict['Luas Tanah'] = [Luas Tanah]
    predict['Luas Bangunan'] = [Luas Bangunan]
    predict['Jumlah Kamar Tidur'] = [Jumlah Kamar Tidur]
    predict['Jumlah Kamar Mandi'] = [Jumlah Kamar Mandi]
    predict['Garasi'] = [Garasi]
    return(model.predict(predict)[0])   

lt = st.number_input("Luas Tanah")
lb = st.number_input("Luas Bangunan")
jkt = st.number_input("Jumlah Kamar Tidur")
jkm = st.number_input("Jumlah Kamar Mandi")
opt = st.selectbox(
    'Garasi',
    ('Ada', 'Tidak ada')
)

grs = 0
if(opt == 'Ada') :
    grs = 1
elif (opt == 'Tidak ada'):
    grs = 0
    
    
if(st.button('Predict')) :
    st.write("Harga rumah impianmu adalah Rp{:,}".format(prediksi(lt,lb,jkt,jkm,grs)))
