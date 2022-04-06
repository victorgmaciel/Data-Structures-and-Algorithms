"""
Create a class for hashing
"""
class HashEntry:
    def __init__(self, key, data):
        #The key of the entry
        self.key = key
        #data stored
        self.value = data
        #reference to new entry
        self.nxt = None
    def __str__(self):
        return str(entry.key) + ", " + entry.value

entry = HashEntry(4, "Left")
print(entry)

class HashTable:
    #constructor for class
    def __init__ (self):
        #size of table
        self.slots = 10
        self.size = 0
        #list of hashentrys
        self.bucket = [None] * self.slots
    
    def get_size(self):
        return self.size
    def is_empty(self):
        return self.get_size() == 0

#hash function 
def get_index(self, key):
    #hash is a built in function in Py
    hash_code = hash(key)
    index = hash_code % self.slots
    return index

#Hash table is ready!
#Note: resizing and other functions are not in this file. 