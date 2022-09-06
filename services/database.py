import mysql.connector 
import models.Cliente as cliente
import streamlit as st;
import Pages.Client.include as PageIncludeClient 


mydb = mysql.connector.connect(host="localhost", user="hickassogdf", passwd="Rikelme10@", database="firstcrud")

mycursor = mydb.cursor()

include = (
   "INSERT INTO crud(name, age, occupation)"
   "VALUES (%s, %s, %s)"
)


delete = ("DELETE FROM crud WHERE id = %s")
 
update = ("UPDATE crud SET name = %s, age = %s, occupation = %s WHERE id = %s")

select = ("SELECT * from crud WHERE id = %s")







#data = ('Ivanzao', '17', 'Developer')

#mycursor.execute(include, data) 

#mycursor.execute("select * from crud")

#mydb.commit()

def selectall():
   mycursor.execute("select * from crud")
   nameList = [] 
   
   for i in mycursor.fetchall():
      nameList.append(cliente.Cliente(i[0], i[1], i[2], i[3]))

      #print(nameList)
   return nameList

selectall()

def selectById(id):
   mycursor.execute("SELECT * from crud WHERE id = %s", [id])
   costumerList = [] 
   
   for i in mycursor.fetchall():
      costumerList.append(cliente.Cliente(i[0], i[1], i[2], i[3]))

      print(costumerList)
   return costumerList[0]



   
   #for rows in mycursor.fetchall():
   #   costumerList.append(cliente.Cliente(rows[1], rows[2], rows[3]))
   #return costumerList
 


#mycursor.execute("show tables")

#for rows in mycursor:
#  lista = print(rows)
  