classes = {}
for _ in range(int(input())):
    item, *parents = input().replace(':', '').split()
    classes[item] = parents
#print(classes)
tested = []
for _ in range(int(input())):
    searchlst = []
    tested_item = input()
    searchlst += classes[tested_item]
    while len(searchlst) > 0:
        firstel = searchlst[0]
        del searchlst[0]
        if firstel in tested:
            print(tested_item)
            break
        else:
            searchlst += classes[firstel]
    else:
        tested.append(tested_item)