# open git bash
# start virtual environment command: python -m venv virt
# activate: source virt/Scripts/activate
# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

# to create webpage there is three step process:
    # 1. create template file (html page)
    # 2. create urls
    # 3. create view






# original commands for creating database through code
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Goarmybeatnavy80!!'

)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE eldferco")

print("All Done")