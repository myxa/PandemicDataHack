from preprocess import Preprocess
from data_utils import download_from_google_disc
pr = Preprocess()
x, y, cat = pr.prepare_trainset('C:\\Users\\Acer\\PycharmProjects\\PandemicDataHack\\data\\train.csv')
print(cat[0])