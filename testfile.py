import pickle

def storeData(filename, data):
    f = open(filename, "ab")
    pickle.dump(data, f)
    f.close()
def clearPickle(filename):
    pickle.d
def loadData(filename):
    f = open(filename, "rb")
    l = pickle.load(f)
    f.close()
    return l

class Test:
    def __init__(self, id):
        self.id = id

    def getID(self):
        print(self.id)
t = Test(2354)
storeData("testsave", t)

d = loadData("testsave")
print(d)
d.getID()
