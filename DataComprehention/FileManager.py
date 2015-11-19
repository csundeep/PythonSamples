def getListData(fileName):
    try:
        with open(fileName, "r") as data:
            return data.readline().strip().split(',')
    except IOError as err:
        print("data file missing", str(err))

def getDictionaryData(fileName):
    try:
        with open(fileName, "r") as data:
            temp=data.readline().strip().split(',')
            return {'name':temp.pop(0),
                    'dob':temp.pop(0),
                    'values':temp}
    except IOError as err:
        print("data file missing", str(err))