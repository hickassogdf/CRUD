import streamlit as st;
#import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import services.database as db 
from services.database import *


def include():
    #Incluindo o formulário
    idUpdate = st.experimental_get_query_params()
    st.experimental_get_query_params()
    client_recovery = None; 
    

    if idUpdate.get("id") != None:
        idUpdate = idUpdate.get("id")[0]
        client_recovery = (db.selectById(idUpdate))
        st.experimental_set_query_params(id=[client_recovery.id])
        st.title("Alterar cliente")
    else:
        st.title("Incluir cliente")



    with st.form(key="include_client"):
        listOccupation = ["Developer", "Engineer", "Doctor"]
        if client_recovery == None:
            input_name = st.text_input(label="Name")
            input_age = st.number_input(label="Age", format= "%d", step=1)
            input_occupation = st.selectbox(label="Select your occupation", options= listOccupation)
            #input_button_submit = st.form_submit_button(label="Submit")
        else:
            input_name = st.text_input(label="Name", value= client_recovery.name)
            input_age = st.number_input(label="Age", format= "%d", step=1, value= client_recovery.age)
            input_occupation = st.selectbox(label="Select your occupation", options= listOccupation, index=listOccupation.index(client_recovery.occupation))
        input_button_submit = st.form_submit_button(label="Submit")


    #Quando o botão submit é acionado, o código vai mandar os dados para o banco de dados
    if input_button_submit:
        if client_recovery == None:
            cliente.name = input_name 
            cliente.age = input_age
            cliente.occupation = input_occupation 

            data = (cliente.name, cliente.age, cliente.occupation)

            db.mycursor.execute(db.include, data) 
            db.mydb.commit()

            st.success("Client included succesfully")
        else:
            cliente.name = input_name 
            cliente.age = input_age
            cliente.occupation = input_occupation 
            

            data = (cliente.name, cliente.age, cliente.occupation, client_recovery.id)

            db.mycursor.execute(db.update, data) 
            db.mydb.commit()

            st.success("Client updated succesfully")
            st.experimental_set_query_params()
            

