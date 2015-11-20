import FileManager
person = FileManager.getObjectData("data.txt")
person.addValue('0.96')
person.addValues(['0.35','2.16'])
print(person.name+' person is',str(person.printOutput()))
