# Importing moduels
import streamlit as st
import pandas as pd
import numpy as np

# File uploders
current=st.file_uploader('Upload Current Quater file')
previous=st.file_uploader('Upload Previous Quater file')

# If condition used for when the file uploaded the only it will read and store
if current is not None:
    current_DF=pd.read_excel(current)

# If condition used for when the file uploaded the only it will read and store
if previous is not None:
    previous_DF=pd.read_excel(previous)
    # IF condition for if there is dublicate values and if not
    if True in (previous_DF['previous'].duplicated().tolist()):
        duplicate=(previous_DF[previous_DF['previous'].duplicated()])['previous'].tolist()
        duplicate_particulars = (previous_DF[previous_DF['previous'] == duplicate[0]])['Unnamed: 0'].tolist()
    else:
        duplicate = []
        duplicate_particulars = []


# Function for Auto merge 
def Auto_merge (df1,df2):
    #loading into local variables
    current_DF= df1
    previous_DF = df2
    # creatting empty colum
    previous_DF['current'] = np.nan
    # For loop to iterate
    for i in range (0,len(current_DF)):
        for j in range (0,len(previous_DF)):
            # Stage 1 where it checks the name 
            if current_DF['Unnamed: 0'][i] == previous_DF['Unnamed: 0'][j]:
                print(current_DF['Unnamed: 0'][i])
                print(previous_DF['Unnamed: 0'][j])
                previous_DF.iat[i,len(previous_DF.columns)-1] = current_DF['Recent'][i]
                print('----------------------------')
                break

            # Stage 2.1 if name was not same checks the back value and in back there are dublicate values   
            elif current_DF['Previous'][i] in duplicate:
                st.subheader('Found Dublicated number in previous Quater')
                st.text('For belowe please select right line item ')
                st.write((current_DF['Unnamed: 0'][i]))
                # It will take input from usere if dublicate values found
                user_in=st.selectbox('Select to which you want to Mearg for the above',options=duplicate_particulars,key=i)
                tabel_num=previous_DF['Unnamed: 0'].tolist().index(user_in)
                print(user_in)
                previous_DF.iat[tabel_num,len(previous_DF.columns)-1] = current_DF['Recent'][i]
                
                break
            # Stage 2.2 if name was not same checks the back value           
            elif current_DF['Previous'][i] == previous_DF['previous'][j]:
                print(current_DF['Previous'][i])
                print(previous_DF['previous'][j])
                previous_DF.iat[i,len(previous_DF.columns)-1] = current_DF['Recent'][i]
                print('--------------------------')
                break
    # Show the merged tabel            
    st.table(previous_DF)

# For activate the Function
if previous is not None:
    m_status = st.button('merge',on_click=Auto_merge(current_DF,previous_DF))
