
def productSales(productList, sales_cnt, survey_grade):
    
    product_dics = {}   #파일에서 읽은 품목별 판매갯수와 평가점수를 담기 위한 dictionary
                        #품목이 key값으로 쓰이고, 판매갯수와 평가점수를 리스트로 만들어 value가 되도록 함
    
    good_products, bad_products = [], []  #우수 상품 리스트와 판매 중지 리스트
    
    for pro in productList:
        dataList = pro.split('/')  #파일의 한 줄씩을 대상으로 /로 분리하여 리스트로 만든다.
        product_dics[dataList[0]] = (int(dataList[1]), int(dataList[2]))
                  #dataList의 첫번째는 품목이고 두번째와 세번째가 각각 판매실적 및 평가 점수이다.
                
    #품목 갯수만큼 반복하면서 판매 기준과 평가 점수의 기준을 비교하여
    #우수 리스트와 판매 중지 리스트에 추가한다.    
    for key in list(product_dics.keys()):

        if product_dics[key][0] >= sales_cnt and product_dics[key][1] >= survey_grade:
            good_products.append(key)

        elif product_dics[key][0] < sales_cnt and product_dics[key][1] < survey_grade:
            bad_products.append(key)

    good_products = sorted(good_products) #sorted()함수를 이용하여 정렬
    bad_products= sorted(bad_products)    #sorted()함수를 이용하여 정렬
    return good_products, bad_products


