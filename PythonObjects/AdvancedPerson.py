import DataConverter
class AdvancedPerson(list):
    def __init__(self,a_name,a_dob,a_values):
        list.__init__([])
        self.name=a_name
        self.dob=a_dob
        self.extend(a_values)
    def printOutput(self):
        return(sorted(set([DataConverter.sanitize(t) for t in self])))
    def addValue(self,newValue):
        self.append(newValue)
    def addValues(self,newValues):
        self.extend(newValues)