import streamlit as st
import pandas as pd
import numpy as np

current=st.file_uploader('Upload Current Quater file')
previous=st.file_uploader('Upload Previous Quater file')


current_DF=pd.read_excel(current)
previous_DF=pd.read_excel(previous)



if True in (previous_DF['previous'].duplicated().tolist()):
    duplicate=(previous_DF[previous_DF['previous'].duplicated()])['previous'].tolist()
    duplicate_particulars = (previous_DF[previous_DF['previous'] == duplicate[0]])['Unnamed: 0'].tolist()
else:
    duplicate = []
    duplicate_particulars = []



def Auto_mearg (df1,df2):
    
    current_DF= df1
    previous_DF = df2
    previous_DF['current'] = np.nan
    for i in range (0,len(current_DF)):
        for j in range (0,len(previous_DF)):
            if current_DF['Unnamed: 0'][i] == previous_DF['Unnamed: 0'][j]:
                print(current_DF['Unnamed: 0'][i])
                print(previous_DF['Unnamed: 0'][j])
                previous_DF.iat[i,len(previous_DF.columns)-1] = current_DF['Recent'][i]
                print('----------------------------')
                break
                
            elif current_DF['Previous'][i] in duplicate:
                st.subheader('Found Dublicated number in previous Quater')
                st.text('For belowe please select right line item ')
                st.write((current_DF['Unnamed: 0'][i]))
                user_in=st.selectbox('Select to which you want to Mearg for the above',options=duplicate_particulars,key=i)
                #user_in = int(input())
                tabel_num=previous_DF['Unnamed: 0'].tolist().index(user_in)
                print(user_in)
                previous_DF.iat[tabel_num,len(previous_DF.columns)-1] = current_DF['Recent'][i]
                
                break
                        
            elif current_DF['Previous'][i] == previous_DF['previous'][j]:
                print(current_DF['Previous'][i])
                print(previous_DF['previous'][j])
                previous_DF.iat[i,len(previous_DF.columns)-1] = current_DF['Recent'][i]
                print('--------------------------')
                break

    st.table(previous_DF)



m_status = st.button('merge')
if m_status:
    Auto_mearg(current_DF,previous_DF)

#if previous_DF == True:
   # Auto_mearg(current_DF,previous_DF)
