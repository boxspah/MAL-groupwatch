"""
This module contains functions used in the Ui of the GroupWatch app.
"""

from PyQt5 import QtWidgets
from typing import List, Tuple
import csv
import html


def add_options(cbox: QtWidgets.QComboBox) -> None:
    """ Add anime titles as the options in a given combo box """
    with open('data\\anime.csv', encoding='utf8') as anime_csv:
        reader = csv.reader(anime_csv, delimiter=',')
        next(reader)
        for row in reader:
            cbox.addItem(html.unescape(row[1]))


def write_csv(user_data: dict, user_name: str, watch_type: str) -> None:
    """ Write user anime data into a csv file"""
    with open(user_name + '_' + watch_type + '.csv') as user_csv:
        writer = csv.writer(user_csv, delimiter=',')
        for anime in user_data:
            writer.writerow([anime, user_data[anime]])


def read_csv(file_name: str) -> List[Tuple]:
    """Read user anime data from a csv file"""
    lst = []
    with open(file_name) as user_csv:
        reader = csv.reader(user_csv)
        for anime in reader:
            lst.append((anime[0], anime[1]))
    return lst
