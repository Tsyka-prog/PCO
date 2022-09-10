from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.compose import make_column_selector as selector
from sklearn.impute import SimpleImputer

from machine_learning.preprocessing import Preprocessing
from machine_learning.data import Data

class PipelineClass():
    
    def __init__(self):
        pass

    def creation_pipeline(self):
        pass