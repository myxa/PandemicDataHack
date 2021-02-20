from preprocess import Preprocess
from data_utils import download_from_google_disc
pr = Preprocess()
x, y, cat = pr.prepare_trainset(Path(os.getcwd()).parent)
print(cat[0])