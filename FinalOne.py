performers = {} #list of all the performers and days
weekend = ['Friday','Saturday','Sunday','Three Day Price']
Prices = {}
TotalPrice = 0
def writeToFile(performers):
    length = len(performers)
    filename = "scheduale.txt"
    file = open(filename,"w+")
    for i,x in performers.items():
        file.write(x)
        file.write(': ')
        file.write(i)
        file.write("\n")
    file.close()
        
def setprice ():
    for i in weekend:
        tmpdate = input('What is the price for %s\n' %i)
        Prices[i] = tmpdate
       
def useradd ():
    added = int(input('How many Preformers would you like to add?\n'))
    for i in range(added):
        tmpname = input('Enter the name\n')
        tmpdates = input('Enter day preforming\n')
        performers[tmpname] = tmpdates
        writeToFile(performers)
    #print(performers)
    
def admin():
    while True:
        print ('1. Add a performer')
        print ('2. Print scheduale')
        print ('3. Set price for each day')
        print ('4. Print performers and their Days')
        print ('5. Exit admin mode')
        i = int(input())
        if i==1:
            useradd()
        if i==2:
                print(performers)
        if i==3:
           setprice()
        if i==4:
            for key,value in per_day_dict.items(): #print the performers and their days
                print (key)
                print (value)
        if i==5:
            break #(quit)
def user():
 print('Ticket Prices:')
 for i in Prices:
    print(i,'$',Prices[i])
 print('/n')
 while True:      
        print ('1. Purchase tickets')
        print ('2. Total price')
        print ('3. Print schedule')
        print ('4. Exit user mode')
        i = int(input())
        if i==1:
           while True:
                global TotalPrice
                print ('1. Friday')
                print ('2. Saturday')
                print ('3. Sunday')
                print ('4. Three Day Pass')
                print ('5. Done Purchasing')
                x = int(input('Enter what date you want to attend.'))
                if x==1:
                    TotalPrice += int(Prices['Friday'])
                    #Add Firdays value to total price
                if x==2:
                   TotalPrice += int(Prices['Saturday'])
                if x==3:
                    TotalPrice += int(Prices['Sunday'])

                if x==4:
                    TotalPrice += int(Prices['Three Day Price'])
                if x==5:
                    break
        if i==2:
            print ('Total cost of tickets is\n%d '% TotalPrice)
            
        if i==3:
            file = open('scheduale.txt','r')
            print(file.read())
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
