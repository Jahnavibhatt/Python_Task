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
myhl =mydb["Holiday"]
mya = mydb["Attendence"]
mysalary = mydb["Salary"]


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
        if (Status == "Fresher" or Status == "fresher") or (Status == "Experience" or Status == "experience"):
            break
        print("it is not valid....please enter status fresher or experience")
    return Status


def validate_mobilenum():
    while True:
        a = input("enter the mobile number:")
        if len(a) == 10 and a.isdigit():
            break
        print("it's not valid....enter the 10-digit mobile number:")
    return a


def validate():
    while True:
        date_entry = input("enter the date in YYYY-MM-DD format:")
        if re.search("^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$", date_entry):
            year, month, day = map(int, date_entry.split('-'))
            date1 = datetime.datetime(year, month, day)
            return date1
            break
        else:
            print("It's not valid.. enter the YYYY-MM-DD format:")


def email_vlidation():
    while True:
        email = input("enter an email address:")
        if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]+$", email):
            break
        print("is not valid..please enter correct email:")
    return email


def Add_Employee():
    def sequence():
        seq = 1
        for i in mycol.find():
            seq += 1
        return seq


    user_dict={"id":sequence(),"name":name_validation(),"Address": input("enter the Address:") ,
               "Status":validate_status(),"DOB":validate(),"Email":email_vlidation(),
                "Mobile No": validate_mobilenum()}
    x = mycol.insert_one(user_dict)
    print(list(user_dict.items()))

def Delete_employee():
    list = []
    for x in mycol.find({}, {"id": 1}):
        list.append(x["id"])

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
               list.append(x["id"])
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
               list.append(x["id"])
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
               list.append(x["id"])
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
               list.append(x["id"])
           remove = {"id": int(input("enter the employee id who you want to edit:"))}
           dis = remove['id']
           if dis in list:
               mycol.update_one({"id":dis},{"$set":{"DOB":validate()}})
               print("DOB successfully updated")
           else:
               print("this id is not found")
               print("please enter valid employee id")
       elif op == 5:
           list = []
           for x in mycol.find({}, {"id": 1}):
               list.append(x["id"])
           remove = {"id": int(input("enter the employee id who you want to edit:"))}
           dis = remove['id']
           if dis in list:
             em = mycol.update_one({"id":dis},{"$set": {"Email":email_vlidation() }})
             print("email address sucessfully update")
           else:
               print("this id is not found")
               print("please enter valid employee id")
       elif op == 6:
           list = []
           for x in mycol.find({}, {"id": 1}):
               list.append(x["id"])
           remove = {"id": int(input("enter the employee id who you want to edit:"))}
           dis = remove['id']
           if dis in list:
              mb = mycol.update_one({"id":dis},{"$set": {"Mobile No":validate_mobilenum()}})
              print("mobile number succesfully updated")
           else:
               print("this id is not found")
               print("please enter valid employee id")
       else:
           print("enter valid number..")
       ch1 = input("do you want to continue with edit employee deatils ?")
       if ch1 == 'y':
           print("please select the option form the below choice\n"
                 "1. Employee name\n"
                 "2. Employee address\n"
                 "3. Employee status\n"
                 "4. Employee DOB\n"
                 "5. Employee email\n"
                 "6. Employee mobile no\n")

       elif ch1 == 'n':
           break
       else:
           print("please enter valid choice between ('y'/'n')")
           break


def Display():
      seq = 0
      for i in mycol.find():
        seq += 1
      if (seq == 0):
        print("No DATA......")
      else:
       for i in mycol.find():
          print("Employee Name     :",i["name"])
          print("Employee_Address  :",i["Address"])
          print("Employee_status   :", i["Status"])
          print("Employee_DOB      :", i["DOB"].strftime("%m/%d/%Y"))
          print("Employee_Email    :", i["Email"])
          print("Employee_Mobile NO:", i["Mobile No"])
          print("-" * 70)
