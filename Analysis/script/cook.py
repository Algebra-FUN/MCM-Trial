import json
import re


class Cook:
    def __init__(self):
        self.__input_json()
        self.__output_data = {}

    def get_output_data(self):
        return self.__output_data

    def __input_json(self):
        with open('./Analysis/storage/raw_data.json', 'r', encoding='UTF-8') as f:
            raw_json = f.read()
        self.__in_dict = json.loads(raw_json)

    def __average(self, targets, k):
        if targets == 0:
            return 0
        length = len(targets)
        if length == 0:
            return 0

        def format_target(target):
            if '+' in str(target):
                return 1000
            nums = re.findall(r'(\d+)',str(target))
            if len(nums) == 0:
                return 0 
            return int(nums[0])

        return sum([format_target(target[k]) for target in targets])/length

    def __parse_gudongxinxi(self, v):
        return self.__average(v['gudongxinxi'], 'risk')

    def __parse_zhuyaorenyuan(self, v):
        return self.__average(v['zhuyaorenyuan'], 'risk')

    def __parse_guquanchuzhi(self, v):
        return self.__average(v['guquanchuzhi'], 'money')

    def __parse_biangengjilu(self, v):
        target = v['biangengjilu']
        if target == 0:
            return 0
        years = [int(re.findall(r'(\d{4})', string)[0]) for string in target]
        return len(target)/(max(years) - min(years) + 1)

    def parse_all_to_dict(self):
        for k, v in self.__in_dict.items():
            d = {}
            d['jingyingyichang'] = int(v['jingyingyichang'])
            d['gudongxinxi'] = self.__parse_gudongxinxi(v)
            d['biangengjilu'] = self.__parse_biangengjilu(v)
            d['zhuyaorenyuan'] = self.__parse_zhuyaorenyuan(v)
            d['guquanchuzhi'] = self.__parse_guquanchuzhi(v)
            self.__output_data[k] = d
        print(self.__output_data)


cook = Cook()
cook.parse_all_to_dict()
output = json.dumps(cook.get_output_data())
with open('./Analysis/storage/baked_data.json', 'w') as f:
    f.write(output)
