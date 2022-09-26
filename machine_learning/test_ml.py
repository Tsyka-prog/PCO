from unittest import TestCase, main
import pandas as pd

from ml import ML

class TestML(TestCase):
    
# Déclaration des variables communes aux tests
    prediction = ML()
    house = dict ((('bedrooms',1),
        ('bathrooms',1),
        ('sqft_living',200),
        ('sqft_lot',300),
        ('floors',1),
        ('waterfront',0),
        ('view',1),
        ('sqft_above',0),
        ('sqft_basement', 0)))
    X = pd.DataFrame(house, index=[0])
    pred = prediction.model_predict_test(X)
    
    
    def test_if_predict_is_positive_number(self):
        self.assertGreater(self.pred[0], 0)
        
    def test_if_predict_is_float(self):
        self.assertIsInstance(self.pred[0], float)
                     
main()