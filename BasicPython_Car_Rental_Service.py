
def mainmenu():
    print('Welcome to Car Rental Service'+'\n')
    print('1. Car Available to Rent\n2. Login\n3. Register\n4. Admin\n5. Exit')
    ans = input('Please Enter a Number above: ')
    if ans == '1':
        loadavailable()
        mainmenu()
    if ans == '2':
        login()
    if ans == '3':
        register()
    if ans == '4':
        admin()
    if ans == '5':
        exit()    
    else: 
        mainmenu()


def adminmenu():
    print('Welcome to Admin Menu')
    print('1. Add Car to be Rented\n2. Modify Car Details\n3. Display All Records\n4. Search Record\n5. Exit')
    ans = input('Please Enter a Number Above: ')
    if ans == '1':
        admin_add_car()    
    if ans == '2':
        modify_car()
    if ans == '3':
        loadavailable()
        loadunavailable()
        adminmenu()
    if ans == '4':
        search_cus_booking()
    if ans == '5':
        exit()
    else:
        print('Invalid Input')
        adminmenu()


def usermenu():
    print('Welcome to User Menu\n1. Modify Personal Detail\n2. View Rental History\n3. View Car Available\n4. Book a Car\n5. Return Car\n6. Exit')
    ans=input('Enter a Number: ')
    if ans == '1':
        personal_modify()
    if ans == '2':
        cusrental_history()
    if ans == '3':
        loadavailable()
        usermenu()
    if ans == '4':
        booking()
    if ans == '5':
        returncar()
    if ans == '6':
        exit()
    else:
        print('Invalid Input')
        usermenu()



####################################################################################################

def login():
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    name = loaduser_id()
    pass1 = loaduser_password()
    index = -1
    for count in range(len(name)):
        if(username==name[count]):
            index = count
            break
    if(pass1[index] == password):
        print('Login Success!!')
        usermenu()
    else:
        print('Input Invalid')
        mainmenu()

def register():
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    confirmpassword=input('Confirmed password: ')
    name = loaduser_id()
    for i in name:
        if(username == i):
            print('User Already Exist!')
            break
        if(password == confirmpassword):
            record=open('account.txt','a')
            record.write(username+':'+password+'\n')
            record.close()
            print('Register Success!')
            personal_details()
        if(password != confirmpassword):
            print('Invalid Input Please Try again')
            register()

def personal_details():
    ic_number=input("Enter your IC number: ")
    email=input("Enter your email address: ")
    phone=input("Enter yor contact number: ")
    everything=str(ic_number+':'+email+':'+phone+'\n')
    ic = loadpersonal_ic()
    email1 = loadpersonal_email()
    phone1 = loadpersonal_phone()
    for i in ic:
        if ic_number in i:
            print('User Exist!')
            personal_details()
    for i in email1:
        if email in i:
            print('User Exist')
            personal_details()
    for i in phone1:
        if phone in i:
            print('User Exist')
            personal_details()

    record=open('personaldata.txt','a')
    record.write(everything)
    record.close()
    print('Registre Success!')
    usermenu()

def admin():
    adminid=input("Enter your AdminID: ")
    adminpass=input("Enter your password: ")
    idmin = load_adminid()
    pass1 = load_adminpassword() 
    index = -1
    for count in range(len(adminid)):
        if(adminid==idmin[count]):
            index = count
            break
    if(pass1[index] == adminpass):
        print('Login Success!!')
        adminmenu()
    else:
        print('Input Invalid')
        mainmenu()

##################################################################

def admin_add_car():
    car_plate=input('Enter the Car plate Number: ')
    car_model=input('Enter the Car Model: ')
    car_brand=input('Enter the car brand: ')
    car_seat=input('Enter the total Car Seat Available: ')
    car_price=input('Enter Car Price per Day: ')
    carlist=loadcar_plate()
    i = 0
    while i < len(carlist):
        if car_plate in carlist:
            print('Car Exist! Please try again')
            admin_add_car()
        else:
            car=open('car.txt','a')
            car.write(car_plate+':'+car_model+':'+car_brand+':'+car_seat+':'+car_price+'\n')
            car.close()
            print('Car Registerd Successfully')
            adminmenu()

