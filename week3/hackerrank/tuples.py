
n = int(input('enter:'))
integer_list = map(int, input().split())
integer_tuple = tuple(integer_list)
print(hash(integer_tuple))