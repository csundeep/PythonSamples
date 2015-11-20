import DataConverter
class Person:
    def __init__(self,a_name,a_dob,a_values):
        self.name=a_name
        self.dob=a_dob
        self.values=a_values
    def printOutput(self):
        return(sorted(set([DataConverter.sanitize(t) for t in self.values])))
    def addValue(self,newValue):
        self.values.append(newValue)
    def addValues(self,newValues):
        self.values.extend(newValues)