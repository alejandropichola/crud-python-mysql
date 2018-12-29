import mysql.connector as MySQLdb

def connect():
  db = MySQLdb.connect(host="localhost", user="root", passwd="", db="api_node")
  return db