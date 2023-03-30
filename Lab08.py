class ProbHash:
    def __init__(self, cap):
        self.hashtable = cap * [None]
        self.n = cap
    
    def hashFunction(self, mykey):
        return mykey % self.n
    
    def rehashFunction(self, hashkey):
        return (hashkey + 1) % self.n
    
    def insertData(self, student_obj):
        key = student_obj.getId()
        hashkey = self.hashFunction(key)
        while self.hashtable[hashkey] is not None and self.hashtable[hashkey].getId() != key:
            hashkey = self.rehashFunction(hashkey)
        self.hashtable[hashkey] = student_obj
        print("Insert", key, "at index", hashkey)
    
    def searchData(self, key):
        hashkey = self.hashFunction(key)
        while self.hashtable[hashkey] is not None and self.hashtable[hashkey].getId() != key:
            hashkey = self.rehashFunction(hashkey)
        if self.hashtable[hashkey] is not None:
            print("Found", key, "at index", hashkey)
            return self.hashtable[hashkey]
        else:
            print(key, "does not exist.")
            return None
        
class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def getGpa(self):
        return self.gpa
    
    def printDetail(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("GPA:", self.gpa)

class main():
    s1 = Student(65070001, "Sandee Boonmak", 3.05)
    s2 = Student(65070077, "Somsak Jaidee", 2.78)
    s3 = Student(65070021, "Somsri Jaiyai", 3.44)
    s4 = Student(65070042, "Sommai Meeboon", 2.89)
    myHash = ProbHash(20)
    myHash.insertData(s1)
    myHash.insertData(s2)
    myHash.insertData(s3)
    myHash.insertData(s4)
    print()

    std = myHash.searchData(65070077)
    std.printDetail()
    print("-------------------------")
    std = myHash.searchData(65070021)
    std.printDetail()
    print("-------------------------")
    std = myHash.searchData(65070042)
    std.printDetail()
    print("-------------------------")
    std = myHash.searchData(65070032)

main()