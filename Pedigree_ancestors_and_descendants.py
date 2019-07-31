n = int(input())
gen_tree = dict()
people = set()
count_dict = dict()
amount_arr = []
for i in range(n-1):
    ancestor, parent = input().split()
    people.add(ancestor)
    people.add(parent)
    gen_tree[ancestor] = parent
for human in people:
    count_dict[human] = 0
    smn = human
    while smn in gen_tree.keys():
        smn = gen_tree[smn]
        count_dict[human] += 1
for i in range(int(input())):
    h1, h2 = input().split()
    if count_dict[h2] > count_dict[h1]:
        smn = h2
        while count_dict[smn] > count_dict[h1]:
            smn = gen_tree[smn]
        if smn == h1:
            amount_arr.append(1)
        elif smn != h1:
            amount_arr.append(0)
    elif count_dict[h1] > count_dict[h2]:
        smn = h1
        while count_dict[smn] > count_dict[h2]:
            smn = gen_tree[smn]
        if smn == h2:
            amount_arr.append(2)
        elif smn != h2:
            amount_arr.append(0)
    else:
        amount_arr.append(0)
print(*amount_arr)
