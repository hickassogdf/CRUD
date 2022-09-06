from turtle import onclick
import streamlit as st;
#import Controllers.ClienteController as ClienteController
import pandas as pd
import services.database as db 
from services.database import *
import models.Cliente as cliente



def read():
    #Seleciona a variável de database.py que seleciona toda a lista do banco de dados e retorna a lista completa
    var = selectall()

    nameList = []
    for item in db.selectall():
       nameList.append([item.name, item.age, item.occupation])

    #utilização da biblioteca PANDAS para criar um Data Frame e depois exibi-lo em forma de tabela (função consultar basicamente na página do server)
    df = pd.DataFrame(
        nameList, 
        columns=['Name', 'Age', 'Occupation']
    )


    st.table(df)

