################################################  Vaccination System  ####################################################
################################## Projected Created And Developed By Jebin Santhosh ###################################



###### Importing Required Modules To Run The Program ######

import random
import sys as s #for s.exit
import time as t
import pickle #for pickle.load(),pickle.dump()
import os     #for os.remove
import con_num_to_words
import mysql.connector



############# Welcome Details ##############
'''choice = int(input("Enter "))
if choice == 1:
    print("djkhdkh")
if choice == 2:
    print("jebin")
if choice == 4:
    print("bad")
if choice == 5:
    print("Bye")'''


#########################   Login Screen #########################

dict={}

def write_data():

  file=open("logindetails.dat","ab") #a-append b-binary
  n=int(input("Welcome To Vaccination Booking\nEnter 1 To Signup & 2 To Close The Page :"))
  if n == 1:

    print("Enter Your Details For Creating An Account")
    dict["MOBILE NUMBER"]=int(input("Enter Your Mobile Number : "))
    dict["NAME"]=(input("Enter Account Name : "))
    dict["PASSWORD"]=int(input("Enter Password (Enter Only Numbers) : "))
    dict["ACCOUNT TYPE"]=(input("Enter Your Account Usage Type (Personal Or Famliy) : "))
    pickle.dump(dict,file) #dump is udes to write in a file
  file.close()
  if n == 2:

      print("Thanks For Visting !!\n😷 Wear Mask 😷 !! Stay Safe 😀 ")
      s.exit()


def display():
  file=open("logindetails.dat","rb") #r-read b-binary

  try:
    while True:

      vac=pickle.load(file) #load is used to read
      print(vac)

  except EOFError:
    pass
  file.close()


def search():
    file=open("logindetails.dat","rb") #r-read b-binary
    a=int(input("Enter Your PhoneNumber To Search Your Account🔍 : "))
    found=0
    try:
      while True:

        vac=pickle.load(file) #load is used to read

        if vac["MOBILE NUMBER"]==a:

            found=1
            print("!! 🔎 Hurray !! Account Found 🔍 !!")
            print(vac)
            break

    except EOFError:
      pass

    if found==0:
      print("!! Oops 🙄 !! Account Not Found 😭\nTry Again Or If You Don't Have An Account Create It !!")
    file.close() 


def update():
    file=open("logindetails.dat","rb") #r-read b-binary
    f=open("temp.dat","ab")
    a=int(input("Enter Your Registered Phone Number To Be Update Your Account📲 : "))
    found=0
    try:

      while True:
        vac=pickle.load(file) #load is used to read

        if vac["MOBILE NUMBER"]==a:
          found=1
          print("!! Enter New Account Details !!")

          dict["MOBILE NUMBER"]=int(input("Enter Your New Mobile Number : "))
          dict["NAME"]=input("Enter Your New Account Name : ")
          dict["PASSWORD"]=int(input("Enter Your New Password : "))
          dict["ACCOUNT TYPE"]=input("ENTER New Account Type (Personal Or Famliy) : ")
          pickle.dump(dict,f) #dump is udes to write in a file

        else:
          pickle.dump(dict,f)

    except EOFError:
      pass

    file.close()
    f.close()
    os.remove("logindetails.dat")
    os.rename("temp.dat","logindetails.dat")
    file=open("logindetails.dat","rb") #r-read b-binary

    try:

      while True:
        vac=pickle.load(file) #load is used to read
        print(vac)
    except EOFError:
      pass
    file.close()


def delete():
    file=open("logindetails.dat","rb") #r-read b-binary
    f=open("temp.dat","ab")
    a=int(input("Enter Your Registered Mobile Number To Delete Your Account📝 : "))
    found=0
    try:

      while True:
        vac=pickle.load(file) #load is used to read

        if vac["MOBILE NUMBER"]==a:
          found=1
          pass

        else:
          pickle.dump(dict,f)

    except EOFError:
      pass
    file.close()
    f.close()
    os.remove("logindetails.dat")
    os.rename("temp.dat","logindetails.dat")
    file=open("logindetails.dat","rb") #r-read b-binary

    try:
      while True:
        vac=pickle.load(file) #load is used to read
        print(vac)

    except EOFError:
      pass
    file.close()
    if found==0:
      print("!! Oops 🙄 !! Account Not Deleted !!\nTry Again")    


################################## Main Program For Login/Signup Screen ##################################


