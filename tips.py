import pandas as pd
import datetime

def current_date():
    """ 現在の日付を出力する関数

    Args:

    Returns:
        str: 現在の日付を返す(%Y%m%d)で
    """

    dt_now = datetime.datetime.now()
    dt_now_format = dt_now.strftime('%Y%m%d')

    return  dt_now_format

def read_csv(df_name):
    return pd.read_csv(df_name + ".csv")

def to_csv_date(df, filename):
<<<<<<< HEAD
    """
    
=======
    df.to_csv(filename+ '_' + current_date() + '.csv')
>>>>>>> parent of 18db660... 210807 create document by sphinx


