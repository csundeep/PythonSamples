import DataConverter

data = list(['2:58', '2.58', '2:39', '2-25', '2-55', '2:54', '2.18', '2:55', '2:55'])
print(sorted(set([DataConverter.sanitize(each_t) for each_t in data])))
# print(sorted([set(DataConverter.sanitize(each_t)) for each_t in data]))
