# 임포트


# 플레이할 사람수 정하기
playerNum = int(input("플레이할 사람 수는 몇명?")) #인원 수
totalDB = [[0 for col in range(playernumber)] for row in range(12)]
opDef = [[]]
totalCarbon = 0 #탄소 총량
turnNum = 10 #턴 수



# 게임규칙 정의 [번호, 수익, 탄소배출량]
plantation = [0, -10, -15]  # 조림지
farm = [1, 1, -5]  # 농장
finance = [2, 10, 0]  # 경영
semiconductor = [3, 20, 5]  # 반도체
tire = [4, 40, 20]  # 타이어
thermalpp = [5, 60, 35]  # 화력발전

#사업 번호 출력

for player in range(playerNum): #사업 정하기
     = int(input("플레이어", player + 1, "번의 사업을 정해주세요 : "))

for turn in range(turnNum): #턴 진행
    print(turn + 1, "번째 턴입니다.")
    for player in range(playerNum):
        initTurn(turn,player)
    calculate(turn,player)  #턴 계산

resultCalculate()


def initTurn(turn,player):
    print(player + 1, "번의 차례입니다.")
    activate = int(input("공장을 가동할까요? // 예 : 0 / 아니요 : 1"))
    if (activate = )



