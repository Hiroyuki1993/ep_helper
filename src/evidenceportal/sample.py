import numpy as np
import pandas as pd
import datetime

class API:
    url = ""
    def __init__(self, url):
        self.url = url

    def hello(self):
        print("hello_world, {}".format(self.url))

    def get_array(self):
        return np.array([1, 2, 3])


    def get_df(self):
        return pd.Series([1, 2, 3])


    def get_date(self):
        print(datetime.datetime(2019, 12, 1, 1, 1, 1))