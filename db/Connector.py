import mysql.connector

connector = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="alula"
)

cursor = connector.cursor()