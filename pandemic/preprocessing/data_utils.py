import os
from google_drive_downloader import GoogleDriveDownloader as gdd
from pathlib import Path


def download_from_google_disc(file_id=None, filename='train'):
    if filename == 'train' and file_id is None:
        file_id = '1P_C55GbIBTV_ZW_bTjiX26yY4p5EQj3H'
        dest = Path(os.getcwd()).parent / 'data' / 'train.csv'
    elif filename == 'worldskills' and file_id is None:
        file_id = '1JUiJYHf-2nOfgoAaV6KYDKZx7HpgnsyZ'
        dest = Path(os.getcwd()).parent / 'data' / 'worldskills.csv'
    else:
        raise NotImplementedError

    gdd.download_file_from_google_drive(file_id=file_id,
                                        dest_path=dest, showsize=True)

download_from_google_disc()

