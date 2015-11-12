friends=list(['SANDEEP','KIRAN','BARU',['JAVA','C#','PYTHON']])
for friend in friends:
    if isinstance(friend, list):
        for lang in range(0, len(friend)):
            print(friend[lang])
    else:
        print(friend)  
        
# print(friends[0]) 
# print(friends[1]) 
# print(friends[2]) 
# print(friends[3][0]) 
# print(friends[3][1]) 
# print(friends[3][2]) 