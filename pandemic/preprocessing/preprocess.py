import pandas as pd




class Preprocess:
    def __init__(self):
        super().__init__()
        self.target = ['salary']
        self.cat_columns = ['position', 'region', 'industry', 'locality',
                            'education_type', 'drive_licences', 'citizenship',
                            'schedule', 'employement_type', 'gender',
                            'relocation_ready', 'travel_ready',
                            'retraining_ready', 'publish_date']

    def opener(self, data_path):
        return pd.read_csv(data_path, sep=';')

    def drop_na_certain_col(self, data, columns):
        """drops rows which have nans according to certain column"""
        return data.dropna(subset=[columns])

    def prepare_trainset(self, data_path, cat_columns=True):
        """ Prepare X, y and cat_features for models
        :param: cat_columns: whether to use categorical features
        """
        train_data = self.opener(data_path)
        X = train_data.drop(self.cat_columns+self.target, axis=1)
        y = train_data[self.target].values
        if cat_columns:
            X = train_data.values
            cat_features = train_data[self.cat_columns].values
            return X, y, cat_features
        return X, y

    # todo обработка drive license

