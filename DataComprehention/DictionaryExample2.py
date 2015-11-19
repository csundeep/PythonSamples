import DataConverter
import FileManager

data = FileManager.getDictionaryData("data.txt")
print(data['name']+' data is',sorted(set([DataConverter.sanitize(each_t) for each_t in data['values']])))
