import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import numpy as np

def connect_to_database():
    conn = psycopg2.connect(
        dbname="Stock",
        user="postgres",
        password="Amish@2209",
        host="localhost",
        port="5432"
    )
    return conn

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

def clean_stock_data(stock_data):
    df = pd.DataFrame(stock_data)
    numeric_columns = ['open', 'high', 'low', 'close', 'adj_close', 'volume']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    df.dropna(subset=numeric_columns, inplace=True)
    df.interpolate(method='linear', inplace=True)
    cleaned_stock_data = df.to_dict(orient='records')
    return cleaned_stock_data

def moving_average(data, window):
    return np.convolve(data, np.ones(window) / window, mode='valid')

def generate_signals(stock_data):
    close_prices = [float(data['close']) for data in stock_data]

    sma_5 = moving_average(close_prices, 5)
    sma_10 = moving_average(close_prices, 10)
    sma_20 = moving_average(close_prices, 20)
    sma_50 = moving_average(close_prices, 50)
    sma_200 = moving_average(close_prices, 200)
    sma_500 = moving_average(close_prices, 500)

    buy_signals = []
    sell_signals = []

    min_length = min(len(sma_5), len(sma_10), len(sma_20), len(sma_50), len(sma_200), len(sma_500))

    for i in range(min_length - 1):
        if sma_50[i] > sma_500[i] and sma_50[i + 1] <= sma_500[i + 1]:
            buy_signals.append(stock_data[i + 1]['date'])

    for i in range(min_length - 1):
        if sma_20[i] < sma_200[i] and sma_20[i + 1] >= sma_200[i + 1]:
            sell_signals.append(stock_data[i + 1]['date'])

    for i in range(min_length - 1):
        if sma_10[i] < sma_20[i] and sma_10[i + 1] >= sma_20[i + 1]:
            sell_signals.append(stock_data[i + 1]['date'])

    for i in range(min_length - 1):
        if sma_5[i] < sma_10[i] and sma_5[i + 1] >= sma_10[i + 1]:
            buy_signals.append(stock_data[i + 1]['date'])

    return buy_signals, sell_signals

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

def store_results(conn, stock_symbol, buy_signals, sell_signals, profit_loss):
    cursor = conn.cursor()
    for signal in buy_signals:
        cursor.execute("INSERT INTO buy_signals (stock_symbol, signal_date) VALUES (%s, %s)", (stock_symbol, signal))
    for signal in sell_signals:
        cursor.execute("INSERT INTO sell_signals (stock_symbol, signal_date) VALUES (%s, %s)", (stock_symbol, signal))
    cursor.execute("INSERT INTO profit_loss (stock_symbol, profit_loss) VALUES (%s, %s)", (stock_symbol, profit_loss))
    conn.commit()
    cursor.close()

def visualize_trading(stock_data, buy_signals, sell_signals):
    df = pd.DataFrame(stock_data)
    df['date'] = pd.to_datetime(df['date'])  
    df.set_index('date', inplace=True)

    numeric_columns = ['open', 'high', 'low', 'close', 'adj_close', 'volume']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    mpf.plot(df, type='candle', style='charles', volume=True, title='Stock Data', tight_layout=True)

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['close'], label='Close Price', color='black', linewidth=0.5)
    plt.scatter(buy_signals, df.loc[buy_signals, 'close'], color='green', label='Buy Signal', s=20)
    plt.scatter(sell_signals, df.loc[sell_signals, 'close'], color='red', label='Sell Signal', s=20)
    plt.title('Trading Signals')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.show()

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



