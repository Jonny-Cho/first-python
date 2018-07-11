# 함수 functions
# 입력값 parameters, 반환값 return

def hello_friends(name):
    print("Hi, {}".format(name))

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"

# print("Hi, {}".format(name1))
# print("Hi, {}".format(name2))
# print("Hi, {}".format(name3))
# print("Hi, {}".format(name4))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)

# 반환(리턴)값이 있는 것은 변수에 담을 수 있다.
# 1) 입력값 o, 반환값 o
def sum(a, b):
    return a + b

# 2) 입력값 o, 반환값 x
def hello_friends(name):
    print("Hi, {}".format(name))

# 3) 입력값 x, 반환값 o
def return_1():
    return 1

# 4) 입력값 x, 반환값 x
def hello_world():
    print("hello world")

#  num_1 = return_1()
#  print(num_1)