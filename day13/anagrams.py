def anagrams(*args):
    lst = list(args)

    def create_list_each_item(item):
        return sorted(list(item))

    mpobj = map(create_list_each_item, lst)

    def joining_string(item):
        return "".join(item)
    again_map = map(joining_string, mpobj)
    print(dict.fromkeys(again_map))

    # x = []
    # anagrams_list = []
    # for i in again_map:
    #     found = x.count(i)
    #     if (found):
    #         indx = x.index(i)
    #         lst
    #         # anagrams_list.append((found,fou))
    #     x.append(i)
    # print(x)


anagrams('race', 'care', 'part', 'trap')


# x = "python"
# # # one
# # print(list(x))

# y = [a for a in x]
# print(y)
