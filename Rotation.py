# 배열을 회전시키는 기능
#
# @param		inputData			입력데이터(이차원배열)
# @return							회전시킨 배열
def rotateArray(inputData):
    rotatedArray = []
    ######################여기부터 구현 (1) ---------------->
    rotatedArray = [[inputData[row][col] for col in range(len(inputData[row]))] for row in range(len(inputData))]

    for i in range(len(inputData)):
        for j in range(len(inputData[i])):
            if i == 0 or i == len(inputData)-1 or j == 0 or j == len(inputData[i])-1:
                rotatedArray[j][len(inputData)-i-1] = inputData[i][j]

    ############################# <-------------- 여기까지 구현 (1)
    return rotatedArray

# 같은 숫자가 인접한 칸을 찾아 0으로 설정하는 기능
#
# @param		rotatedArray		회전시킨 배열
# @return							설정된 배열
def setUpArray(rotatedArray):
    setArray = []
    ######################여기부터 구현 (2) ---------------->
    setArray = [[rotatedArray[row][col] for col in range(len(rotatedArray[row]))] for row in range(len(rotatedArray))]

    for i in range(1, len(rotatedArray) - 1):
        for j in range(1, len(rotatedArray[i]) - 1):
            if i == 1:
                if setArray[i][j] == setArray[i - 1][j]:
                    setArray[i][j] = 0

            elif i == len(rotatedArray) - 2:
                if setArray[i][j] == setArray[i + 1][j]:
                    setArray[i][j] = 0

            if j == 1:
                if setArray[i][j] == setArray[i][j - 1]:
                    setArray[i][j] = 0

            elif j == len(rotatedArray[i]) - 2:
                if setArray[i][j] == setArray[i][j + 1]:
                    setArray[i][j] = 0

    ############################# <-------------- 여기까지 구현 (2)
    return setArray
