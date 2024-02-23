def load_stock_data(conn, stock_data):
    cursor = conn.cursor()
    for data_point in stock_data:
        cursor.execute("INSERT INTO stock_data (date, open, high, low, close, adj_close, volume) VALUES (%s, %s, %s, %s, %s, %s, %s)", data_point)
    conn.commit()
    cursor.close()

def fetch_stock_data(conn, stock_symbol):
    cursor = conn.cursor()
    query = f"SELECT * FROM {stock_symbol};"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()

    columns = [desc[0] for desc in cursor.description]
    stock_data = []
    for row in rows:
        stock_data.append(dict(zip(columns, row)))

    return stock_data