while True:
  print("😀Account Menu😀 \n1 : New User 😊 ?? Signup Now 📌 \n2 : Display Your Account Details 📋 \n3 : Search Your Account 🔍 \n4 : Update Your Account 📲 \n5 : Delete Your Account 😨 \n6 : Proceed To Vaccination Booking Slot Page 📃")

  ch=int(input("Enter Your Choice :"))

  if ch==1:
    write_data()

  if ch==2:
    display()

  if ch==3:
    search()

  if ch==4:
    update()

  if ch==5:
    delete()
    
  if ch==6:
    print("Proceeding To Next Page 📃 \nLoaded Vaccination Booking Page 📄 \nSuccess 💿 ")
    break



###### Starting The Program ######

userphoneno = int(input("😷 Welcome To Covid-19 Vaccine Booking 😷 \n!! 💪🏻 Stay Healthy 👦🏻 Stay Safe !!\nEnter Your Registered Phone Number To Get An OTP : "))

while len(str(userphoneno)) != 10:
    
    print("❌ OMG !! You Have Entered a Wrong Number ❌ !!\nTry Again By Entering A Valid 10-Digit Phone Number 📱")
    
    userphoneno = int(input("Enter Your Registered Phone Number To Get An OTP : "))
    
    if len(str(userphoneno)) == 10:
        break
    
print("🔃Processing OTP...")
print("!!! 🔃Verifying OTP", end='')

for i in range(3):
    print(".", end='')
    t.sleep(2)
    
print("📤 Proceeding To Send OTP")
print("📩 OTP Sending To Your Phone Number")

print ("📱 A SMS With a 6-Digit Verification Code Was Just Sent To +91 \nDon't Share Your OTP With Anyone 🚫", userphoneno)


############### Using Random Module To Generate The OTP ###############


while True:
    
    otp = random.randint(100000, 999999)
    print("OTP is", otp)
    userOTP = int(input("Enter The 6-Digit OTP Number : "))

    
    if otp == userOTP:
        
        print("🔃 Processing OTP", end='')
        
        for i in range(3):
            
            print(".", end='')
            t.sleep(2)

        print("🔍 Verifying OTP", end='')
        
        for i in range(3):
            
            print(".", end='')
            t.sleep(2)

        print("❗Success ❕", end='')
        
        for i in range(3):
            
            print(".", end='')
            t.sleep(2)
    
        print("OTP Verified ✅")
        print("🔃 Proceeding To Next Process", end = '')
        
        for i in range(3):
            
            print(".", end='')
            t.sleep(2)
            
        print("\n😀 Welcome To Vaccination Booking Page 😀")
        print("NOTE: You Can Only Register 4 Members With One Mobile Number")
        
        break
    
    else:
        print("❌ Oops !! Wrong OTP ❌ \nTry Again")
        
        continue


############### Choosing Options ###############

    
registerno = int(input("Enter '1' To Proceed To Next Page 📄 \nEnter '2' To Close The Page 📃 \nEnter Your Choice 📍 : "))

if registerno == 1:
    
    print("🔃 Procceding To Next Page")
    
elif registerno == 2:
    
    print("🙏🏻 Thanks For Visting !! 💉 Please Take Your Vaccinate Soon To Fight Against Covid-19 💉 !!")
    s.exit()

else:
    pass



##################### Details Collecting Screen For Registering Vaccination #####################

n=int(input('💉 Enter The Number Of Persons To Take Up The Vaccination 💉 : '))

if n > 4:
    
    print("😥 Sorry !! You Can Only Register 4 Members With One Mobile Number 📱")
    
