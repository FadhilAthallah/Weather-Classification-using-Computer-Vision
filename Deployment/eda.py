# eda.py

import streamlit as st

def run_eda():
    st.title("Exploratory Data Analysis (EDA)")
    # Add your EDA code here

    st.title("**Data Distribution**")
    st.image("pie.png", caption="Distribution of weather", use_column_width=True)
    st.write('**Penjelasan:**')
    st.write("""* Persebaran data memiliki distribusi yang merata untuk gambar cloudy, rainy dan foggy dengan jumlah 20% dari total kesuluruhan data 
* sunrise memiliki jumlah 23.3% dan shine memiliki jumlah 16.7% dari keseluruhan data total
* Berdasarkan dari seluruh persebarannyannya, data yang akan digunakan ini memiliki perseberaran yang sudah cukup baik dengan perbedaan jumlah yang tidak terlalu jauh
""")
    
    st.title('**Foggy**')
    st.image("foggy.png", caption="Foggy Screenshot", use_column_width=True)

    st.title('**rainy**')
    st.image("rainy.png", caption="rainy Screenshot", use_column_width=True)

    st.title('**sunny**')
    st.image("sunny.png", caption="sunny Screenshot", use_column_width=True)

    st.title('**sunrise**')
    st.image("sunrise.png", caption="sunrise Screenshot", use_column_width=True)

    st.title('**cloudy**')
    st.image("cloudy.png", caption="cloudy Screenshot", use_column_width=True)    

    st.write('* berdasarkan pengecekan, kelima kelas sudah berhasil memasukkan gambar yang sesuai ')        