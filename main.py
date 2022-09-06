import streamlit as st;
#import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import services.database as db 
from services.database import *
import pandas as pd 
import Pages.Client.include as PageIncludeClient 
import Pages.Client.read as PageReadClient 
import Pages.Client.exclude as PageExcludeClient 
import Pages.Client.update as PageUpdateClient

#Titulos e menu na direita
#st.title('Include client')
st.sidebar.title('Menu')

Page_client = st.sidebar.selectbox('Client', ['Include', 'Read', 'Update', 'Delete'])

if Page_client == 'Read': 
    PageReadClient.read()

if Page_client == 'Include': 
    PageIncludeClient.include()

if Page_client == 'Delete': 
    PageExcludeClient.exclude()

if Page_client == 'Update': 
    PageUpdateClient.update()



    #incluir = "INSERT INTO crud (name) VALUES (cliente.name)"
    #db.mycursor.execute(incluir)
    #db.mydb.commit()
    #print(db.mycursor.rowcount, "record inserted.")
    #st.write(f'Name: {cliente.name}')
    #st.write(f'Age: {cliente.age}')
    #st.write(f'Occupation: {cliente.occupation}')
    #ClienteController.Incluir(cliente)
   


   
    
    
    


