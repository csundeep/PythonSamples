import DataConverter

clean_data = []
unique_data=[]
data = list(['2:58', '2.58', '2:39', '2-25', '2-55', '2:54', '2.18', '2:55', '2:55'])

for each_t in data:
    if each_t not in clean_data:
        clean_data.append(DataConverter.sanitize(each_t))
        
for each_t in clean_data:
    if each_t not in unique_data:
        unique_data.append(each_t)
    
print(sorted(unique_data))
