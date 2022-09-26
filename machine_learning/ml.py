from sklearn.metrics import classification_report, plot_confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler

from data import Data
from preprocessing import Preprocessing
from pipeline_class import PipelineClass

class ML:

    def __init__(self):
        self.df_house = Data().lecture_df()
        self.X_train, self.X_test, self.y_train, self.y_test = Preprocessing().select_x_y()
        self.reg = PipelineClass().creation_pipeline()

    def model_fitting(self):
        fitted_model = self.reg.fit(self.X_train, self.y_train)
        return fitted_model

    def model_predict_test(self, X=None):
        fitted_model = self.model_fitting()
        if X is None:
            y_pred = fitted_model.predict(self.X_test)
        else:

            y_pred = fitted_model.predict(X)

        return y_pred.tolist()
    
    def model_score(self):
        fitted_model = self.model_fitting()
        return fitted_model.score(self.X_test, self.y_test)
