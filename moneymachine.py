import pickle
import csv
import time
import numpy as np
import ccxt
import os

DIR = os.getcwd()

exchange = ccxt.kucoin({
    'enableRateLimit': True,
})
markets = exchange.load_markets()
symbols = exchange.symbols

market_filter = 'USDT'

arb_list_path = DIR + exchange.id + '_arb_list_' + market_filter
arb_list = []

for e in arb_list:
    print(e)

with open(arb_list_path, 'rb') as fp:
    arb_list = pickle.load(fp)

arb_array = np.array(arb_list)
arb_list_T = np.ndarray.tolist(arb_array.T)


seconds = 3600
orderbook_test_list = []
test_list_path = DIR + exchange.id + '_test_list_' + market_filter + '.csv'

start_time = time.time()

while True:

    bid_list1 = exchange.fetch_tickers(arb_list_T[0][0])
    ask_list = exchange.fetch_tickers(arb_list_T[0][1])
    bid_list2 = exchange.fetch_tickers(arb_list_T[0][2])

    i = 0
    while i < len(arb_list_T[0][0]):
        expected_profit = bid_list1[arb_list_T[0][0][i]]['bid'] * (1/ask_list[arb_list_T[0][1][i]]['ask']) * (1/bid_list2[arb_list_T[0][2][i]]['bid'] if arb_list_T[1][2][i] else bid_list2[arb_list_T[0][2][i]]['bid'])
        i += 1

        if expected_profit > 1.003:
            t = time.localtime()
            orderbook_test_list += [[time.strftime("%H:%M:%S", t)] + [arb_array[i]] + [expected_profit]]
            print(time.strftime("%H:%M:%S", t), ', ', arb_array[i], ', ', expected_profit)


    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > seconds:
        break

with open(test_list_path, 'w', newline='') as test_list_csv:
    test_list_writer = csv.writer(test_list_csv)
    test_list_writer.writerows(orderbook_test_list)

    



# orderbook_test_list = []
# start_time = time.time()

# for arb_triangle in arb_list:
#     bidsasks = exchange.fetch_tickers([arb_triangle[0][0], arb_triangle[1][0], arb_triangle[2][0]])

#     bid1 = bidsasks[arb_triangle[0][0]]['bid']
#     ask2 = bidsasks[arb_triangle[1][0]]['ask']
#     bid3 = bidsasks[arb_triangle[2][0]]['bid']

#     expected_profit = bid1 * (1/ask2) * (1/bid3 if arb_triangle[2][1] else bid3)

    # if expected_profit > 1.0:
    #     t = time.localtime()
    #     orderbook_test_list += [time.strftime("%H:%M:%S", t)] + [arb_triangle] + [expected_profit]
    #     print(time.strftime("%H:%M:%S", t), ', ', arb_triangle, ', ', expected_profit)


# end_time = time.time()

# print('runtime: ', (end_time - start_time))