def Annual():

    print(
        "please select the option form the below :\n"
        "1. Add Function Name\n"
        "2. Display the deatils of Function\n"
        "3. Update the functions details\n")

    def Add_Function():
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
            date1 = datetime.datetime(year, month, day)
            return date1
        function = {"id": sequence(), "Title": input("enter the Function name:"), "Date": validate(),
                    "Budget": float(input("enter the budget for function:")),
                    "Amount": print("right now your amount for function is:", amount())}
        x = myan.insert_one(function)
    def Disply_Fun():
        seq = 0
        for i in myan.find():
            seq += 1
        if (seq == 0):
            print("No DATA......")
        else:
            for i in myan.find():
                print("Function_Titile:",i["Title"])
                print("Function_Date:", i["Date"].strftime("%d/%m/%y"))
                print("Function_Budget:", i["Budget"])
                print("Function_Amount:",i["Amount"])
                print("-" * 70)
    def Edit_Function():
         print(
            "please select the option form the below :\n"
            "1. Edit Function name\n"
            "2. Edit Function date\n"
            "3. Edit Function Budget\n"
            "4. Edit Function Amount\n")
         while True:
             op = int(input("enter the number of choice you want to change:"))
             if op == 1:
                 list = []
                 for x in myan.find({}, {"id": 1}):
                     list.append(x["id"])
                 remove = {"id": int(input("enter the function id who you want to edit:"))}
                 dis = remove['id']
                 if dis in list:
                     nam = myan.update_one({"id": dis}, {"$set": {"Title": input("enter the function name:")}})
                     print("successfully update function name")
                 else:
                     print("this id is not found")
                     print("please enter valid function id")
             elif op==2:
                 list = []
                 for x in myan.find({}, {"id": 1}):
                     list.append(x["id"])
                 remove = {"id": int(input("enter the function id who you want to edit:"))}
                 dis = remove['id']
                 if dis in list:
                     nam = myan.update_one({"id": dis}, {"$set": {"Date":validate()}})
                     print("successfully update Date")
                 else:
                     print("this id is not found")
                     print("please enter valid function id")
             elif op == 3:
                 list = []
                 for x in myan.find({}, {"id": 1}):
                     list.append(x["id"])
                 remove = {"id": int(input("enter the function id who you want to edit:"))}
                 dis = remove['id']
                 if dis in list:
                     nam = myan.update_one({"id": dis}, {"$set": {"Budget": input("enter the Budget:")}})
                     print("successfully update Budget")
                 else:
                     print("this id is not found")
                     print("please enter valid function id")
             elif op == 4:
                 list = []
                 for x in myan.find({}, {"id": 1}):
                     list.append(x["id"])
                 remove = {"id": int(input("enter the function id who you want to edit:"))}
                 dis = remove['id']
                 if dis in list:
                     nam = myan.update_one({"id": dis}, {"$set": {"Amount": float(input("enter the Amount:"))}})
                     print("successfully update Amount")
                 else:
                     print("this id is not found")
                     print("please enter valid function id")
                 ch2 = input("do you want to continue with Function system??")
                 if ch2 == 'y':
                     print("please select the option form the below choice\n"
                           "1. Edit Function name\n"
                           "2. Edit Function date\n"
                           "3. Edit Function Budget\n"
                           "4. Edit Function Amount\n")
                 elif ch2 == 'n':
                     break
                 else:
                     print("please enter valid choice between ('y'/'n')")
                     break


    while True:
     choice = int(input("enter the number of choise you want:"))
     if choice == 1:
       Add_Function()
     elif choice == 2:
        Disply_Fun()
     elif choice == 3:
        Edit_Function()
     else:
        print("enter the valid number:")
     op2 = input('Do You Want To Continue with function details? ')
     if op2 == 'y':
         print("please select the option form the below choice\n"
               "1. Add Function Name\n"
               "2. Display the deatils of Function\n"
               "3. Update the functions details\n")

     elif op2 == 'n':
         break
     else:
         print("please enter valid choice between ('y'/'n')")
         break


def Holiday_management():
    print(
        "please select the option form the below :\n"
        "1. Add Holiday\n"
        "2. Display the deatils of Holiday\n"
        "3. Update the Holiday details\n"
        "4. Delete Holiday details\n")
    def Add_Holiday():
        def sequence():
            seq = 1
            for i in myhl.find():
                seq += 1
            return seq

        function = {"id": sequence(), "Holiday_name": input("enter the Holiday name:"), "Date":validate()}
        x = myhl.insert_one(function)
    def Edit_Holiday():
        print(
            "please select the option form the below :\n"
            "1. Edit Holiday name\n"
            "2. Edit Holiday date\n")
        while True:
            op = int(input("enter the number of choice you want to change:"))
            if op == 1:
                list = []
                for x in myhl.find({}, {"id": 1}):
                    list.append(x["id"])
                remove = {"id": int(input("enter the holiday id who you want to edit:"))}
                dis = remove['id']
                if dis in list:
                    nam = myhl.update_one({"id": dis}, {"$set": {"Holiday_name": input("enter the holiday name:")}})
                    print("successfully update holiday name")
                else:
                    print("this id is not found")
                    print("please enter valid holiday id")
            elif op==2:
                list = []
                for x in myhl.find({}, {"id": 1}):
                    list.append(x["id"])
                remove = {"id": int(input("enter the holiday id who you want to edit:"))}
                dis = remove['id']
                if dis in list:
                    nam = myhl.update_one({"id": dis}, {"$set": {"Date": validate()}})
                    print("successfully update holiday name")
                else:
                    print("this id is not found")
                    print("please enter valid holiday id")
                ch4 = input("do you want to continue Edit Holiday system??")
                if ch4 == 'y':
                    print("please select the option form the below choice\n"
                          "1. Edit Holiday name\n"
                          "2. Edit Holiday date\n")
                elif ch4 == 'n':
                    break
                else:
                    print("please enter valid choice between ('y'/'n')")
                    break
    def Display_Holiday():
        seq = 0
        for i in myhl.find():
            seq += 1
        if (seq == 0):
            print("No DATA......")
        else:
            for i in myhl.find():
                print("Holiday_name:",i["Holiday_name"])
                print("Holiday_Date:", i["Date"].strftime("%d/%m/%y"))
                print("-" * 70)

    def Delete_Holiday():
      list = []
      for x in myhl.find({}, {"id": 1}):
        list.append(x["id"])
      remove = {"id": int(input("enter the holiday id who you want to delete:"))}
      dis = remove['id']
      if dis in list:
        myhl.delete_one(remove)
        Display()
      else:
        print("this id is not found")
        print("please enter valid holiday id")

    while True:
     choice = int(input("enter the number of choise you want:"))
     if choice == 1:
       Add_Holiday()
     elif choice == 2:
      Display_Holiday()
     elif choice == 3:
        Edit_Holiday()
     elif choice == 4:
         Delete_Holiday()
     else:
        print("enter the valid number:")
     op1 = input("Do You Want To Continue with Holiday Management?")
     if op1 == 'y':
         print(
             "please select the option form the below :\n"
             "1. Add Holiday\n"
             "2. Display the deatils of Holiday\n"
             "3. Update the Holiday details\n"
             "4. Delete Holiday details\n")
     elif op1 == 'n':
         break
     else:
         print("please enter valid choice between ('y'/'n')")
         break

