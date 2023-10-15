"""
(number) BaseBall Game -> bbg
Rule: https://namu.wiki/w/%EC%88%AB%EC%9E%90%EC%95%BC%EA%B5%AC
"""
import random
import time

def countStrike(myAns, Ans):
    assert len(myAns) == len(Ans), 'Len Error' # 자릿수가 난이도와 같지 않다면
    L = len(Ans)
    s = 0
    for i in range(L):
        for j in range(L):
            if (i == j) and (myAns[i] == Ans[j]): s += 1
    return s

def countBall(myAns, Ans):
    assert len(myAns) == len(Ans), 'Len Error' # 자릿수가 난이도와 같지 않다면
    L = len(Ans)
    b = 0
    for i in range(L):
        for j in range(L):
            if (i != j) and (myAns[i] == Ans[j]): b += 1
    return b

while True:
    try_count = 0
    start_time = time.time()
    level = int(input('number of dights: ')) # 난이도 설정

    numList = list(range(0, 10))
    ansList = random.sample(numList, level) # 자릿수만큼 추출
    ans = ''

    for num in ansList:
        ans += str(num) # 컴퓨터가 랜덤으로 설정한 수

    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print('Start!!')

    while True:
        myans = input('answer: ') # 사용자가 예상하는 답 받기
        if myans == 'ans':
            print(ans)
            break
        try:
            int(myans)
        except ValueError: print('input again') # 숫자가 아닌 문자가 포함되어있다면
        else:
            if len(myans) != level: print('input again') # 자릿수와 난이도가 같지 않다면
            elif len(myans) != len(set(myans)): print('input again') # 방금 입력한 예상 답안에 같은 숫자가 포함되어있다면
            else: # 제대로 된 형식의 정답이라면
                s = countStrike(myans, ans)
                b = countBall(myans, ans)
                if s == level: # 정답이라면
                    assert b == 0, "it's wrong." # 오류 체크
                    end_time = time.time()
                    print('GREAT!!, time=%0.4fsec, number of tries: %d' % ((end_time - start_time), try_count))
                    break
                else:
                    if (s, b) == (0, 0): print('Out!!')
                    elif s == 0: print('%db' % b)
                    elif b == 0: print('%ds' % s)
                    else: print('%ds %db' % (s, b))
                    try_count += 1

    cmd = input('end? ') # 게임이 끝났는지 묻는 차례
    if cmd == '': break # 아무 키도 없이 그냥 엔터만 눌렸다면 Yes로 받아들여 게임 중지