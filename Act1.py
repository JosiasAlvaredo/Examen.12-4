def intersect(list1, list2):
    new_list = []
    for i in  list1:
        if i in list2:
            new_list.append(i)
            while (new_list.count(i) > 1):
                index=list1.index(i)
                del new_list[index]
    return new_list

print(intersect([1,2,3,4,5],[3,3,4,5,6,7]))