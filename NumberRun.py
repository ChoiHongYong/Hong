#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Number.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from number.Number import *

def main():
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()

    # 큰 수 찾기 기능
    largeNumber = getLargeNumber(inputData)
    printLargeNumber(inputData, largeNumber)

    # 최종 숫자 구하기 기능
    finalNumber = getFinaleNumber(largeNumber)
    printFinalNumber(largeNumber, finalNumber)

def loadData():
    ######################
    # 제공 데이터 세트 1
    ######################

    inputData = 1234567


    ######################
    # 제공 데이터 세트 2
    ######################

    # inputData = 34217869

    return inputData



def printLargeNumber(inputData, largeNumber) :
    print("[두 수로 분리하여 큰 수 찾기]")
    print("입력: {}".format(inputData))
    print("출력:", end=" ")
    if largeNumber == 0:
        print("결과값이 없습니다.")
    else:
        print(largeNumber)
    printLine()

def printFinalNumber(largeNumber, finalNumber) :
    print("[최종 숫자 구하기]")
    print("입력:", end=" ")
    if largeNumber == 0:
        print("두 수로 분리하여 찾은 큰 수")
    else:
        print(largeNumber)
    print("출력:", end=" ")
    if finalNumber == 0:
        print("결과값이 없습니다.")
    else:
        print(finalNumber)
    printLine()

def printLine():
    print("--------------------------------------------------------------------------")

## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()