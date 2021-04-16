"""
This module contains functions used in the Ui of the GroupWatch app.
"""

from PyQt5 import QtWidgets
import csv
import GroupWatchGroup
import GroupWatchSolo
import sys


def add_options(cbox: QtWidgets.QComboBox) -> None:
    """ Add anime titles as the options in a given combo box """
    with open('data\\anime.csv', encoding='utf8') as anime_csv:
        reader = csv.reader(anime_csv, delimiter=',')
        next(reader)
        for row in reader:
            cbox.addItem(row[1])


def write_csv(user_data: dict, user_name: str, watch_type: str) -> None:
    """ Write user anime data into a csv file"""
    with open(user_name + '_' + watch_type + '.csv') as user_csv:
        writer = csv.writer(user_csv, delimiter=',')
        for anime in user_data:
            writer.writerow([anime, user_data[anime]])
