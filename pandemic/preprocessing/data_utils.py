import os
from google_drive_downloader import GoogleDriveDownloader as gdd
from pathlib import Path


def download_from_google_disc(file='train', dest=None):
    if file == 'train':
        file_id = '1P_C55GbIBTV_ZW_bTjiX26yY4p5EQj3H'
        if dest is None:
            dest = Path(os.getcwd()).parent / 'data' / 'train.csv'
    elif file == 'worldskills':
        file_id = '1JUiJYHf-2nOfgoAaV6KYDKZx7HpgnsyZ'
        if dest is None:
            dest = Path(os.getcwd()).parent / 'data' / 'worldskills.csv'
    else:
        raise NotImplementedError

    gdd.download_file_from_google_drive(file_id=file_id,
                                        dest_path=dest, showsize=True)

