import re

with open('./Analysis/storage/INDEX-sorted-list.txt', 'r') as f:
    index_arr = [item.split('-') for item in f.read().split('\n')]

with open('./TY-Crawler/storage/target_enterprise_id&money_list.txt', 'r') as f:
    money_arr = [item.split(',') for item in f.read().split('\n')]

for i, item in enumerate(index_arr):
    if item[0] == '':
        break
    for m in money_arr:
        if item[0] == m[0]:
            money = re.findall(r'(\d+)', m[1])[0]
            item[1] = str(float(item[1])/int(money))
            print(item)
index_arr.pop()
index_arr.sort(key=lambda item: float(item[1]))

with open('./Analysis/storage/RELATE_INDEX-sorted-list.txt', 'w') as f:
    f.writelines(['{}\n'.format('-'.join(item)) for item in index_arr])

print(index_arr)
