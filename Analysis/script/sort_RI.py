# 进行 风险指数排序
import json as praser


with open('./Analysis/storage/baked_data.json','r') as f:
    json = praser.loads(f.read())
    enterprise_ids = list(json.keys())
    f.close()

with open('./Analysis/storage/INDEX-list.txt','r') as f:
    enterprise_indexs = list([string.strip('\n') for string in f.readlines()])
    f.close()

enterprises = [(enterprise_ids[i],enterprise_indexs[i]) for i in range(len(enterprise_ids)) ]
enterprises.sort(key=lambda item: float(item[1]))
print(enterprises)

with open('./Analysis/storage/INDEX-sorted-list.txt','w') as f:
    f.writelines(['{}\n'.format('-'.join(item)) for item in enterprises])