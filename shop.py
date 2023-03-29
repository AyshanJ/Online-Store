import sqlite3

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()



create_Category_table_query = """
CREATE TABLE Category (
  id INT PRIMARY KEY,
  name TEXT,
  product_id INT   
)
"""
create_Product_table_query = """
CREATE TABLE Product (
  id INT PRIMARY KEY,
  name TEXT,
  price INT   
)
"""
create_Sale_table_query = """
CREATE TABLE Sale (
  id INT PRIMARY KEY,
  client TEXT,
  product_id INT,
  qty INT 
)
"""
cursor.execute(create_Category_table_query)
cursor.execute(create_Product_table_query)
cursor.execute(create_Sale_table_query)
conn.close()
