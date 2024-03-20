import csv
import os

DIR = os.getcwd()

history_path = DIR + "history.csv"
addition_path = DIR + "season-1819.csv"
season = "2018-19"

with open(history_path, "a", newline="") as historycsv, open(addition_path, newline="") as additioncsv:
    historywriter = csv.writer(historycsv)
    # historyreader = csv.reader(historycsv)
    additionreader = csv.reader(additioncsv)

    # for row in historyreader:
    #     print(row[10])
    #     if row[10] != season:
    #         historywriter.writerow(row)

    for row in additionreader:
        row_fixed = row[0:10]
        row_fixed.append(season)
        historywriter.writerow(row_fixed)
