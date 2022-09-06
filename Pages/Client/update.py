import streamlit as st;
import services.database as db 
from services.database import *
import Pages.Client.include as PageIncludeClient 

def update():
    paramId = st.experimental_get_query_params()
    if paramId == {}:


        colms = st.columns((1, 2, 1, 2, 1))
        fields = ['id', 'name', 'age', 'occupation', 'update']
        for col, fields_name in zip(colms, fields):
            col.write(fields_name)
        
        for item in db.selectall():
            col1, col2, col3, col4, col5 = st.columns((1, 2, 1, 2, 1))
            col1.write(item.id)
            col2.write(item.name)
            col3.write(item.age)
            col4.write(item.occupation)
            button_space = col5.empty()
            on_click_update = button_space.button('update', 'btn_update'+ str(item.id))
            
            if on_click_update:
                st.experimental_set_query_params(
                    id=[item.id])
                st.experimental_rerun()
    else:
        on_click_back = st.button("Back")
        if on_click_back:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageIncludeClient.include()

                
