import sqlite3

conn = sqlite3.connect('shop.db')
cursor = conn.cursor()


category_list = []
with open ("data/category.txt",'r') as f:
    for line in f:
        item = line.strip().split(',')
        category_list.append(tuple([int(item[0]), item[1],int(item[2])]))
# print(company_list) # [(1, 'ASUS'), (2, 'ACER'), (3, 'AGB'), (4, 'IBALL'), (5, 'HP')]


cursor.executemany("INSERT INTO Category (id,name,product_id) VALUES(?,?,?);", category_list)
conn.commit()



product_list = []
with open ("data/product.txt",'r') as f:
    for line in f:
        item = line.strip().split(',')
        product_list.append(tuple([int(item[0]), item[1],int(item[2])]))
# print(company_list) # [(1, 'ASUS'), (2, 'ACER'), (3, 'AGB'), (4, 'IBALL'), (5, 'HP')]


cursor.executemany("INSERT INTO Product (id,name,price) VALUES(?,?,?);", product_list)
conn.commit()

sale_list = []
with open ("data/sale.txt",'r') as f:
    for line in f:
        item = line.strip().split(',')
        sale_list.append(tuple([int(item[0]), item[1],int(item[2]),int(item[3])]))
# print(company_list) # [(1, 'ASUS'), (2, 'ACER'), (3, 'AGB'), (4, 'IBALL'), (5, 'HP')]

cursor.executemany("INSERT INTO Sale (id,client,product_id,qty) VALUES(?,?,?,?);", sale_list)
conn.commit()

cursor.close()
conn.close()