def store_results(conn, stock_symbol, buy_signals, sell_signals, profit_loss):
    cursor = conn.cursor()
    for signal in buy_signals:
        cursor.execute("INSERT INTO buy_signals (stock_symbol, signal_date) VALUES (%s, %s)", (stock_symbol, signal))
    for signal in sell_signals:
        cursor.execute("INSERT INTO sell_signals (stock_symbol, signal_date) VALUES (%s, %s)", (stock_symbol, signal))
    cursor.execute("INSERT INTO profit_loss (stock_symbol, profit_loss) VALUES (%s, %s)", (stock_symbol, profit_loss))
    conn.commit()
    cursor.close()