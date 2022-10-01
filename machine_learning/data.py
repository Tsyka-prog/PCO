import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Data:

    def lecture_df(self):
        self.df_house = pd.read_csv("machine_learning\data.csv")
        return self.df_house