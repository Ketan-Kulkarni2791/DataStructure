class GetHashMap:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]  # Initializaing 100 elements in the array with the value none.

    def getHash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.getHash(key)
        self.arr[h] = value

    def __getitem__(self, item):
        h = self.getHash(item)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.getHash(key)
        self.arr[h] = None


objGetHashMap = GetHashMap()
objGetHashMap['march 6'] = 120
objGetHashMap['march 7'] = 130
objGetHashMap['march 8'] = 140
objGetHashMap['march 9'] = 150
objGetHashMap['march 10'] = 160
objGetHashMap['march 11'] = 170
objGetHashMap['march 12'] = 200

valueGot = objGetHashMap['march 10']

print(objGetHashMap.arr)
print(valueGot)

objGetHashMap.__delitem__('march 8')
print(objGetHashMap.arr)
