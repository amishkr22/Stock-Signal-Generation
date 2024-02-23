def calculate_profit_loss(stock_data, buy_signals, sell_signals):
    profit_loss = 0
    position = None
    buy_price = None

    for row in stock_data:
        date = row['date']

        if date in buy_signals:
            if position == 'SELL':
                profit_loss += (row['close'] - buy_price)
                position = None

            if position != 'BUY':
                position = 'BUY'
                buy_price = row['close']

        elif date in sell_signals:
            if position == 'BUY':
                profit_loss += (row['close'] - buy_price)
                position = None

            if position != 'SELL':
                position = 'SELL'
                buy_price = row['close']

    return profit_loss