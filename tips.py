import pandas as pd
import datetime

def current_date():
    """ 現在の日付を出力する関数


    Returns:
        str: 現在の日付を返す(%Y%m%d)で
    """

    dt_now = datetime.datetime.now()
    dt_now_format = dt_now.strftime('%Y%m%d')

    return dt_now_format


def read_csv(df_name):
    """
    csv を読み込む関数

    .csv は省略してファイル名だけで読み込むこと可能

    Args:
        df: 読み込むcsvのファイル名

    Returns:
        DataFrame : 読み込んだデータフレーム

    """
    return pd.read_csv(df_name + ".csv")


def to_csv_date(df, filename):
    """
    

    ファイル名に関数実行日(例210807)を加えて保存する

    Args:
        df : 保存するデータフレーム
        filename : ファイル名
    """
    df.to_csv(filename + '_' + current_date() + '.csv')
