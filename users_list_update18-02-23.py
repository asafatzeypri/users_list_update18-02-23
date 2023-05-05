import pymongo
import pyfiglet
import pwinput
import getpass

#create the database in mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
list = db["mylist"]


#create a bannner
banner = pyfiglet.figlet_format("welcome to base", font = "standard")
print(banner)

#create a menu
print ("for sign up enter 1 \n""for sign in enter 2 \n""____________________")
x = (input("enter the your choice: "))
print (x)


#to sign up and insert to database
if x==("1"):
    user = input("Enter your username: ")
    password = pwinput.pwinput(prompt="enter: ")
    email = input("Enter your email: ")


    document = {"user": user, "password": password, "email": email}

    list.insert_one(document)

    client.close()
    print("Welcome!")

#to sign in
elif x==("2"):
    user_in = input("Enter your username: ")
    password_in = input("Enter your password: ")
    dblist = list.find_one(
        {'user': user_in, 'password': password_in}


    )
    # print(dblist)

    if dblist is None:
        print("username or password incorrect")
    else:
        print("you are connected")


else:
    print("its just 2 options go back later!")








("Enter your password: ")