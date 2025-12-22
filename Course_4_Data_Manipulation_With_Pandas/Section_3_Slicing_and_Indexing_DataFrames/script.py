# OOP Using Python with Pandas

# First import pandas as pd
import pandas as pd

# Create a utilitary class

class DataFrameHandler:
    """
    Class that handles DataFrame operations
    """
    def __init__(self, file):
        self.file = pd.read_csv(file, index_col=0)

    def print_dataframe(self):
        """
        Function incharge of printing the whole dataframe
        """
        # Display all rows and columns
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        print(self.file)

    def print_dataframehead(self):
        """
        Function incharge of printing the whole dataframe headers
        :return:
        """
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', None)
        print(self.file.head())