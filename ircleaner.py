import datetime as dt
import os
import shutil
import sys


DATETIME_FORMAT = '%d-%m-%Y %H-%M'

FILE_TYPES = [
    '.txt',
    '.doc',
    '.jpg',
    '.jpeg',
    '.png',
    '.pptx',
    '.xlsx',
    '.docx'
    ]


def clean():
    if sys.platform.startswith('win32'):
        desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        os.chdir(desktop_path)
        name_dir_to_collected = dt.datetime.now().strftime(DATETIME_FORMAT)
        os.mkdir(name_dir_to_collected)
        files_to_collect = list()
        for file in os.listdir():
            for file_type in FILE_TYPES:
                if file.endswith(file_type):
                    files_to_collect.append(file)
        for file in files_to_collect:
            shutil.move(file, name_dir_to_collected)


if __name__ == '__main__':
    clean()
