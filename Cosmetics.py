# 구매한 화장품 목록 구하기 기능
#
# @param		inputData				입력데이터(화장품 판매 내역)
# @param		name					입력데이터(고객 ID)
# @param		term					입력데이터(기간)
# @return								구매한 화장품 목록
def getCosmeticsList(inputData, name, term):
    cosmeticsList = []
    ######################여기부터 구현 (1) ---------------->
    start = int(term[0:term.find("-")])
    end = int(term[term.find("-") + 1:])
    cosmeticsId = []
    tmpCosmeticsList = []

    for input in inputData:
        eachInputArr = input.split(",")
        currentDate = int(eachInputArr[3])
        if currentDate >= start and currentDate <= end and eachInputArr[1] == name:
            if eachInputArr[2] not in cosmeticsId:
                cosmeticsId.append(eachInputArr[2])
                tmpCosmeticsList.append(input)

    for str in tmpCosmeticsList:
        strArr = str.split(",")
        cosmeticsList.append(strArr[2])
    ############################# <-------------- 여기까지 구현 (1)
    return cosmeticsList

# 판매한 모든 화장품의 총액을 계산하는 기능
#
# @param		inputData				입력데이터(화장품 판매 내역)
# @param		sellerId				입력데이터(판매자 ID)
# @param		periodOfSale			입력데이터(기간)
# @return								총액
def getPrice(inputData, sellerId, periodOfSale):
    price = 0
    ######################여기부터 구현 (2) ---------------->

    start = int(periodOfSale[0:periodOfSale.find("-")])
    end = int(periodOfSale[periodOfSale.find("-") + 1:])

    for input in inputData:
        eachInputArr = input.split(",")
        currentDate = int(eachInputArr[3])
        if currentDate >= start and currentDate <= end and eachInputArr[0] == sellerId:
            price += int(eachInputArr[4])
    ############################# <-------------- 여기까지 구현 (2)
    return price