else:
    
    while True:
        
        for i in range(n):
            
            print('Enter The Details Of The Vaccine Taker ',i+1,":")
            
            Aadhar_Number = int(input('Enter The Aadhar Number : '))
            
            if len(str(Aadhar_Number)) > 12 or len(str(Aadhar_Number)) < 12:
                
                print("!! Oops !! Wrong Aadhar Number ❌")
                
                continue
            
            Name = input('Enter The Name : ')
            
            Age = int(input('Enter Age : '))
            if Age < 15 or Age > 60:
                
                print("Sorry !! You Are Not Eligible To Up The Vaccination 💉")
                
                s.exit() 

            Gender = input("Enter Gender Male/Female : ")

            Email = input("Enter Email Address : ")
            
            Blood_Group = input("Enter Blood Group : ")

            while True:
                
                Dose_Number = int(input("Enter The Dose number : "))
                
                if Dose_Number < 1 or Dose_Number > 3:
                    
                    print("Oops !! Entered Wrong Choice ❌ Please Enter A Valid Choice")
                    
                    continue
                
                else:
                    break
                
            Vaacine_Name = ''
            
            while True:
                
                print("1. Covaxin 💉")
                print("2. Covishield 💉")
                print("3. Sputnik 💉")
                Vaccine_Type = int(input("Enter Your Vaccine Choice 💉 : "))
                
                if Vaccine_Type == 1:
                    
                    Vaacine_Name = "Covaxin"
                    break
                
                elif Vaccine_Type == 2:
                    
                    Vaacine_Name = "Covishield"
                    break
                
                elif Vaccine_Type == 3:
                    
                    Vaacine_Name = "Sputnik"
                    break
                
                else:
                    
                    print("Oops !! Entered Wrong Choice ❌ Please Enter A Valid Choice")
                    break
            
            District_Name = ''
            district = {"Ariyalur":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Chengalpattu":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Chennai":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Coimbatore":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Cuddalore":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Dharmapuri":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Dindigul":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Erode":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Kallakurichi":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Kanchipuram":{'Government' : ["ABC"], #10
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Kanyakumari":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Karur":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Krishnagiri":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Madurai":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Nagapattinam":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Namakkal":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Nilgiris":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Perambalur":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Pudukkottai":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Ramanathapuram":{'Government' : ["ABC"], #20
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Ranipet":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Salem":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Sivagangai":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Tenkasi":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Thanjavur":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Theni":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Thoothukudi":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Tiruchirappalli":{'Government' : ["ABC"],
                                    'Private' : ["ABC"],
                                    'Camp' : ["ABC"]},
                        "Tirunelveli":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Tirupathur":{'Government' : ["ABC", "DEF"], #30
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Tiruppur":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Tiruvallur":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Tiruvannamalai":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Tiruvarur":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Vellore":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Viluppuram":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]},
                        "Virudhunagar":{'Government' : ["ABC", "DEF"],
                                    'Private' : ["ABC", "DEF"],
                                    'Camp' : ["ABC", "DEF"]}}
            while True:
                print("1. Ariyalur")
                print("2. Chengalpattu")
                print("3. Chennai")
                print("4. Coimbatore")
                print("5. Cuddalore")
                print("6. Dharmapuri")
                print("7. Dindigul")
                print("8. Erode")
                print("9. Kallakurichi")
                print("10. Kanchipuram")
                print("11. Kanyakumari")
                print("12. Karur")
                print("13. Krishnagiri")
                print("14. Madurai")
                print("15. Nagapattinam")
                print("16. Namakkal")
                print("17. Nilgiris")
                print("18. Perambalur")
                print("19. Pudukkottai")
                print("20. Ramanathapuram")
                print("21. Ranipet")
                print("22. Salem")
                print("23. Sivagangai")
                print("24. Tenkasi")
                print("25. Thanjavur")
                print("26. Theni")
                print("27. Thoothukudi")
                print("28. Tiruchirappalli")
                print("29. Tirunelveli")
                print("30. Tirupathur")
                print("31. Tiruppur")
                print("32. Tiruvallur")
                print("33. Tiruvannamalai")
                print("34. Tiruvarur")
                print("35. Vellore")
                print("36. Viluppuram")
                print("37. Virudhunagar")

                District = int(input('Enter Your Distict \nNOTE: Enter The District Where You Gonna Take The Vaccination 💉 : '))
                
                if District == 1:
                    
                    District_Name = "Ariyalur"
                    break
                
                elif District == 2:
                    
                    District_Name = "Chengalpattu"
                    break
                
                elif District == 3:
                    
                    District_Name = "Chennai"
                    break
                
                elif District == 4:
                    
                    District_Name = "Coimbatore"
                    break
                
                elif District == 5:
                    
                    District_Name = "Cuddalore"
                    break
                
                elif District == 6:
                    
                    District_Name = "Dharmapuri"
                    break
                
                elif District == 7:
                    
                    District_Name = "Dindigul"
                    break

                elif District == 8:
                    
                    District_Name = "Erode"
                    break
                
                elif District == 9:
                    
                    District_Name = "Kallakurichi"
                    break

                elif District == 10:
                    
                    District_Name = "Kanchipuram"
                    break
                
                elif District == 11:
                    
                    District_Name = "Kanyakumari"
                    break

                elif District == 12:
                    
                    District_Name = "Karur"
                    break
                
                elif District == 13:
                    
                    District_Name = "Krishnagiri"
                    break

                elif District == 14:
                    
                    District_Name = "Madurai"
                    break
                
                elif District == 15:
                    
                    District_Name = "Nagapattinam"
                    break        

                elif District == 16:
                    
                    District_Name = "Namakkal"
                    break
                
                elif District == 17:
                    
                    District_Name = "Nilgiris"
                    break

                elif District == 18:
                    
                    District_Name = "Perambalur"
                    break
                
                elif District == 19:
                    
                    District_Name = "Pudukkottai"
                    break

                elif District == 20:
                    
                    District_Name = "Ramanathapuram"
                    break

                elif District == 21:
                    
                    District_Name = "Ranipet"
                    break
                
                elif District == 22:
                    
                    District_Name = "Salem"
                    break
                
                elif District == 23:
                    
                    District_Name = "Sivagangai"
                    break
                
                elif District == 24:
                    
                    District_Name = "Tenkasi"
                    break
                
                elif District == 25:
                    
                    District_Name = "Thanjavur"
                    break
                
                elif District == 26:
                    
                    District_Name = "Theni"
                    break
                
                elif District == 27:
                    
                    District_Name = "Thoothukudi"
                    break

                elif District == 28:
                    
                    District_Name = "Tiruchirappalli"
                    break
                
                elif District == 29:
                    
                    District_Name = "Tirunelveli"
                    break

                elif District == 30:
                    
                    District_Name = "Tirupathur"
                    break

                elif District == 31:
                    
                    District_Name = "Tiruppur"
                    break
                
                elif District == 32:
                    
                    District_Name = "Tiruvallur"
                    break
                
                elif District == 33:
                    
                    District_Name = "Tiruvannamalai"
                    break
                
                elif District == 34:
                    
                    District_Name = "Tiruvarur"
                    break
                
                elif District == 35:
                    
                    District_Name = "Vellore"
                    break
                
                elif District == 36:
                    
                    District_Name = "Viluppuram"
                    break
                
                elif District == 37:
                    
                    District_Name = "Virudhunagar"
                    break

                else:
                    
                    print("Oops !! Entered Wrong Choice ❌ Please Enter A Valid Choice")
                    break            
            Centre_Name = ''
            while True:
                print("1. "+District_Name+" Governmnet Hospital")
                print("2. "+District_Name+" Private Hospital")
                print("3. "+District_Name+" Camp")

                Center = int(input("Enter Your Centre Number Choice : "))

                if Center == 1:

                    Center_Name = "Governmnet Hospital"
                    Hospital_Name = district[District_Name]["Government"]
                    count = 1
                    a = []
                    for i in Hospital_Name:
                        a.append([str(count),i])
                        print(count,i)
                        count+=1
                    Hospital_Name =''    
                    Hospital_Name_input = int(input("Enter Your District Government Hospital Choice : "))
                    for i in a:
                        if Hospital_Name_input==int(i[0])-1:
                            Hospital_Name+i[1]
                        break  
                    break

                elif Center == 2:

                    Center_Name = "Private Hospital"
                    Hospital_Name = district[District_Name]["Private"]
                    count = 1
                    a = []
                    for i in Hospital_Name:
                        a.append([str(count),i])
                        print(count,i)
                        count+=1
                    Hospital_Name =''    
                    Hospital_Name_input = int(input("Enter Your Private Hospital Choice : "))
                    for i in a:
                        if Hospital_Name_input==int(i[0])-1:
                            Hospital_Name+i[1]
                        break
                    break
                
            
                elif Center == 3:

                    Center_Name = "Camp"
                    Hospital_Name = district[District_Name]["Camp"]
                    count = 1
                    a = []
                    for i in Hospital_Name:
                        a.append([str(count),i])
                        print(count,i)
                        count+=1
                    Hospital_Name =''
                    Hospital_Name_input = int(input("Enter Your Camp Choice : "))
                    for i in a:
                        if Hospital_Name_input==int(i[0])-1:
                            Hospital_Name+i[1]
                        break
                    break
            
            print("!! 😁 WOW 😁 !! 😁You Are Registered Against The Covid-19 💉")
            
            booking_number = random.randint(100000000, 999999999)
            
            word = con_num_to_words.convertToWords(booking_number)
            
            print("Your Vaacination Booking  Number Is ", booking_number)
            
            print("Booking Number In Words",word)

            print("🙏🏻 Thanks For Registering With Us \nSoon You Will Get Touched Up With The Further Information 📄")
            print("Thank You 🙏🏻 !! Goodbye 👋🏻 !! Stay Safe 😷")

################################# My-SQL Connector For Details Registering #################################

            connection = mysql.connector.connect(host = "localhost", user = "root", passwd = "mysql", database ="vaccination")
            cursor = connection.cursor()
            
            cursor.execute("insert into details values ({}, '{}', {}, '{}', '{}', '{}', '{}', '{}','{}','{}')".format(Aadhar_Number, Name, Age,Gender, Email, Blood_Group, Vaacine_Name, Dose_Number, District_Name,Center_Name))

            connection.commit()

            connection.close()
        break 
