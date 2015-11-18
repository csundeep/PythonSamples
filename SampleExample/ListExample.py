friends=list(['SANDEEP','KIRAN','BARU','SATYA','KOW','KIRANMI',['JAVA','C#','PYTHON']])
for friend in friends:
    if isinstance(friend, list):
        for lang in range(0, len(friend)):
            print(friend[lang])
    else:
        print(friend)  
        
# print(friends[0:3])
        
# print(friends[0]) 
# print(friends[1]) 
# print(friends[2]) 
# print(friends[3]) 
# print(friends[4]) 
# print(friends[5]) 
# print(friends[6][0]) 
# print(friends[6][1]) 
# print(friends[6][2]) 