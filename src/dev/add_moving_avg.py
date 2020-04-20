from dev.dev_lib import IntegrateData


class AddMovingAverage(IntegrateData):

    def __init__(self, in_path, out_path="", periods=(), value_col="PRC", id_col="TICKER", date_col="date"):
        super().__init__(in_path, output_path=out_path)
        self.periods = periods
        self.value = value_col
        self.id = id_col
        self.date = date_col

    def integrate_data(self):

        # retain only necessary data and declare a new column that maps the index to facilitate df.apply()
        self.data = self.data[[self.date, self.id, self.value]]
        self.data["temp-idx"] = self.data.index

        # for each period p over which we want a moving average
        for p in self.periods:

            # decare new column name
            new_col = self.value + " moving average " + str(p)

            # perform moving average calculation
            self.data[new_col] = self.data[self.value].rolling(p).mean()

            # change NaN to dummy value of -1
            self.data[new_col] = self.data[new_col].apply(lambda x: x if x > 0 else -1)

            # adjust rows whose moving average contains values from different ids to dummy value of -1
            self.data[new_col] = self.data["temp-idx"].apply(
                lambda x: self.data.at[x, new_col]
                if self.data.at[x, self.id] == self.data.at[max(x - p, 0), self.id] else -1)

        # drop the now redundant index duplicate
        self.data.drop(columns=["temp-idx"], axis=1, inplace=True)

        # call to parent method to mark self.data as ready for writing
        super().integrate_data()


path_in = "../data/raw_stock_data_HEAD.csv"
path_out = "../data/MA_stock_data_HEAD.csv"

addMA = AddMovingAverage(path_in, out_path=path_out, periods=[20])
addMA.process()
