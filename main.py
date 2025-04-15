import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Название 
# Описание
st.title('Заполни пропуски')
st.write('Загрузи свой датафрейм и заполни пропуски')

#  шаг 1 загрузка csv

uploader_file = st.sidebar.file_uploader('Загрузи csv файл', type = 'csv')

if uploader_file is not None:
    df = pd.read_csv(uploader_file)
    st.write(df.head(5))
else:
    st.stop()
    
#  шаг 2 проверка наличия пропуска

missed_valies = df.isna().sum()
missed_valies = missed_valies[missed_valies > 0]
if len(missed_valies) > 0:
    fig, ax = plt.subplots()
    sns.barplot(x = missed_valies. index, y = missed_valies.values)
    ax.set_title("Пропуски в столбиках")
    st.pyplot(fig)
#  шаг 3 заполнить пропуски

    button = st.button('Заполнить пропуски')
    if button:
        df_filled = df[missed_valies.index].copy()

        for col in df_filled:
            if df_filled[col].dtype == 'object':
                df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])
            else:
                df_filled[col] = df_filled[col].fillna(df_filled[col].median())

        st.write(df_filled.head(5))

     
#  шаг 4 выгрузить заполненный csv 

        dawnload_button = st.dawnload_button(label = 'Скачать CSV файл',
                        data = df_filled.to_csv(),
                        file_name = 'filled_fate.csv')

else:
    st.write('Нет пропусков в данных')    
    st.stop