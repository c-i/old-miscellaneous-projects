import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt
import csv
import os

h_team = []
a_team = []
matches = []
matches_old = []
teamlist = []
# season = []

DIR = os.getcwd()

with open(DIR + "history_upto2018.csv", newline="") as historycsv:
    historyreader = csv.reader(historycsv)
    next(historyreader)
        
    for row in historyreader:
        if(row[10] == "2012-13"):
            break
        matches_old.append(row[2:6])

    for row in historyreader:  
        matches.append(row[2:6])
        # season.append(row[10])


matches_T = np.array(matches).T
# print(matches_T)
matches_old_T = np.array(matches_old).T
h_team = matches_T[0]
a_team = matches_T[1]
nsim = 100000


def get_teamlist():
    for team in matches_old_T[0]:
        if not team in teamlist:
            teamlist.append(team)
    for team in matches_T[0]:
        if not team in teamlist:
            teamlist.append(team)

    return teamlist


def get_score(h, a):
    # given the home team and away team of an upcoming match,  
    # return a random variate of the poisson distribution for home and away centered at the mean score (!!!based on last 5 seasons!!!)

    scores = [[],[]]

    for i in range(len(matches)):
        if h_team[i] == h and a_team[i] == a:
            scores[0].append(int(matches[i][2]))
            scores[1].append(int(matches[i][3]))

    print(scores)

    # calculate poisson distribution using medians instead of means?

    
    if len(scores[0]) > 3:
        h_score = np.random.poisson(np.mean(scores[0]), nsim)
        a_score = np.random.poisson(np.mean(scores[1]), nsim)
    else:
        h_sh = []
        h_ca = []
        a_ch = []
        a_sa = []
        for i in range(len(matches)):
            if matches_old_T[0][i] == h or h_team[i] == h:
                h_sh.append(int(matches_T[2][i]))
            if matches_old_T[1][i] == h or a_team[i] == h:
                h_ca.append(int(matches_T[2][i]))
            if matches_old_T[0][i] == a or h_team[i] == a:
                a_ch.append(int(matches_T[3][i]))
            if matches_old_T[1][i] == a or a_team[i] == a:
                a_sa.append(int(matches_T[3][i]))

        h_score = np.random.poisson(.5 * (np.mean(h_sh) + np.mean(h_ca)), nsim)
        a_score = np.random.poisson(.5 * (np.mean(a_ch) + np.mean(a_sa)), nsim)
        print("NOT ENOUGH DATA")
    
    h_score = np.sort(h_score)
    a_score = np.sort(a_score)
     

    return h_score, a_score

def get_pred(h_score, a_score):
    d_prob = 0
    h_prob = 0
    a_prob = 0
    length = len(h_score)


    # tally scores
    h_counts = [0]*(h_score[len(h_score)-1] + 1)
    for i in h_score:
        h_counts[i] += 1
    
    a_counts = [0]*(a_score[len(a_score)-1] + 1)
    for i in a_score:
        a_counts[i] += 1

    # convert tallies into frequencies
    h_freq = []
    for i in h_counts:
        h_freq.append(i/length)

    a_freq = []
    for i in a_counts:
        a_freq.append(i/length)
    print(h_freq)
    print(a_freq)


    hf_len = len(h_freq)
    af_len = len(a_freq)
    # calculate probabilities for home win, away win, draw
    for i in range(1, len(h_freq)):
        for k in range(i):
            h_prob += h_freq[k] * a_freq[k-1]

    for i in range(1, len(a_freq)):
        for k in range(i):
            a_prob += a_freq[k] * h_freq[k-1]
        
    
    if len(h_freq) > len(a_freq):
        for i in range(len(a_freq)):
            d_prob = a_freq[i] * h_freq[i]
    else:
        for i in range(len(h_freq)):
            d_prob = a_freq[i] * h_freq[i]

    h_prob = round(h_prob, 5)
    a_prob = round(a_prob, 5)
    d_prob = round(d_prob, 5)
    return h_prob, a_prob, d_prob

    


score = get_score("Aston Villa", "Sheffield United")
print(score)
print(get_pred(score[0], score[1]))
# print("home mean: ", np.mean(score[0]), "\naway mean: ", np.mean(score[1]), "\n")
# print("home median: ", np.median(score[0]), "\naway median: ", np.median(score[1]), "\n")
# print("home mode: ", str(st.mode(score[0])[0]), "\naway mode: ", str(st.mode(score[1])[0]))

# count, bins, ignored = plt.hist(score, [1,2,3,4,5,6,7,8,9], density=True)
# plt.show()

