import apicalls

class DataDictionary():

    def __init__(self):
        self.races = apicalls.getRaceData()
        self.classes = apicalls.getClassData()
        self.alignments = ["Lawful Good","Neutral Good","Chaotic Good","Lawful Neutral","Neutral","Chaotic Neutral","Lawful Evil","Neutral Evil","Chaotic Evil"]