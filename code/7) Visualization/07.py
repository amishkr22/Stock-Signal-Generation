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