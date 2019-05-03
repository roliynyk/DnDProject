import apicalls

class DataDictionary():

    def __init__(self):
        self.races = apicalls.getRaceData()
        self.classes = apicalls.getClassData()
        self.alignments = ["Lawful Good","Neutral Good","Chaotic Good","Lawful Neutral","Neutral","Chaotic Neutral","Lawful Evil","Neutral Evil","Chaotic Evil"]
        self.classNameDict = {i['name']:i['index']-1 for i in self.classes}
        self.raceNameDict = {i['name']:i['index']-1 for i in self.races}
#     def retNames(self, var):
#         for i in var:
#             print(i["name"])


print(DataDictionary().raceNameDict)
# data = DataDictionary()
# data.retNames(data.classes)
