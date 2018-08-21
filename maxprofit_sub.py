def max_profit(prices):
    
    max_profit = 0  # 최대 수익은 항상 0 이상의 값
    purchase_day = 0
    sales_day = 0
    
    n = len(prices)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]  # i날에 사서 j날에 팔았을 때 얻을 수 있는 수익
            if profit > max_profit:  # 이 수익이 지금까지 최대 수익보다 크면 값을 고침
                purchase_day = i
                sales_day = j
                max_profit = profit

    
    return purchase_day,sales_day,max_profit

