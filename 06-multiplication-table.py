# 구구단 만들기

# 사용자에게 몇 단 출력 할지 입력 받음 input
# 만약 사용자가 n를 입력하면 if
# 구구단 중 n단의 값을 출력 while 2번

inp = int(input("몇 단을 출력 하시겠습니까?"))

for num in range(1, 10):
    print("{} * {} = {}".format(inp, num, inp * num))