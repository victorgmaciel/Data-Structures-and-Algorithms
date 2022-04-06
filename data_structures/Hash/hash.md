## HASHING 

Insertion, deletion, and search for most data structures, are up to 
O(logn) or O(nlogn) which is really good. 

However when we get to large amounts of data, these data structure's efficiency starts to be an issue. 

This is where Hashing comes into play. 


Hashing is a process that is used to store an object to a unique key. Hashing creates: 
    > key:value pair

the first type of hashing that we'll discuss is the hash table.(aka hash map) 

If you want to proritize search operations, hash table is probably the way to go because: 
1. it is faster than searching through an array
2. O(1) constant time so they scale well in algos

Python has several built in types of hashing which is: 
`set` and `dict`

The performance of a hash table depends on three fundamental factors:
1. Size of the hash table
2. the hash function
3. Collision handling





