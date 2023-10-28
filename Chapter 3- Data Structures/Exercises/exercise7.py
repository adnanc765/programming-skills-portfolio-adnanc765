places= ['portugal' , ' argentina' ,' madrid' ,' milan ' , ' turin ']

print ("Original order: ")
print (places)

print("\nAlphabetical: ")
print (sorted(places))

print("\nOriginal order:")
print(places)

print("\nReverse alphabetical:")
print(sorted(places, reverse=True))

print("\nOriginal order:")
print(places)

print("\nReversed:")
places.reverse()
print(places)

print("\nOriginal order:")
places.reverse()

print("\nAlphabetical")
places.sort()
print(places)

print("\nReversed alphabetical")
places.sort(reverse=True)
print(places)