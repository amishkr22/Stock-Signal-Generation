import psycopg2
from datetime import datetime
import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import numpy as np

def connect_to_database():
    conn = psycopg2.connect(
        dbname="DATABASE_NAME",
        user="USER_NAME",
        password="ENTER_PASSWORD",
        host="HOST_NAME",
        port="PORT"
    )
    return conn
