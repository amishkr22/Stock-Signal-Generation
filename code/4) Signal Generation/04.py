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