def clean_stock_data(stock_data):
    df = pd.DataFrame(stock_data)
    numeric_columns = ['open', 'high', 'low', 'close', 'adj_close', 'volume']
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
    df.dropna(subset=numeric_columns, inplace=True)
    df.interpolate(method='linear', inplace=True)
    cleaned_stock_data = df.to_dict(orient='records')
    return cleaned_stock_data