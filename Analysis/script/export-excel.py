import xlwt

wb = xlwt.Workbook()
target = ['INDEX', 'INDEX_LOG', 'RELATE_INDEX']

for name in target:
    with open('./Analysis/storage/{}-sorted-list.txt'.format(name), 'r') as f:
        arr = f.readlines()
        ws = wb.add_sheet(name)
        for i, txt in enumerate(arr):
            txt = txt.strip('\n')
            txt = txt.split('-')
            for j in range(2):
                ws.write(i, j, txt[j])

wb.save('./Analysis/storage/INDEX.xls')
