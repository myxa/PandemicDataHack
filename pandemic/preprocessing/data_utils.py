import os
from google_drive_downloader import GoogleDriveDownloader as gdd
from pathlib import Path


def download_from_google_disc(file_id=None, filename='train', dest=None):
    # dictionary for datasets name and ids
    id_dict = {'train.csv': '1P_C55GbIBTV_ZW_bTjiX26yY4p5EQj3H',
               'worldskills.csv': '1JUiJYHf-2nOfgoAaV6KYDKZx7HpgnsyZ'}

    for key in id_dict:
        filename, file_id = key, id_dict[key]
        dest = Path(os.getcwd()).parent / 'data' / key
        gdd.download_file_from_google_drive(file_id=file_id,
                                            dest_path=dest, showsize=True)


download_from_google_disc()
