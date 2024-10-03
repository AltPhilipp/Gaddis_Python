i = 0
name = "claus"

sentence = "        hello asd asdd   "

spaces = "hello name sein oder nicht sein"

sliced = name[0:4]  # Print first 4 characters (list does not include the 5th character)

print(sliced)

print(f"Length: {len(name)}")

for c in name:
    print(f"Character {i}: {c}")
    i += 1

if "c" not in name:
    print("There's no 'c' character in the name.")
else:
    print("The 'c' character is present in the name.")

print(name.upper())

print(sentence.strip())

print(spaces.split())  # spaces.split(" ") also works

print(name.endswith("aus"))

print(f"Finding: {spaces.find("o")}")

list = [1, 2, 3, 4, "Hello"]
tuple = (1, 2, 3, 4, 5)
set1 = {68, 1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5, 6, 1000}
set3 = {91992}

print(set)
print(list.pop())
print(list.index(2))
print(tuple.index(3))

print(f"Union: {set1.union(set2)}")  # Combine all unique elements
print(f"Intersection: {set1.intersection(set2)}")  # Provides all identical elements from set1
print(f"Difference: {set1.difference(set2)}")  # Provides all unique element from set1

print(set1.isdisjoint(set3))  # Checks if disjoint (no common elements)

