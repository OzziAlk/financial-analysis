import pandas as pd


def filter_csv(in_path, out_path, filter_id, filter_col):
    df = pd.read_csv(in_path)
    df = df[df[filter_col] == filter_id]
    df.to_csv(out_path)


in_path = "../data/raw_stock_data.csv"
out_path = "../data/semicon_stock_data.csv"
semiconductor_sic = 3674
sic_col = "HSICCD"

filter_csv(in_path, out_path, semiconductor_sic, sic_col)