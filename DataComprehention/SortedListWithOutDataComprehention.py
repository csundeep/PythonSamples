import DataConverter
import FileManager
clean_data = []
unique_data=[]
data = FileManager.getListData("temp.txt")

for each_t in data:
    if each_t not in clean_data:
        clean_data.append(DataConverter.sanitize(each_t))
        
for each_t in clean_data:
    if each_t not in unique_data:
        unique_data.append(each_t)
    
print(sorted(unique_data))
