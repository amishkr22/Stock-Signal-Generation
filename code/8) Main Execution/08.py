def main():
    conn = connect_to_database()
    stock_symbol = "tsla"
    stock_data = fetch_stock_data(conn, stock_symbol)
    
    if not stock_data:
        stock_data_to_load = [(datetime(2023, 1, 1), 100, 110, 90, 105, 105, 10000)]
        load_stock_data(conn, stock_data_to_load)
        stock_data = fetch_stock_data(conn, stock_symbol)

    clean_stock_data(stock_data)
    buy_signals, sell_signals = generate_signals(stock_data)
    profit_loss = calculate_profit_loss(stock_data, buy_signals, sell_signals)
    store_results(conn, stock_symbol, buy_signals, sell_signals, profit_loss)
    visualize_trading(stock_data, buy_signals, sell_signals)

    conn.close()

if __name__ == "__main__":
    main()