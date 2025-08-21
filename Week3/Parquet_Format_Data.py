import numpy as np
import pandas as pd

class Parquet_Format_Data():
    def __init__(self, csv_file, parquet_file):
        self.csv_file = csv_file
        self.parquet_file = parquet_file
        self.csv_data = None

    def read_file(self):
        self.csv_data = pd.read_csv(self.csv_file)
        print(f"{self.csv_file} file data is displayed below\n")
        print(self.csv_data)

    def convert_to_parquet(self):
        self.csv_data.to_parquet(self.parquet_file, engine="pyarrow", index=False)
        print(f"\n\nParquet file '{self.parquet_file}' created successfully.\n")
        print(self.csv_data)

    def calculations(self):
        #Get numeric columns
        self.numeric_columns = self.csv_data.select_dtypes(include=[np.number]).columns
        print(f"\n\nNumeric columns: {list(self.numeric_columns)}")

        for num_col in self.numeric_columns:
            num_data_set = self.csv_data[num_col]
            print(f"\nColumn: {num_col}")
            print(f"\tMaximum : {num_data_set.max()}")
            print(f"\tMinimum : {num_data_set.min()}")
            print(f"\tAverage : {num_data_set.mean():.3f}")
            print(f"\tFirst 10 absolute values : {num_data_set.abs().head(10).tolist()}")


def main():
    csv_file = "forestfires.csv"
    parquet_file = "sample.parquet"
    data = Parquet_Format_Data(csv_file, parquet_file)

    data.read_file()
    data.convert_to_parquet()
    data.calculations()


if __name__ == "__main__":
    main()
