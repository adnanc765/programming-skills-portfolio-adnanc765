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
#We got a larger table, lets invite more guests!
print("\nWe got a bigger table!")
guest.insert(0,' eusabio ')
guest.insert(2,' giorginago ')
guest.append('antonella')

name = guest[0].title()
print(name +" please come to dinner. ")

name = guest[1].title()
print(name +" please come to dinner. ")

name = guest[2].title()
print(name +" please come to dinner. ")

name = guest[3].title()
print(name +" please come to dinner. ")

name = guest[4].title()
print(name +" please come to dinner. ")

name = guest[5].title()
print(name +" please come to dinner. ")
#table won't arrive on time
print ("\nSorry, we cant only invite two people to dinner.")

name=guest.pop()
print("Sorry" + name +" there's no room at the table.")

name=guest.pop()
print("Sorry" + name +" there's no room at the table.")

name=guest.pop()
print("Sorry" + name +" there's no room at the table.")

name=guest.pop()
print("Sorry" + name +" there's no room at the table.")
#there should be two more people. Lets invite them!
name = guest[0].title()
print (name +", Please come to dinner.")

name = guest[1].title()
print (name +", Please come to dinner.")
#empty out the list.
del(guest[0])
del(guest[0])
#prove list is empty
print(guest)