#write performer names to the file
def writeToFile(performer):
    length = len(performer)
#New list of performers is created
    filename = "performers"+str(length)+".txt"
    file = open(filename,"w+")
    for performer in performer:
        file.write(performer)
        file.write("\n")
    file.close()
performer = [] #list of all the performers

d={}
for i in range(4):
    performer=input("Enter schedule %s performer:\n" % (i+1))
    day=input("Enter performer %s day:\n" % str(i+1))

    if performer not in d:
        d[performer]=day
    print()

print("SCHEDULE")
for p,v in sorted(d.items()):
    print("%s:%s" % (v,p))

print()

while True:
    print('\na - Add performer')
    print('d - Remove performer')
    print('u - Update performer day')
    print('o - Output schedule')
    print('q - Quit')

    choice=input('\nChoose an option:\n')
    choice=choice.lower()
  
    if choice=='o':
        print("\nSchedule")
        for p,v in sorted(d.items()):
            print("%s:%s" % (v,p))

    elif choice=='a':
        performer=input("Enter a new performer:\n")
        day=input("Enter performer day:\n")

        if performer not in d:
            d[performer]=day
        else:
            print("\nThe performer already in the list")

    elif choice== 'd':
        performer=input("\nEnter a performer:\n")

        if performer in d:
            del d[performer]
        else:
            print("\nThe performer is not in the list")

    elif choice== 'u':
        performer=input("\nEnter a performer:\n")

        if performer in d:
            day=input("\nEnter a new day for the performer:\n")
            d[performer]=day
        else:
            print("\nThe performer is not in the list")

    elif choice=='q':
        break
    else:
        print("\nEnter a valid choice")