def modify_car():
    allcar = loadallcar()
    plate = loadcar_plate()
    ans = input('Enter your Car Plate Number: ')
    i = 0
    while i < len(plate):
        if ans in plate:
            count_position = plate.index(ans)
            if (len(allcar[count_position]) == 5):
                print('1. Car Plate: ', allcar[count_position][0])
                print('2. Car Model: ', allcar[count_position][1])
                print('3. Car Brand: ', allcar[count_position][2])
                print('4. Car Seat: ', allcar[count_position][3])
                print('5. Price: ', allcar[count_position][4])
                ans1 = input('Enter the field you want to change: ')
                intans = int(ans1)
                change = input('Enter the change: ')
                confirm = input('Confirm your change: ')
                if change == confirm:
                    allcar[count_position][intans-1]=change
                    with open('car.txt', 'w') as fh:
                        cnt = 0
                        newcontent = ""
                        while (cnt < len(allcar)):
                            recstr = ":".join(allcar[cnt])
                            newcontent += recstr + "\n"
                            cnt += 1
                        fh.write(newcontent)
                        fh.close()
                    print('Modify Success!')
                    adminmenu()
            if (len(allcar[count_position]) > 5):
                print('1. Car Plate: ', allcar[count_position][0])
                print('2. Car Model: ', allcar[count_position][1])
                print('3. Car Brand: ', allcar[count_position][2])
                print('4. Car Seat: ', allcar[count_position][3])
                print('5. Price: ', allcar[count_position][4])
                print('6. CustomerID: ',allcar[count_position][5])
                print('7. Payment Date: ',allcar[count_position][6])
                print('8. Booking Date: ',allcar[count_position][7])
                print('9. Return Date: ',allcar[count_position][8])
                print('10. Total Price: ',allcar[count_position][9])
                print('11. Credit card No: ',allcar[count_position][10])
                print('12. CVV: ',allcar[count_position][11])
                ans1 = input('Enter the field you want to change: ')
                intans = int(ans1)
                change = input('Enter the change: ')
                confirm = input('Confirm your change: ')
                if change == confirm:
                    allcar[count_position][intans - 1] = change
                    with open('car.txt', 'w') as fh:
                        cnt = 0
                        newcontent = ""
                        while (cnt < len(allcar)):
                            recstr = ":".join(allcar[cnt])
                            newcontent += recstr + "\n"
                            cnt += 1
                        fh.write(newcontent)
                        fh.close()
                    print('Modify Success!')
                    adminmenu()
        if ans not in i:
            print('Invalid Input')
            adminmenu()




def search_cus_booking():
    ans = str(input('Enter Customer ID: '))
    name = loaduser_id()
    book = booked()
    cusid = booked_cusid()
    i =0
    while i < len(name):
        if ans in name:
            count_position = cusid.index(ans)
            print('1. CustomerID: ',book[count_position][5])
            print('2. Car Plate: ',book[count_position][0])
            print('3. Car Model: ',book[count_position][1])
            print('4. Car Brand: ',book[count_position][2])
            print('5. Car Seat: ',book[count_position][3])
            print('6. Car Price: ',book[count_position][4])
            print('7. Date of Payment: ',book[count_position][6])
            print('8. Date of Booking: ',book[count_position][7])
            print('9. Date of Return: ',book[count_position][8])
            print('10. Total Price: ',book[count_position][9])
            print('11. Credit Card Number: ',book[count_position][10])
            print('12. CVV: ',book[count_position][11])
            ans2=input('Enter Y if you want to search again: ')
            if ans2 == 'Y':
                search_cus_booking()
            else:
                adminmenu()
        else:
            print('Record Not Exist!')
            search_cus_booking()


####################################################################
def personal_modify():
    alldata = loadall_personal()
    ic = loadpersonal_ic()
    ans = input('Enter your IC Number: ')
    i = 0
    while i < len(ic):
        if ans in ic:
            count_position = ic.index(ans)
            print('1. IC Number: ', alldata[count_position][0])
            print('2. Email: ', alldata[count_position][1])
            print('3. Phone: ', alldata[count_position][2])
            ans1 = input('Enter the field you want to change: ')
            intans = int(ans1)
            change = input('Enter the change: ')
            confirm = input('Confirm your change: ')
            if change == confirm :
                alldata[count_position][intans - 1] = change
                with open('personaldata.txt', 'w') as fh:
                    cnt = 0
                    newcontent = ""
                    while (cnt < len(alldata)):
                        recstr = ":".join(alldata[cnt])
                        newcontent += recstr + "\n"
                        cnt += 1
                    fh.write(newcontent)
                    fh.close()
                print('Modify Success!')
                usermenu()
            if change != confirm:
                print('Invalid Input')
                personal_modify()
        if ans != i:
            print('Invalid Input')
            usermenu()


