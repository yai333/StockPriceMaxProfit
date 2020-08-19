from utils.stock import get_max_profit

if __name__ == "__main__":
    # change stock_prices_yesterday value
    stock_prices_yesterday = [10, 7, 5, 8, 11, 4,
                              20, 10, 1, 20, 15]
    min_buy, max_sell, max_profit = get_max_profit(stock_prices_yesterday)
    print("="*40)
    print(
        f"${max_profit} ( buying for ${min_buy} and selling for ${max_sell} )")
    print("="*40)
