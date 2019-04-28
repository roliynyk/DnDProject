import apicalls

class DataDictionary():
    def __init__(self):
        self.races = apicalls.getRaceData()
        self.classes = apicalls.getClassData()
