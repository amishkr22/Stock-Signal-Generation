# Stock Signal Generation

## Description
This project generates buy and sell signals for stocks based on moving average crossovers. It fetches stock data from a PostgreSQL database, preprocesses the data, generates trading signals, calculates profit/loss, stores results, and visualizes trading data.

## PostgreSQL Setup
1. **Install PostgreSQL**: Download and install PostgreSQL from the official website [here](https://www.postgresql.org/download/).
2. **Create Database**: Use the following SQL code to create a database named `stock_data`:
   ```sql
   CREATE DATABASE stock_data;

## Table Setup
```sql
CREATE TABLE stock_data (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    open NUMERIC NOT NULL,
    high NUMERIC NOT NULL,
    low NUMERIC NOT NULL,
    close NUMERIC NOT NULL,
    adj_close NUMERIC NOT NULL,
    volume INT NOT NULL
);

CREATE TABLE buy_signals (
    id SERIAL PRIMARY KEY,
    stock_symbol VARCHAR(10) NOT NULL,
    signal_date DATE NOT NULL
);

CREATE TABLE sell_signals (
    id SERIAL PRIMARY KEY,
    stock_symbol VARCHAR(10) NOT NULL,
    signal_date DATE NOT NULL
);

CREATE TABLE profit_loss (
    id SERIAL PRIMARY KEY,
    stock_symbol VARCHAR(10) NOT NULL,
    profit_loss NUMERIC NOT NULL
);

** Make Sure to replace stock_data with your desired table name **
