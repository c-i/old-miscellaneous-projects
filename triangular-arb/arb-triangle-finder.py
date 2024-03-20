import pickle
import ccxt
import os

DIR = os.getcwd()


def get_arb_list(exchange, market_filter='', save_list=False):
    markets = exchange.load_markets()
    symbols = exchange.symbols

    print(symbols)

    arb_list = []
    i = 0
    while i < len(symbols):
        num = symbols[i][0:symbols[i].find('/')]
        denlist = [symbols[i][symbols[i].find('/')+1:]]
        layer2_all = [symbols[i]]
        e = i + 1
        skip_count = 1
        while e < len(symbols) and symbols[e][0:symbols[e].find('/')] == num:
            denlist += [symbols[e][symbols[e].find('/')+1:]]
            layer2_all += [symbols[e]]
            e += 1
            skip_count += 1
        # print(num, denlist)
        # print(layer2_all)

        layer3_all = []
        for den in denlist:
            j = denlist.index(den) + 1
            while j < len(denlist):
                layer3_all += [den + '/' + denlist[j]]
                layer3_all += [denlist[j] + '/' + den]
                j += 1
            
        layer3_ref = list(layer3_all)
        for pair in layer3_all:
            if pair not in symbols:
                layer3_ref.remove(pair)
            

        # print(layer3_all)


        for den in denlist:
            base = num + '/' + den
            layer2 = list(layer2_all)
            layer2.remove(base)
            layer3 = []

            for pair in layer3_ref:
                if den in pair:
                    layer3 += [pair]

            for pair in layer2:
                for p in layer3:
                    if den + '/' + pair[pair.find('/')+1:] == p:
                        arb_list += [[[base, False], [pair, True], [p, False]]]
                    if pair[pair.find('/')+1:] + '/' + den == p:
                        arb_list += [[[base, False], [pair, True], [p, True]]]

        i += skip_count
    
    arb_list_ref = list(arb_list)
    if market_filter != '':
        for triangle in arb_list:
            if market_filter not in triangle[0][0]:
                arb_list_ref.remove(triangle)


    if save_list:
        arb_list_path = DIR + exchange.id + '_arb_list_' + market_filter
    
        with open(arb_list_path, 'wb') as fp:
            pickle.dump(arb_list_ref, fp)

    return arb_list_ref
    
arb_list = get_arb_list(ccxt.kucoin(), 'USDT', True)

for e in arb_list:
    print(e)


