from Person import Person
def getListData(fileName):
    try:
        with open(fileName, "r") as person:
            return person.readline().strip().split(',')
    except IOError as err:
        print("person file missing", str(err))
        
def getObjectData(fileName):
    try:
        with open(fileName, "r") as person:
            temp=person.readline().strip().split(',')
            return Person(temp.pop(0),temp.pop(0),temp)
    except IOError as err:
        print("person file missing", str(err))

def getDictionaryData(fileName):
    try:
        with open(fileName, "r") as person:
            temp=person.readline().strip().split(',')
            return {'name':temp.pop(0),
                    'dob':temp.pop(0),
                    'values':temp}
    except IOError as err:
        print("person file missing", str(err))