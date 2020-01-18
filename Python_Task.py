import pymongo
import re
import datetime


welcome = print("welcome to Company Management System")
operations = print("hello....\n"
                   "please select the option form the below choice\n"
                   "1. Add Employeee\n"
                   "2. Delete Employee\n"
                   "3. Edit Employee Details\n"
                   "4. Display all Employee Details\n"
                   "5. Salary Management\n"
                   "6. Attendance Management\n"
                   "7. Annual Functions Management\n"
                   "8. Holiday Management")

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CompanyManagementSystem"]
mycol = mydb["Employee"]
myan = mydb["Annual"]

def Add_Employee():
    def sequence():
        seq = 1
        for i in mycol.find():
            seq += 1
        return seq

    def name_validation():
        while True:
          name = input("enter employee name:")
          if name.isalpha():
             break
          print("invalid name")
        return name

    def validate_status():
         while True:
           Status = input("enter the status:")
           if (Status=="Fresher" or Status=="fresher") or (Status=="Experience" or Status=="experience"):
              break
           print("it is not valid....please enter status fresher or experience")
         return Status
    def validate_mobilenum():
        while True:
          a = input("enter the mobile number:")
          if len(a) == 10:
            break
          print("it's not valid....enter the 10-digit mobile number:")
        return a
    def validate():
         while True:
             date = input("enter the date of birthday:")
             if re.search("^([1-9] |1[0-9]| 2[0-9]|3[0-1])(.|-)([1-9] |1[0-2])(.|-|)20[0-9][0-9]$",date):
                break
             print("It's not valid.. enter the YYYY-MM-DD format:")
         return date
    def email_vlidation():
        while True:
          email = input("enter an email address:")
          if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",email):
           break
          print("is not valid..please enter correct email:")
        return email

    user_dict={"id":sequence(),"name":name_validation(),"Address": input("enter the Address:") ,
               "Status":validate_status(),"DOB":validate(),"Email":email_vlidation(),
                "Mobile No": validate_mobilenum()}
    x = mycol.insert_one(user_dict)
    print(list(user_dict.items()))

def Delete_employee():
    list = []
    for x in mycol.find({}, {"id": 1}):
        # print(x["id"])
        list.append(x["id"])
    # print(list)

    remove = {"id": int(input("enter the employee id who you want to delete:"))}
    dis = remove['id']

    if dis in list:
        mycol.delete_one(remove)
        Display()
    else:
        print("this id is not found")
        print("please enter valid employee id")


