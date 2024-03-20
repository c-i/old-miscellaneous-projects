import csv
import numpy as np
import sim
import scipy.stats as st
import os

DIR = os.getcwd()

prompt = input("Test new fixtures? (Y/N)")

while not(prompt == "N" or prompt == "n" or prompt == "Y" or prompt == "y"):
    prompt = input("Test new fixtures? (Y/N)")

if prompt == "N" or prompt == "n":
    raise SystemExit

if prompt == "Y" or prompt == "y":
    
    fixtures = []
    teamlist = sim.get_teamlist()
    
    count = 1
    temp = ""
    while prompt != "exit" or prompt != "Exit" or prompt != "EXIT":
        prompt = input("Enter the HOME team for game no. " + str(count) + " (enter 'exit' to stop): ")
        if prompt == "exit" or prompt == "Exit" or prompt == "EXIT":
            break
        while not prompt in teamlist:
            prompt = input("Team not found, please try again: ")
        temp = prompt
        prompt = input("Enter the AWAY team for game no. " + str(count) + " (enter 'exit' to stop): ")
        while not prompt in teamlist:
            prompt = input("Team not found, please try again: ")
        fixtures.append([temp, prompt])
        count += 1
    print(fixtures)

    results = []
    score = []
    prompt = input("Simulate games? (Y/N)")
    while not(prompt == "N" or prompt == "n" or prompt == "Y" or prompt == "y"):
        prompt = input("Simulate games? (Y/N)")
    if prompt == "N" or prompt == "n":
        raise SystemExit
    if prompt == "Y" or prompt == "y":
        for row in fixtures:
            score = sim.get_score(row[0], row[1])
            pred = sim.get_pred(score[0], score[1])
            results.append([row[0], row[1], np.mean(score[0]), np.mean(score[1]), np.median(score[0]), np.median(score[1]), str(st.mode(score[0])[0]), str(st.mode(score[1])[0])], pred[0], pred[1], pred[2])
            print(results)
    

    prompt = input("Save simulation as .csv? (Y/N)")
    while not(prompt == "N" or prompt == "n" or prompt == "Y" or prompt == "y"):
        prompt = input("Save simulation as .csv? (Y/N)")
    if prompt == "N" or prompt == "n":
        raise SystemExit
    if prompt == "Y" or prompt == "y":
        filepath = ""
        prompt = input(f"Use the default path: {DIR} ? (Y/N)")
        
        while not(prompt == "N" or prompt == "n" or prompt == "Y" or prompt == "y"):
            prompt = input(f"Use the default path: {DIR} ? (Y/N)")
        if prompt == "Y" or prompt == "y":
            filepath = DIR
        if prompt == "N" or prompt == "n":
            filepath = input("Enter a file path (using double backslashes): ")

        filepath += input("Enter a file name: ") + ".csv"
        print(filepath)


        with open(filepath, "w", newline="") as savefilecsv:
            savefilewriter = csv.writer(savefilecsv)
            savefilewriter.writerow(["Home", "Away", "Home Mean", "Away Mean", "Home Median", "Away Median", "Home Mode", "Away Mode", "Home Prob", "Away Prob", "Draw Prob"])
            savefilewriter.writerows(results)
        

            
