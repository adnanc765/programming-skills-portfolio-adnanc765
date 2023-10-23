guest= [' Cristiano ronaldo' , ' Lionel messi' , ' Diego maradona']

name= guest[0].title()
print (name + ", please come to dinner.")

name= guest[1].title()
print (name + ", please come to dinner.")

name= guest[2].title()
print (name + ", please come to dinner.")

name= guest[1].title()
print ("\nSorry, " + name + " can't make it to dinner. " )

#Messi can't make it to the dinner, let's invite neymar JR instead.
del(guest[1])
guest.insert (1, ' Neymar JR ')

#print invitation again.
name=guest[0].title()
print("\n" + name + ", please come to dinner.")

name=guest[1].title()
print(name + ", please come to dinner.")

name=guest[2].title()
print(name + ", please come to dinner.")