import DataConverter
import FileManager

data = FileManager.getListData("temp.txt")
print(sorted(set([DataConverter.sanitize(each_t) for each_t in data])))
# print(sorted([set(DataConverter.sanitize(each_t)) for each_t in data]))
