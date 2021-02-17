import pandas as pd
import numpy as np
from numpy import ndarray


class Preprocess:
    def __init__(self):
        super().__init__()

    def opener(self, data_path):
        return pd.read_csv(data_path, sep=';')
        #self.test_data = pd.read_csv(test)

    def prepare_trainset(self, data_path, columns_to_use, target, cat_columns=[]):
        """ Prepare X, y and cat_features for models
        :param: columns_to_use: non-categorical features, list
        :param: target: target column, list
        :param: cat_columns: categorical features, list (optional)
        """
        #self.train_data = self.train_data.fillna
        self.train_data = self.opener(data_path)
        if not columns_to_use:
            raise ValueError('Select at least one column to use')
        X = self.train_data[columns_to_use].values
        y = self.train_data[target].values
        if cat_columns:
            cat_features = self.train_data[cat_columns].values
            return X, y, cat_features
        return X, y

