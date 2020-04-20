from dev.dev_lib import IntegrateData


class CleanRawData(IntegrateData):

    def __init__(self, in_path, out_path=""):
        super().__init__(in_path, output_path=out_path)

    def integrate_data(self):

        # adjust for erroneous negative entries into price column
        self.data['PRC'] = self.data['PRC'].apply(lambda x: abs(x))

        # call to parent method to mark self.data as ready for writing
        super().integrate_data()


def main():
    path_in = "../data/raw_stock_data_HEAD.csv"

    clean = CleanRawData(path_in)
    clean.process()


main()
