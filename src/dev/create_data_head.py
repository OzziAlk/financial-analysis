import pandas as pd


def make_head_from_full_csv(in_path, n=5000, out_path ="", other_manipulations=None):

    # if no out path specified, set it to match the input path with the suffix "_HEAD"
    if out_path == "" or not isinstance(out_path, str):
        out_path = in_path[:-4] + "_HEAD.csv"

    # read full data,
    df_full = pd.read_csv(in_path)

    # if we have passed a valid function to perform other data manipulations, attempt to execute it with df_full
    if other_manipulations is not None and callable(other_manipulations):
        try:
            other_manipulations(df_full)
        except RuntimeError:
            pass

    # store just the head of our full dataframe, using specified head-count n
    df_head = df_full.head(n=n)

    # write head dataframe to csv at out_path
    df_head.to_csv(out_path)


def main():
    in_path = "../data/raw_stock_data.csv"
    make_head_from_full_csv(in_path)

main()