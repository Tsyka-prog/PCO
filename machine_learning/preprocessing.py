from select import select
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

from data import Data

class Preprocessing():
    def __init__(self):
        self.df_house = Data().lecture_df()

    def drop_columns(self):
        self.df_house = self.df_house.drop(['date', 'country', 'street', 'city', 'statezip','yr_built', 'yr_renovated','condition'],
        axis=1)
        return self.df_house

    def delete_zero_price(self):
        delete_zero_line = self.df_house[self.df_house['price'] == 0].index
        self.df_house.drop(delete_zero_line, inplace=True)
        return self.df_house

    def delete_outliers(self):
        drop_line_sqft = self.df_house[self.df_house['sqft_basement'] > 4000].index
        self.df_house.drop(drop_line_sqft , inplace=True)
        drop_line_price = self.df_house[self.df_house['price'] > 1000000].index
        self.df_house.drop(drop_line_price , inplace=True)
        return self.df_house

    def select_x_y(self):
        self.drop_columns()
        self.delete_zero_price()
        self.delete_outliers()
        y = self.df_house["price"]
        X = self.df_house.drop(["price"], axis=1)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        return X_train, X_test, y_train, y_test