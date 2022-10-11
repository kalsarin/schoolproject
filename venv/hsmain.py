# 임포트

# 플레이할 사람수 정하기
playernumber = int(input("플레이할 사람 수는 몇명?"))
playerdb = [[0 for col in range(playernumber)] for row in range(11)]

# 게임규칙 정의 [번호, 수익, 탄소배출량]
plantation = [0, -10, -15]  # 조림지
farm = [1, 1, -5]  # 농장
finance = [2, 10, 0]  # 경영
semiconductor = [3, 20, 5]  # 반도체
tire = [4, 40, 20]  # 타이어
thermalpp = [5, 60, 35]  # 화력발전
totalcarbon = 0


print("")
setup()

for turnCount in range(10):
    for playerNum in range(playerCount):
        turn(playerNum,turnCount)
    calculate()

def turn(player,turnCount):
    player = playerNum
    turn = turnCount

# 입출력