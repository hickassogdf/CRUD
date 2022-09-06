import streamlit as st;
import services.database as db 
from services.database import *

def exclude():
    colms = st.columns((1, 2, 1, 2, 1))
    fields = ['id', 'name', 'age', 'occupation', 'exclude']
    for col, fields_name in zip(colms, fields):
        col.write(fields_name)
    
    for item in db.selectall():
        col1, col2, col3, col4, col5 = st.columns((1, 2, 1, 2, 1))
        col1.write(item.id)
        col2.write(item.name)
        col3.write(item.age)
        col4.write(item.occupation)
        button_space = col5.empty()
        on_click_exclude = button_space.button('exclude', 'btn_excluir'+ str(item.id))

        if on_click_exclude:
            db.mycursor.execute(db.delete, [item.id]) 
            db.mydb.commit()
            button_space.button = st.success("Client deleted succesfully")
           

            
        

             
        


