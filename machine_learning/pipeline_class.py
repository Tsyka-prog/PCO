from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_selector as selector
from sklearn.linear_model import LinearRegression

from preprocessing import Preprocessing
from data import Data

class PipelineClass():
    
    def __init__(self):
        pass

    def creation_pipeline(self):
        numeric_transformer = Pipeline(steps=[('scaler', MinMaxScaler())])

        preprocessor = ColumnTransformer(transformers=[
            ('numeric_transformer', numeric_transformer, selector(dtype_include=["float"]))
        ],remainder='passthrough')

        reg = Pipeline(steps=[
            ('preprocessor', preprocessor), 
            ('regressor', LinearRegression())])
        return reg