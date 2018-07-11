# 구현 내용

# 사용자에게 가위, 바위, 보 중 하나를 물어봅니다.
# 사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
# 다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.

# 힌트

# 리스트를 한 개를 사용하고 사용자의 입력을 받아야 합니다.
# 앞서 사용했던 임의 뽑기를 다시 사용합니다. 검색 키워드 : random, randint, shuffle
# 컴퓨터에게 가위, 바위, 보의 승패를 가르쳐줘야 합니다.

import random

user_choice = input("가위, 바위, 보 중 하나를 입력해 주세요")
computer_choice = ["가위", "바위", "보"]

print(user_choice)
print(random.choice(computer_choice))

#Result

if user_choice == computer_choice:
    print ("비겼습니다!")
elif user_choice == "가위":
    if computer_choice == "보":
        print("이겼습니다")
    else:
        print("졌습니다")
elif user_choice == "바위":
    if computer_choice == "가위":
        print("이겼습니다")
    else:
        print("졌습니다")
elif user_choice == "보":
    if computer_choice == "바위":
        print("이겼습니다")
    else:
        print("졌습니다")


    