#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Product.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from Product import *

def main():
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()

    # 문자열을 변경하는 기능
    newStr = getNewStr(inputData)
    printNewStr(inputData, newStr)

    # 상품번호를 생성하는 기능
    productNum = getProductNum(newStr)
    printProductNum(newStr, productNum)

def loadData():
    ######################
    # 제공 데이터 세트 1
    ######################

    inputData = "371B4A4"


    ######################
    # 제공 데이터 세트 2
    ######################

    # inputData = "5312D6C"

    return inputData


def printNewStr(inputData, newStr) :
    print("[변경된 문자열]")
    print("입력: {}".format(inputData))
    print("출력: ", end="")
    if(newStr == ""):
        print("결과값이 없습니다.")
    else:
        print(newStr)
    printLine()


def printProductNum(newStr, productNum) :
    print("[상품번호]")
    print("입력: ", end="")
    if(newStr == ""):
        print("변경된 문자열")
    else:
        print(newStr)
    print("출력: ", end="")
    if (productNum == ""):
        print("결과값이 없습니다.")
    else:
        print(productNum)
    printLine()


def printLine():
    print("--------------------------------------------------------------------------")


## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()
