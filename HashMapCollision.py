class HashMap:
    def __init__(self):
        self.MAX = 10
        self.arrr = [None for i in range(self.MAX)]

    def getHashKey(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, value):
        keyGot = self.getHashKey(key)
        self.arrr[keyGot] = value

    def __getitem__(self, key):
        keyGot = self.getHashKey(key)
        return self.arrr[keyGot]


objHashMap = HashMap()
objHashMap['FMCG'] = 564
objHashMap['Banking'] = 526
objHashMap['Insurance'] = 789
objHashMap['Pharma'] = 632

print(objHashMap.getHashKey('Insurance'))

print(objHashMap.arrr)
val = objHashMap['Banking']
print(val)

objHashMap.__setitem__('Insurance', 564)
print(objHashMap.arrr)

