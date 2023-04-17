import pyodbc

def dbConnect():
    constring = "Driver=MySQL ODBC 8.0 Unicode Driver;SERVER=127.0.0.1;UID=excel_entity;PWD=tokyo2;DATABASE=lojax;PORT=3306"
    conn = pyodbc.connect(constring) #estabelecendo conexão com o DB
    return conn
