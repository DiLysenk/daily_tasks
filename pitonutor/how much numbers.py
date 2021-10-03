a = {i for i in input().split()}
b = {i for i in input().split()}
a.intersection_update(b)
a = sorted(a)
a = list(a)

for i in a:
    print(" ".join(i))




# a = {i for i in input().split()}
# b = {i for i in input().split()}
# a.intersection_update(b)
#
#
# print(a)



# a = {i for i in input().split()}
# print(len(a))

