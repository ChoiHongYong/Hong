def fruitPurchase(dict):

    purchaseDics = {} # 추가 구입해야하는 과일이름을 key로 하고 추가 구입 갯수와
                      # 과일별 구입 소요 비용을 리스트로 만들어 value로 등록 
    total_expenses = 0

    for key in list(dict.keys()):
        
        if dict[key][1] < 5:  #현재 보유하고 있는 각 과일의 갯수가 5미만인지 체크

            partial_expense = (5 - dict[key][1]) * dict[key][0] #추가 구입 비용 계산

            purchaseDics[key] = list(map(int, ((5 - dict[key][1]), partial_expense)))
            
            total_expenses += partial_expense # 총 소요 비용 누적해서 계산

    return purchaseDics, total_expenses
    

