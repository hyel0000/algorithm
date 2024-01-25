def solution(friends, gifts):
    gift_dic = {}
    for i in gifts:
        gift_dic[i] = 0

    for i in gifts:
        if i in gift_dic.keys():
            gift_dic[i] = gift_dic[i] + 1

    # 준 선물
    give_dic = {}
    for key, value in gift_dic.items():
        name = key.split()
        if name[0] not in give_dic.keys():
            give_dic[name[0]] = value
        else:
            give_dic[name[0]] = give_dic[name[0]] + value

    for i in friends:
        if i not in give_dic.keys():
            give_dic[i] = give_dic.get(i, 0)

    # 받은 선물
    given_dic = {}
    for key, value in gift_dic.items():
        name = key.split()
        if name[1] not in given_dic.keys():
            given_dic[name[1]] = value
        else:
            given_dic[name[1]] = given_dic[name[1]] + value

    for i in friends:
        if i not in given_dic.keys():
            given_dic[i] = given_dic.get(i, 0)

    # 선물지수
    gift_index = {}
    for i in give_dic.keys():
        index = give_dic[i] - given_dic[i]
        gift_index[i] = index

    # 선물 주고받는 모든 경우의 수
    friend_poss = []
    i = 0
    while i <= len(friends) - 1:
        if i == 0:
            j = 1
            while j <= len(friends) - 1:
                fri_list = []
                fri_list.append(friends[i])
                fri_list.append(friends[j])
                j = j + 1
                friend_poss.append(fri_list)
            i = i + 1
        else:
            j = 0
            while j < i:
                fri_list = []
                fri_list.append(friends[i])
                fri_list.append(friends[j])
                j = j + 1
                friend_poss.append(fri_list)
            j = i + 1
            while j <= len(friends) - 1:
                fri_list = []
                fri_list.append(friends[i])
                fri_list.append(friends[j])
                j = j + 1
                friend_poss.append(fri_list)

            i = i + 1

    # 선물 주고받은 경우
    give_gift = []
    for i in gifts:
        give_list = []
        name = i.split()
        give_list.append(name[0])
        give_list.append(name[1])
        give_gift.append(give_list)
        give_list = []
        give_list.append(name[1])
        give_list.append(name[0])
        give_gift.append(give_list)

    # 선물 주고받지 않은 경우
    not_give = []
    for i in friend_poss:
        if i not in give_gift:
            not_give.append(i)

    # 다음달에 받을 선물의 수
    new_gift = {}
    for i in friends:
        new_gift[i] = new_gift.get(i, 0)

    # 선물 주고받은 경험없을때
    print(not_give)
    for i in not_give:
        if gift_index[i[0]] > gift_index[i[1]]:
            new_gift[i[0]] = new_gift[i[0]] + 1
    print(new_gift)

    # 선물 주고받았을때

    for key, value in gift_dic.items():
        name = key.split()
        opp_name = name[1] + ' ' + name[0]
        if opp_name not in gift_dic.keys():
            new_gift[name[0]] = new_gift[name[0]] + 1
        else:
            if value > gift_dic[opp_name]:
                new_gift[name[0]] = new_gift[name[0]] + 1
            elif value == gift_dic[opp_name]:
                if gift_index[name[0]] > gift_index[name[1]]:
                    new_gift[name[0]] = new_gift[name[0]] + 1

    print(new_gift)
    # return 값
    max = 0
    for value in new_gift.values():
        if value > max:
            max = value
    return max