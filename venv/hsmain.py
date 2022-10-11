# 임포트


# 플레이할 사람수 정하기
playerNum = int(input("플레이할 사람 수는 몇명?")) #인원 수
totalDB = [[0 for col in range(playerNum + 1)] for row in range(12)]

opDef = [
    ["조림지", -10, -15], #이름, 돈, 탄소배출량
    ["농장", 1, -5],
    ["금융 회사", 10, 0],
    ["반도체 공장", 20, 5],
    ["타이어 공장", 40, 20],
    ["화력 발전소", 60, 35],
    ]
totalCarbon = 0 #탄소 총량
turnNum = 10 #턴 수
tax = 0

def initTurn(turn, player):
    print(str(player + 1) + " 번의 차례입니다.")
    activate = int(input(opDef[totalDB[0][player + 1]][0] + " 을(를) 가동할까요? // 예 : 0 / 아니요 : 1 // "))

    while (True):
        if (activate == 0):
            money = opDef[totalDB[0][player + 1]][1]
            carbon = opDef[totalDB[0][player + 1]][2]
            print("공장을 가동합니다.")
            break
        elif (activate == 1):
            money = 0
            carbon = 0
            print("장비를 정지합니다.")
            break
        else:
            print("다시 입력하세요.")

    totalDB[turn+1][player+1] = money
    return carbon

def calculate(turn, player):

    if (totalCarbon < 200):
        tax = 0
    elif (totalCarbon < 300):
        tax = 1
    elif (totalCarbon < 400):
        tax = 2
    else :
        tax = 4

    if (tax > 0):
        for player in range(playerNum):
            if (totalDB[turn + 1][player + 1] != 0):
                totalDB[turn + 1][player + 1] -= opDef[totalDB[0][player + 1]][2]
    else:
        print("세금이 없습니다!")




for player in range(playerNum): #사업 정하기
     totalDB[0][player + 1] = int(input('플레이어 ' + str(player + 1) + ' 번의 사업을 정해주세요 : '))


for turn in range(turnNum): #턴 진행
    print(str(turn + 1) + " 번째 턴입니다.")
    for player in range(playerNum):
        totalCarbon += initTurn(turn, player)

    calculate(turn, player)  #턴 계산

#resultCalculate()




