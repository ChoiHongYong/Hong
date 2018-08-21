#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Cosmetics.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from Cosmetics import *

def main():
    global nameValue, term, sellerId, periodOfSale
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()
    printInput(inputData)

    # 구매한 화장품 목록 구하기 기능
    cosmeticsList = getCosmeticsList(inputData, nameValue, term)
    printCosmeticsList(cosmeticsList)

    # 판매한 모든 화장품의 총액을 계산하는 기능
    price = getPrice(inputData, sellerId, periodOfSale)
    printPrice(price)

def loadData():
    global nameValue, term, sellerId, periodOfSale

    inputData = [
        "KIM,CUST02,CREAM02,25,35000",
        "KIM,CUST01,CREAM02,23,35000",
        "LEE,CUST04,CREAM02,12,35000",
        "LEE,CUST04,LOTION01,28,17000",
        "LEE,CUST04,SKIN01,19,15000",
        "LEE,CUST03,CREAM01,14,30000",
        "KIM,CUST01,SKIN02,31,24000",
        "LEE,CUST04,CREAM02,4,35000",
        "KIM,CUST01,SKIN01,29,15000",
        "KIM,CUST04,CREAM02,15,35000"
    ]
    ######################
    # 제공 데이터 세트 1
    ######################
    nameValue = "CUST04"
    term = "10-20"
    sellerId = "KIM";
    periodOfSale = "20-25";

    ######################
    # 제공 데이터 세트 2
    ######################

    # nameValue = "CUST02"
    # term = "20-30"
    # sellerId = "LEE";
    # periodOfSale = "10-15";

    return inputData

def printInput(inputData):
    printLineInitial()
    for str in inputData:
        print(str)
    printLine()

def printCosmeticsList(cosmeticsList) :
    print("[고객ID]: {}".format(nameValue))
    print("[기간]: {}".format(term))
    print("[구매한 화장품 목록 구하기]: ", end="")
    if len(cosmeticsList) == 0:
        print("결과값이 없습니다.")
    else:
        for name in cosmeticsList:
            print(name, end=" ")
        print()
    printLine()

def printPrice(price) :
    print("[기간]: {}".format(periodOfSale))
    print("[판매자({})가 판매한 모든 화장품의 총액]: ".format(sellerId), end="")
    if price == 0:
        print("결과값이 없습니다.")
    else:
        print(price)
    printLine()

def printLineInitial():
    print("[초기 입력 데이터]")

def printLine():
    print("--------------------------------------------------------------------------")

## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()