def Edit_details():
   print(
      "please select the option form the below what u want to edit:\n"
      "1. Employee name\n"
      "2. Employee address\n"
      "3. Employee status\n"
      "4. Employee DOB\n"
      "5. Employee email\n"
      "6. Employee mobile no\n")

   while True:
       op = int(input("enter the number of choice you want to change:"))
       if op == 1:
           list = []
           for x in mycol.find({}, {"id": 1}):
               # print(x["id"])
               list.append(x["id"])
           # print(list)

           remove = {"id": int(input("enter the employee id who you want to edit:"))}
           dis = remove['id']

           if dis in list:
               nam = mycol.update_one({"id": dis}, {"$set": {"name": input("enter the name:")}})
               print("successfully update name")
           else:
               print("this id is not found")
               print("please enter valid employee id")
       elif op == 2:
           list = []
           for x in mycol.find({}, {"id": 1}):
               # print(x["id"])
               list.append(x["id"])
           # print(list)

           remove = {"id": int(input("enter the employee id who you want to edit:"))}
           dis = remove['id']
           if dis in list:
              adr = mycol.update_one({"id": dis},{"$set": {"Address": input("enter the address:")}})
              print("successfully update address")
           else:
              print("this id is not found")
              print("please enter valid employee id")

       elif op == 3:
           list = []
           for x in mycol.find({}, {"id": 1}):
               # print(x["id"])
               list.append(x["id"])
           # print(list)

           remove = {"id": int(input("enter the employee id who you want to edit:"))}
           dis = remove['id']
           if dis in list:
               mycol.update_one({"id":dis},{"$set":{"Status": input("enter the status:")}})
               print("Status successfully updated")
           else:
               print("this id is not found")
               print("please enter valid employee id")

       elif op == 4:
           list = []
           for x in mycol.find({}, {"id": 1}):
               # print(x["id"])
               list.append(x["id"])
           # print(list)

           remove = {"id": int(input("enter the employee id who you want to edit:"))}
           dis = remove['id']
           if dis in list:
               mycol.update_one({"id":dis},{"$set":{"DOB": input("enter the DOB:")}})
               print("DOB successfully updated")
           else:
               print("this id is not found")
               print("please enter valid employee id")

       elif op == 5:
           list = []
           for x in mycol.find({}, {"id": 1}):
               # print(x["id"])
               list.append(x["id"])
           # print(list)

           remove = {"id": int(input("enter the employee id who you want to edit:"))}
           dis = remove['id']
           if dis in list:
             em = mycol.update_one({"id":dis},{"$set": {"Email": input("enter the email:")}})
             print("email address sucessfully update")
           else:
               print("this id is not found")
               print("please enter valid employee id")

       elif op == 6:
           list = []
           for x in mycol.find({}, {"id": 1}):
               # print(x["id"])
               list.append(x["id"])
           # print(list)

           remove = {"id": int(input("enter the employee id who you want to edit:"))}
           dis = remove['id']
           if dis in list:
              mb = mycol.update_one({"id":dis},{"$set": {"Mobile No": input("enter the mobile no:")}})
              print("mobile number succesfully updated")
           else:
               print("this id is not found")
               print("please enter valid employee id")
       else:
           print("enter valid number..")


       if input('Do You Want To Continue with to edit employee details? ') != 'y':
         break
       else:
           print(
               "please select the option form the below what u want to edit:\n"
               "1. Employee name\n"
               "2. Employee address\n"
               "3. Employee status\n"
               "4. Employee DOB\n"
               "5. Employee email\n"
               "6. Employee mobile no\n")

def Display():
    seq = 0
    for i in mycol.find():
        seq += 1
    if (seq == 0):
        print("No DATA......")
    else:
       for i in mycol.find({},{ "_id": 0}):
          print(i)


def Add_Function():
  while True:
    def sequence():
        seq = 1
        for i in myan.find():
            seq += 1
        return seq

    def amount():
       amt = 0
       return amt

    def date_fun():
        date_entry = input('Enter a date in YYYY-MM-DD format:')
        year, month, day = map(int, date_entry.split('-'))
        date1= datetime.datetime(year, month, day)
        return date1

    function = {"id": sequence(), "Title": input("enter the Function name:"), "Date": date_fun(),
                "Budget": int(input("enter the budget for function:")), "Amount":print("right now your amount for function is:",amount()) }

    x = myan.insert_one(function)
    if input('Do You Want To Continue to add function details? ') != 'y':
        break



while True:
 choice = int(input("enter the number of choise you want:"))

 if choice == 1:
    print("Add Employeee")
    Add_Employee()
 elif choice == 2:
    # print("Delete Employee")
    Delete_employee()
 elif choice == 3:
    print("Edit Employee Details")
    Edit_details()
 elif choice == 4:
    # print("Display all Employee Details")
    Display()
 elif choice == 5:
    print("Salary Management")
 elif choice == 6:
    print("Attendance Management")
 elif choice == 7:
     print("Annual Functions Management")
     Add_Function()
 elif choice == 8:
     print("Holiday Management")
 else:
    print("enter valid number:")

 if input('Do You Want To Continue with employee? ') != 'y':
     break
 else:
     print("please select the option form the below choice\n"
           "1. Add Employeee\n"
           "2. Delete Employee\n"
           "3. Edit Employee Details\n"
           "4. Display all Employee Details\n"
           "5. Salary Management\n"
           "6. Attendance Management\n"
           "7. Annual Functions Management\n"
           "8. Holiday Management")





