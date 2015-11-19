import DataConverter
import FileManager

data = FileManager.getListData("data.txt")
sandy_data={}
sandy_data['name']=data.pop(0)
sandy_data['dob']=data.pop(0)
sandy_data['values']=data
print(sandy_data['name']+' data is',sorted(set([DataConverter.sanitize(each_t) for each_t in sandy_data['values']])))
