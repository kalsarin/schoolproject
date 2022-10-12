#프로그램 변수지정

opDef = [
    ["조림지", -10, -15],  # 이름, 돈, 탄소배출량
    ["농장", 1, -5],
    ["금융 회사", 10, 0],
    ["반도체 공장", 20, 5],
    ["타이어 공장", 40, 20],
    ["화력 발전소", 60, 35],
]
totalCarbon = 0  # 탄소 총량
turnNum = 10  # 턴 수
tax = 0


def startTurn(turn, player):
    cutZone('*')

    print(str(player + 1) + " 번의 차례입니다.")
    print("")

    while True:
        try:
            activate = int(input(opDef[totalDB[0][player + 1]][0] + " 을(를) 가동할까요? // 예 : 0 / 아니요 : 1 // "))

            if (activate != 1 and activate != 0):
                print("다시 입력해 주세요.")  # 범위가 잘못되었을때 출력
            else:
                break
        except ValueError:
            print("입력값이 숫자가 아닙니다.")  # 문자열이 들어가 입력값이 숫자가 아닐때 출력

    while (True):
        print("")
        if (activate == 0):
            money = opDef[totalDB[0][player + 1]][1]
            carbon = opDef[totalDB[0][player + 1]][2]
            print(opDef[totalDB[0][player + 1]][0] + " 을(를) 가동합니다.")
            break
        elif (activate == 1):
            money = 0
            carbon = 0
            print("장비를 정지합니다.")
            break
        else:
            print("다시 입력해 주세요.")

    totalDB[turn + 1][player + 1] = money
    return carbon


def calculate(turn, player):
    if (totalCarbon < 200):
        tax = 0
    elif (totalCarbon < 300):
        tax = 1
    elif (totalCarbon < 400):
        tax = 2
    else:
        tax = 4

    if (tax > 0):
        for player in range(playerNum):
            if (totalDB[turn + 1][player + 1] != 0):
                totalDB[turn + 1][player + 1] -= (opDef[totalDB[0][player + 1]][2] * tax)

    return tax


def printChart():
    print("%7s" % '번호', end='')
    for player in range(1, playerNum + 1):
        print("%7s" % str(player), end='')
    print("")
    for i in range(1, 11):
        print("%7s" % str(i) + "년", end='')
        for j in range(1, playerNum + 1):
            print("%7s" % str(totalDB[i][j]), end='')
        print("")


def cutZone(char):
    print("")
    print(str(char) * 50)
    print("")


def totalCalculate():
    cutZone('@')
    maxMoney = 0
    winner = 0
    for player in range(playerNum):
        totalMoney = 0
        for year in range(1, 12):
            totalMoney += totalDB[year][player + 1]
        print("플레이어 " + str(player + 1) + "번이 번 돈 : " + str(totalMoney))
        if (totalMoney > maxMoney):
            maxMoney = totalMoney
            winner = player + 1
    cutZone('@')
    print("가장 돈을 많이 번 사람 : " + str(winner) + "번 플레이어")



#프로그램 시작

#프로그램 시작 전 규칙 출력하기
cutZone(r'#')
print("지구는 환경오염에 처해 있습니다. 옆에 표를 참고하여 환경을 파괴하지 않는 선에서 돈을 많이 버는 팀이 승리합니다."
      "\n플레이어는 사업을 실행시킬지 말지 두가지를 선택할 수 있습니다. 사업을 실행시킬때마다 각각의 규칙에 따라 총 탄소량이 늘고 돈을 벌게 됩니다."
      "\n이때 탄소가 늘게 되면 세금 징수량이 늘어나니 이를 잘 조절해서 돈을 많이 버십시오. 화이팅!")
cutZone(r'#')

while (True):
    try:
        playerNum = int(input("게임을 플레이 할 인원은 몇명? "))  # 인원 수

        if (playerNum < 2):
            print("다시 입력해 주세요.")  # 범위가 잘못되었을때 출력
        else:
            break

    except ValueError:
        print("입력값이 숫자가 아닙니다.")  # 문자열이 들어가 입력값이 숫자가 아닐때 출력

    except IndexError:
        print("입력값이 범위가 아닙니다.")  # 입력값이 범위가 아닐때 출력

totalDB = [[0 for col in range(playerNum + 1)] for row in range(12)]

for player in range(playerNum):  # 사업 정하기
    while True:
        try:
            totalDB[0][player + 1] = int(input('플레이어 ' + str(player + 1) + ' 번의 사업을 정해주세요. : '))
            if (totalDB[0][player + 1] >= 0 and totalDB[0][player + 1] <= 5):
                print(str(player + 1) + "번 플레이어의 사업은 " + opDef[totalDB[0][player + 1]][0] + "입니다.")
                print("")
                break
            else:
                print("다시 입력해 주세요.")  # 범위가 잘못되었을때 출력


        except ValueError:
            print("입력값이 숫자가 아닙니다.")  # 문자열이 들어가 입력값이 숫자가 아닐때 출력

        except IndexError:
            print("입력값이 범위가 아닙니다.")  # 입력값이 범위가 아닐때 출력



for turn in range(turnNum):  # 턴 진행

    for player in range(playerNum):

        totalCarbon += startTurn(turn, player)

        if (player + 1 != playerNum):
            cutZone('*')
            print("%7s" % str(turn + 1) + "턴 진행중")
            cutZone('*')
            printChart()
            print("")
            print("현재 총 탄소량 : " + str(totalCarbon))
            print("")

    tax = calculate(turn, player)

    cutZone('@')
    print("%7s" % str(turn + 1) + "턴 결과")
    cutZone('@')
    printChart()
    print("")
    print("현재 총 탄소량 : " + str(totalCarbon))
    print("현재 세금 : kg 당 " + str(tax) + "원")
totalCalculate()
a = input("")







