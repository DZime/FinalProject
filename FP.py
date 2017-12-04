# your code goes here#write performer names to the file

performers = [] #list of all the performers
per_day_dict = {} #key value pair for performer and their Day's

def writeToFile(performers):
    length = len(performers)
    filename = "textfile"+str(length)+".txt"
    file = open(filename,"w+")
    for performer in performers:
        file.write(performer)
        file.write("\n")
        file.close()
        
def admin():
    while True:
        print ('1. Add a performer')
        print ('2. Print performers')
        print ('3. Set price for each performer')
        print ('4. Print performers and their Days')
        print ('5. Exit admin mode')
        i = int(input());
        if i==1:
            print ('Enter the name')
            name = input();
            performers.append(name)
            writeToFile(performers)
        if i==2:
            for performer in performers:
                print (performer)
        if i==3:
            for performer in performers:
                print ('Enter the price for ')+ performer
                price = int(input())
                per_day_dict[performer] = day #Add the Days to ther performe
        if i==4:
            for key,value in per_day_dict.items(): #print the performers and their days
                print (key)
                print (value)
        if i==5:
            break #(quit)
def user():
    schedule = []
    cost = 0
    while True:
        print ('1. Purchase tickets')
        print ('2. Total price')
        print ('3. Print schedule')
        print ('4. Exit user mode')
        i = int(input())
        if i==1:
            for key,value in per_price_dict.items():
                print (key)
                print (value)
                print ('Enter the name of performer')
                name = input()
                schedule.append(name) #creates a list of performances to be attended
                print ('Enter the number of tickets')
                n = int(input()) #number of tickets for their performer
                for key,value in per_price_dict.items():
                    if key==name: #if the key equals of our performer name, update cost
                        cost = cost +value*n
                        break
                print ('Thanks for purchasing')
        if i==2:
            print ('Total cost of tickets is ')
            print (cost)
        if i==3:
            for performer in schedule: #print the to-attend list
                print ("Going to >>> ")+performer
                if i==4:
                    break

while True:
    print ('1. Admin')
    print ('2. User')
    choice = int(input())
    if choice==1:
        admin()
    elif choice==2:
            user()
    else:
        print ('Enter correct choice')