def booking():
    loadavailable()
    checkcarplate = loadcar_plate()
    input1=input('\n\nEnter the car plate number you want to rent: ')
    i = 0
    while i < len(checkcarplate):
        if input1 in checkcarplate:
            count_position = checkcarplate.index(input1)
            allcar = loadallcar()
            original = allcar[count_position]
            print('1. Car Plate: ',original[0])
            print('2. Car Model: ',original[1])
            print('3. Car Brand: ',original[2])
            print('4. Car Seat: ',original[3])
            print('5. Price per Day: ',original[4])
            input2=input('Do you want to proceed to payment Y/N : ')
            count_position2 =str(count_position)
            if input2 == 'Y':  
                with open('temfiletowritecount.txt','w')as fh:
                    fh.write(count_position2)
                    fh.close()
                payment()            
            else:
                input3=input('Enter 1 to Book again or Enter 2 to Exit')
                if input3 == '1':
                    booking()
                else:
                    exit()

    if (input1 != i):
        print('Car plate not exist!')
        booking()  


def payment():
    listinlist = loadallcar()
    from datetime import date
    getdate=input('Enter the date you want to book (DD/MM/YYYY): ')
    getdate2=getdate.split('/')
    getdate3=date(int(getdate2[2]),int(getdate2[1]),int(getdate2[0]))

    currentdate = date.today()
    currentdate2 = currentdate.strftime('%d/%m/%Y')
    currentdate3 = currentdate2.split('/')
    currentdate4 = date(int(currentdate3[2]),int(currentdate3[1]),int(currentdate3[0]))

    if getdate3 >= currentdate4:
        returndate=input('Enter the date you want to return (DD/MM/YYYY): ')
        returndate2=returndate.split('/')
        returndate3=date(int(returndate2[2]),int(returndate2[1]),int(returndate2[0]))

        if returndate3 >= getdate3:
            countgap = returndate3 - getdate3
            onlyday = countgap.days
            with open('temfiletowritecount.txt', 'r')as fh:
                count = fh.readline()
            count1=int(count)
            list = []
            price = loadcar_price()
            list.append(price[count1])
            total = onlyday * int(list[0])
            print('The Total will be: ',total)
            creditcard=input('Pleasee Enter your credit card number: ')
            n = len(creditcard)
            if n == 16:
                cvv=input('Please Enter your CVV: ')
                n2 = len(cvv)
                if n2 == 3:
                    customerid = input('Please Input your CustomerID: ')
                    id = loaduser_id()
                    for i in id:
                        if i == customerid:
                            change = listinlist[count1]
                            index = 1
            if n != 16:
                print('Input Invalid')
                payment()
                if n2 != 3:
                    print('Input Invalid')
                    payment()
                    if i != customerid:
                        print('Invalid Input')
                        payment()


            if(index ==1):
                cusid = customerid
                add1 = currentdate2
                add2 = getdate
                add3 = returndate
                card = creditcard
                cvv2 = cvv
                change.append(cusid)
                change.append(add1)
                change.append(add2)
                change.append(add3)
                change.append(str(total))
                change.append(card)
                change.append(cvv2)

                with open('car.txt', 'w') as fh:
                    cnt = 0
                    newcontent = ""
                    while (cnt < len(listinlist)):
                        recstr = ":".join(listinlist[cnt])
                        newcontent += recstr + "\n"
                        cnt += 1
                    fh.write(newcontent)
                    fh.close()
                file1 = open('bookingrecord.txt','a')
                for i in change:
                    liststr=':'.join(change)
                    newliststr=(liststr+'\n')
                file1.write(newliststr)
                file1.close()
                print('Payment Accepted')
                usermenu()

            else:
                print('Input Invalid')
                payment()
        else:
            print('Input Invalid')
            payment()
    else:
        print('Input Invalid')
        payment()

def cusrental_history():
    ans= input("Please Enter your Customer ID: ")
    alldata=booked()
    print('[Car Plate, Car Model, Car Brand, Seat, Price, YourID, Payment Date, Order Date, Return Date, Total Price]')
    for count in range(len(alldata)):
        if(alldata[count][5]== ans):
            print(alldata[count])
    ans = input('Do you want to go back to menu? Type Y to go back to mainmenu : ')
    if ans == 'Y':
        usermenu()
    else:
        cusrental_history()



def returncar():
    ans = input('Enter car plate number: ')
    allcar = loadallcar()
    count_position = -1
    for count in range(len(allcar)):
        if (allcar[count][0] == ans):
            count_position = count
            allcar[count_position].pop(5)
            allcar[count_position].pop(5)
            allcar[count_position].pop(5)
            allcar[count_position].pop(5)
            allcar[count_position].pop(5)
            allcar[count_position].pop(5)
            allcar[count_position].pop(5)
    if count_position == -1:
        print('Car Does Not Exist!')
        returncar()
    if count_position != -1:
        with open('car.txt', 'w') as fh:
            cnt = 0
            newcontent = ""
            while (cnt < len(allcar)):
                recstr = ":".join(allcar[cnt])
                newcontent += recstr + "\n"
                cnt += 1
            fh.write(newcontent)
            fh.close()
        print('Car have return')
        usermenu()

