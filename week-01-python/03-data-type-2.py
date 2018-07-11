# print("list")
# list_a = [1, 2, 3]
# print(list_a)

# # 0 부터 2 바로전까지 출력
# # print(list_a[0:2])
# # print(list_a[0:3])

# list_a.append(4)
# print(list_a)

# list_a.remove(2)
# print(list_a)

# list_a.clear()
# print(list_a)

# dic_a = {
#     "apple" : "a type of fruits",
#     "pen" : "a thing to write"
# }
# print(dic_a["pen"])
# dic_a["pen"] = "something to write"
# print(dic_a)

#set set([]) 중복불가!!
set_a = set([1, 2, 3])
set_b = set([2, 4, 6])
print(set_a)
print(set_b)

# 교집합, 합집합, 차집합
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)