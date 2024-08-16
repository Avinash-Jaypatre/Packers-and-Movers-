import mysql.connector

class DbManager:
    def getConnection(self):
        connection = mysql.connector.connect(host="localhost",user="root",password="root")
        cursor = connection.cursor()
        return connection,cursor