##################################################################

def loaduser_id():
    list1 =[]
    with open('account.txt', 'r') as fh:
        for line in fh:
            strip0 = line.strip('\n')
            strip1 = strip0.split(':')
            list1.append(strip1[0])
    return list1

def loaduser_password():
    list1 =[]
    with open('account.txt','r') as fh:
        for line in fh:
            strip0 = line.strip('\n')
            strip1 = strip0.split(':')
            list1.append(strip1[1])
    return list1

def load_adminid():
    list1 = []
    with open('adminaccount.txt')as fh:
        for line in fh:
            strip0 = line.strip('\n')
            strip1 = strip0.split(':')
            list1.append(strip1[0])
        return list1

def load_adminpassword():
    list1 = []
    with open('adminaccount.txt')as fh:
        for line in fh:
            strip0 = line.strip('\n')
            strip1 = strip0.split(':')
            list1.append(strip1[1])
        return list1

#####################################################################

def loadpersonal_ic():
    list1 =[]
    with open('personaldata.txt')as fh:
        for line in fh:
            strip0 = line.strip('\n')
            strip1 = strip0.split(':')
            list1.append(strip1[0])
        return list1

def loadpersonal_email():
    list1 =[]
    with open('personaldata.txt')as fh:
        for line in fh:
            strip0 = line.strip('\n')
            strip1 = strip0.split(':')
            list1.append(strip1[1])    
    return list1

def loadpersonal_phone():
    list1 =[]
    with open('personaldata.txt')as fh:
        for line in fh:
            strip0 = line.strip('\n')
            strip1 = strip0.split(':')
            list1.append(strip1[2])
    return list1

def loadall_personal():
    list1 =[]
    with open("personaldata.txt") as fh:
        for line in fh:
            strip0 = line.strip('\n')
            strip1 = strip0.split(':')
            list1.append(strip1)
    return list1

#####################################################################

def loadallcar():
    list1 =[]
    car =open("car.txt","r")
    for line in car:
        strip0 = line.strip('\n')
        strip1 = strip0.split(':')
        list1.append(strip1)
    return list1

def loadcar_plate():
    list1 =[]
    car =open("car.txt","r")
    for line in car:
        strip1 = line.split(':')
        list1.append(strip1[0])
    return list1

def loadcar_model():
    list1 =[]
    car =open("car.txt","r")
    for line in car:
        strip1 = line.split(':')
        list1.append(strip1[1])
    return list1

def loadcar_brand():
    list1 =[]
    car =open("car.txt","r")
    for line in car:
        strip1 = line.split(':')
        list1.append(strip1[2])
    return list1
def loadcar_seat():
    list1 =[]
    car =open("car.txt","r")
    for line in car:
        strip1 = line.split(':')
        list1.append(strip1[3])
    return list1


def loadcar_price():
    list1 =[]
    car =open("car.txt","r")
    for line in car:
        strip0 = line.strip('\n')
        strip1 = strip0.split(':')
        list1.append(strip1[4])
    return list1


def loadavailable():
    available_list = []
    allcar = loadallcar()
    for item in allcar:
        if len(item) == 5:
            available_list.append(item)
    print('Car Available\n')       
    for item in available_list:
        print(item)
    return item

def loadunavailable():
    unavailable_list = []
    allcar = loadallcar()
    for item in allcar:
        if len(item) > 5:
            unavailable_list.append(item)
    print('\nCar Rented Out with Customer Booking Information\n')
    for item in unavailable_list:
        print(item)
    return item

def booked():
    list1 =[]
    car =open("bookingrecord.txt","r")
    for line in car:
        strip0 = line.strip('\n')
        strip1 = strip0.split(':')
        list1.append(strip1)
    return list1

def booked_cusid():
    list1 = []
    acc = open("bookingrecord.txt", "r")
    for line in acc:
        strip1 = line.split(':')
        list1.append(strip1[5])
    return list1

def showbooking():
    booking = open('bookingrecord.txt','r')
    for line in booking:
        strip0 = line.strip('\n')
        strip = strip0.split(':')
    return strip
##########################################################





#booked()
#loadavailable()
#booking()
#payment()
#loadcar_price()
#loadallcar()
#modify_car()
#search_cus_booking()
#booked_cusid()
#loaduser_name()
#adminmenu()
#showbooking()
#cusrental_history()
#returncar()
#adminmenu()
#modify_car()
#loadall_personal()
#personal_modify()
mainmenu()
#loaduser_password()
#loaduser_name()
#cusrental_history()
#personal_details()
#register()
