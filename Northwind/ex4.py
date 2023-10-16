import requests
import sqlite3
import random

# Função para obter dados aleatórios da API
def get_random_user_data():
    response = requests.get('https://randomuser.me/api/')
    data = response.json()
    user = data['results'][0]
    return {
        'name': f"{user['name']['first']} {user['name']['last']}",
        'email': user['email'],
    }

# Conectar-se ao banco de dados
conn = sqlite3.connect('meu_db.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY,
    Name TEXT,
    Email TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Suppliers (
    SupplierID INTEGER PRIMARY KEY,
    Name TEXT,
    Email TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY,
    ProductName TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    SupplierID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
''')

# Preencher tabelas com dados aleatórios
for _ in range(10):
    customer_data = get_random_user_data()
    cursor.execute('INSERT INTO Customers (Name, Email) VALUES (?, ?)', (customer_data['name'], customer_data['email']))
    
for _ in range(5):
    supplier_data = get_random_user_data()
    cursor.execute('INSERT INTO Suppliers (Name, Email) VALUES (?, ?)', (supplier_data['name'], supplier_data['email']))
    
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
for product_name in products:
    cursor.execute('INSERT INTO Products (ProductName) VALUES (?)', (product_name,))

# Simular pedidos aleatórios
for _ in range(20):
    customer_id = random.randint(1, 10)
    supplier_id = random.randint(1, 5)
    product_id = random.randint(1, 5)
    quantity = random.randint(1, 10)
    cursor.execute('INSERT INTO Orders (CustomerID, SupplierID, ProductID, Quantity) VALUES (?, ?, ?, ?)',
                   (customer_id, supplier_id, product_id, quantity))

# Commit e fechar a conexão com o banco de dados
conn.commit()
conn.close()
