import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        database="homework20",
        user="postgres",
        password="1234"
    )

    print("Підключення успішне!")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories_Natali (
        id SERIAL PRIMARY KEY,
        category_name VARCHAR(100) NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products_Natali (
        id SERIAL PRIMARY KEY,
        product_name VARCHAR(100) NOT NULL,
        description TEXT,
        price DECIMAL(10,2) NOT NULL,
        category_id INTEGER REFERENCES categories(id)
    );
    """)

    insert_categories_Natali = '''INSERT INTO categories_Natali (category_name)
                                VALUES
                                ('Ноутбуки'),
                                ('Смартфони'),
                                ('Навушники');'''

    insert_products_Natali = '''INSERT INTO products_Natali (product_name, description, price, category_id)
                            VALUES
                            ('Lenovo ThinkPad', 'Ноутбук для роботи', 35000, 1),
                            ('iPhone 15', 'Apple смартфон', 52000, 2),
                            ('Samsung Galaxy S25', 'Android смартфон', 43000, 2),
                            ('Sony WH-1000XM5', 'Бездротові навушники', 16000, 3);'''

    print("Таблиці створено!")

    cursor.execute("SELECT * FROM categories;")
    rows = cursor.fetchall()

    print("Категорії:")
    for row in rows:
        print(row)

    cursor.execute("SELECT * FROM products;")

    rows = cursor.fetchall()

    print("Продукти:")
    for row in rows:
        print(row)

    cursor.execute("""
    SELECT
        products.product_name,
        products.description,
        products.price,
        categories.category_name
    FROM products
    JOIN categories
    ON products.category_id = categories.id;
    """)

    rows = cursor.fetchall()

    print("Список товарів:")
    for row in rows:
        print(row)

    conn.commit()

    cursor.close()
    conn.close()

except Exception as e:
    print("Помилка:")
    print(e)