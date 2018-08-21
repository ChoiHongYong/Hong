#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Rotation.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from rotation.Rotation import *

def main():
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()
    printInput(inputData)

    # 배열을 회전시키는 기능
    rotatedArray = rotateArray(inputData)
    printRotateArray(rotatedArray)

    # 같은 숫자가 인접한 칸을 찾아 0으로 설정하는 기능
    setArray = setUpArray(rotatedArray)
    printSetUpArray(setArray)

def loadData():
    ######################
    # 제공 데이터 세트 1
    ######################

    inputData = [
        [1, 2, 2, 5, 4],
        [3, 1, 3, 3, 2],
        [5, 2, 3, 4, 4],
        [2, 4, 4, 5, 1],
        [4, 1, 5, 3, 5]
    ]


    


    ######################
    # 제공 데이터 세트 2
    ######################

    # inputData = [
    #     [2, 5, 5, 5, 5],
    #     [2, 2, 2, 5, 4],
    #     [2, 3, 1, 5, 4],
    #     [2, 3, 4, 5, 4],
    #     [3, 3, 3, 3, 4]
    # ]

    return inputData
def printInput(inputData):
    printLineInitial()
    for i in range(len(inputData)):
        for j in range(len(inputData[i])):
            print(inputData[i][j], end = " ")
        print()
    printLine()

def printRotateArray(rotatedArray) :
    print("[회전시킨 배열]")
    if len(rotatedArray) == 0:
        print("결과값이 없습니다.")
    else:
        for i in range(len(rotatedArray)):
            for j in range(len(rotatedArray[i])):
                print(rotatedArray[i][j], end=" ")
            print()
    printLine()

def printSetUpArray(setArray) :
    print("[인접한 같은 숫자를 0으로 설정한 배열]")
    if len(setArray) == 0:
        print("결과값이 없습니다.")
    else:
        for i in range(len(setArray)):
            for j in range(len(setArray[i])):
                print(setArray[i][j], end=" ")
            print()
    printLine()

def printLineInitial():
    print("[초기 입력 데이터]")

def printLine():
    print("--------------------------------------------------------------------------")

## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()