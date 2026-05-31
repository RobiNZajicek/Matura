arr = [1,2,3,4,5]
print(arr[3]) # O(1)
print(3 in arr) # O[n]

hash_set = {1,2,3,4,5}
print(hash_set)

dictionary = {
    "id1": "Robin",
    "id2": "Adam"
}

print(dictionary["id1"])       # hledani podle klice O(1)
dictionary["id3"] = "Karel"    # pridani podle klice
print(dictionary)
print(hash("Robin"))           # ukazka hashovani