def Attendence_Management():
    print(
        "please select the option form the below :\n"
        "1. Add Attendence\n"
        "2. Display the employee Attendence\n")

    def Add_attendence():
        def sequence():
            seq = 1
            for i in mya.find():
                seq += 1
            return seq

        function = {"id": sequence(), "Employeeid":int(input("enter the employee id:")),"Date":validate()}
        x = mya.insert_one(function)

    def Display_Attendence():
        seq = 0
        for i in mya.find():
            seq += 1
        if (seq == 0):
            print("No DATA......")
        else:
            for i in mya.find():
                print("Employee_id:", i["Employeeid"])
                print("Employee_date:", i["Date"].strftime("%d/%m/%y"))
                print("-" * 70)

    while True:
     choice = int(input("enter the number of choise you want:"))
     if choice == 1:
       Add_attendence()
     elif choice == 2:
       Display_Attendence()
     else:
        print("enter the valid number:")
     op = input("'Do You Want To Continue with Attendence Management?'")
     if op=='y':
         print(
             "please select the option form the below :\n"
             "1. Add Attendence\n"
             "2. Display the employee Attendence\n")
     elif op == 'n':
         break
     else:
         print("please enter valid choice between ('y'/'n')")
         break

def salary():
    print(
        "please select the option form the below :\n"
        "1. calculate Employee salary\n"
        "2. Display the employee salary details")

    def Add_Salary():
      def sequence():
         seq = 1
         for i in mysalary.find():
          seq += 1
         return seq
      def cal_salary():
         list = []
         for x in mysalary.find({}, {"Employeeid": 1}):
             list.append(x["Employeeid"])
         id = int(input("enter the employee id who's salary u want to calculate"))
         a = list.count((id))
         sal = int(input("enter the employee salary:"))
         cal = ((sal/30)*a)
         print("your salary is",cal)
         # return cal
         function = {"id": sequence(), "Employeeid":id, "Salary": cal}
         x = mysalary.insert_one(function)
         print("sucessfully calculate employee salary")
      cal_salary()

    def Display_salary():
         for i in mysalary.find():
          print("Employee_id:", i["Employeeid"])
          print("Employee_Salary:", i["Salary"])
          print("-" * 70)


    while True:
        choice = int(input("enter the number of choise you want:"))
        if choice == 1:
            Add_Salary()
        elif choice == 2:
            Display_salary()
        else:
            print("enter the valid number:")
        op = input("'Do You Want To Continue with Salary Management?'")
        if op == 'y':
                print(
                    "please select the option form the below :\n"
                    "1. Add Employee salary\n"
                    "2. Display the employee salary\n")
        elif op == 'n':
            break
        else:
                print("please enter valid choice between ('y'/'n')")
                break

while True:
 choice = int(input("enter the number of choise you want:"))

 if choice == 1:
    Add_Employee()
 elif choice == 2:
    Delete_employee()
 elif choice == 3:
    print("Edit Employee Details")
    Edit_details()
 elif choice == 4:
    Display()
 elif choice == 5:
    print("Salary Management")
    salary()
 elif choice == 6:
    Attendence_Management()
 elif choice == 7:
     Annual()
 elif choice == 8:
     Holiday_management()
 else:
    print("enter valid number:")


 ch = input("do you want to continue with employee system??")
 if ch == 'y':
     print("please select the option form the below choice\n"
           "1. Add Employeee\n"
           "2. Delete Employee\n"
           "3. Edit Employee Details\n"
           "4. Display all Employee Details\n"
           "5. Salary Management\n"
           "6. Attendance Management\n"
           "7. Annual Functions Management\n"
           "8. Holiday Management")
 elif ch == 'n':
     print("Thank you")
     break
 else:
     print("please enter valid choice between ('y'/'n')")
     break





