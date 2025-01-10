from collections import deque
# 데이터 저장
n, l = map(int, input().split())
a = list(map(int, input().split()))
mydeque = deque()

for i in range(n):
    # 덱의 마지막 위치에서부터 현재 값보다 큰 값을 덱에서 제거
    while mydeque and mydeque[-1][0] > a[i]:
        mydeque.pop()
    # 덱의 마지막 위치에 현재 값 저장 (인덱스, 숫자)
    mydeque.append((a[i], i))
    # 덱의 첫 번째 위치에서부터 l의 범위를 벗어난 값을 덱에서 제거
    # mydeque[0][1]=mydeque[0]의 두 번째 값(즉, 인덱스)
    # 다시말해, mydeque[0]는 첫 번째 요소(a[i], i)
    # mydeque[0][1]는
    # 이 튜플에서 인덱스 i를 가져옵니다.만약 mydeque가[(4, 0), (2, 1), (1, 2)]
    # 와 같이 되어 있다면: mydeque[0]는(4, 0) mydeque[0][1]는 0

    if mydeque[0][1] <= i - l:
        mydeque.popleft()
    # 덱의 첫 번째 데이터 출력
    print(mydeque[0][0], end=' ')
