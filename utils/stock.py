def get_max_profit(prices):
    min_buy = 0
    max_sell = 0
    max_profit = 0
    min_buys = []

    for _index, _price in enumerate(prices):
        if _index+1 < len(prices) and \
                prices[_index+1] > _price:
            min_buys.append(_price)

    min_buy = min(min_buys)

    max_sell = max(prices[_]
                   for _ in range(prices.index(min_buy), len(prices)))

    if max_sell-min_buy > max_profit:
        return min_buy, max_sell, max_sell-min_buy
    else:
        return min_buy, max_sell, max_profit
