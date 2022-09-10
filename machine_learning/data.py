import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Data:

    def lecture_df(self):
        self.df_house = pd.read_csv('./data.csv')
        return self.df_house

    def viz_info(self):
        self.lecture_df()
        self.df_house.info()
        return self.df_house.describe()

    def regression_viz(self):
        self.lecture_df()
        for i, col in enumerate(self.df_house.columns):
            plt.figure(i)
            sns.regplot(x=self.df_house.columns[i], y="price", data=self.df_house)

    def viz_barplot(self):
        self.lecture_df()
        return sns.barplot(data=self.df_house, x='sqft_lot', y='price')

    def viz_displot(self):
        self.lecture_df()
        return sns.distplot(self.df_house['price'])