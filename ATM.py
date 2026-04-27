from datetime import date
today = date.today()
        
#user database (here we stores user details)
user_data={"sahil":{"available_balance":100,"account_pin":2006,"history":[]},
            "khushboo":{"available_balance":0,"account_pin":2005,"history":[]},
            "aarav":{"available_balance":1000,"account_pin":2007,"history":[]}}
        
      
#this function creates new accounts for users
def new_account():
    user_name=input("write your name: ")
    if user_name in user_data:
        print("Account with this name is already exist")
    else:    
        balance=int(input("Enter amount(if you don't want want to add then enter 0):"))
        account_pin=int(input("choose a 4 digit account pin:"))
        user_data[user_name]={"available_balance":balance,"account_pin":account_pin,"history":[]}
        print("your account created succesfully✅")
        
        
    #statement function gave the statement record of the user
def statement():
    user_name=input("write your name: ")
    if user_name in user_data:
        user_pin=int(input("Enter your 4 digit account pin:"))
        if(user_pin==(user_data[user_name]["account_pin"])):#checking if user entered wrong pin or not
            print(user_data[user_name]["history"])
        else:
            print("Entered wrong pin")
    else:
        print("Wrong name or user does't exist")        
        
        
        #this function checks balance of users
def balance():
    user_name=input("enter your name: ")
    if (user_name in user_data):
        user_pin=int(input("Enter your 4 digit account pin:"))
        if(user_pin==(user_data[user_name]["account_pin"])):#checking if user entered wrong pin or not
            print("available balance :" ,user_data[user_name]["available_balance"])#printing balance
        else:
            print("Wrong pin")
    else:
        print("Wrong name or user does't exist")
        
#This function used to withdraw money
def withdraw():
    user_name=input("enter your name: ")
        
    if(user_name in user_data):
        withdraw_amount = int(input("Enter amont you want to withdraw: "))
        
        user_pin=int(input("Enter your 4 digit account pin:"))
        #checking if user entered wrong pin or not
        if(user_pin==(user_data[user_name]["account_pin"])):
            #checking if there enough money in user account
            if(user_data[user_name]["available_balance"]>=withdraw_amount):
                print("withdraw succesfull")
                #deducting the money from user account
                user_data[user_name]["available_balance"] = (user_data[user_name]["available_balance"])-withdraw_amount
                #ading statement/history
                user_data[user_name]["history"].append(f"{today} you withdraw {withdraw_amount} from your account")
                
                
            else:
                print("your account has not much amount")
        else:
            print("Wrong pin")        
    else:
        print("Enter a valid name or if you do not have account then create it first")
            
        
def credit():
    user_name=input("enter your name: ")
    if(user_name in user_data):
        user_pin=int(input("Enter your 4 digit account pin:"))
        #checking if user entered wrong pin or not
        if(user_pin==(user_data[user_name]["account_pin"])):
            credit_amount = int(input("Enter amount you want to credit: "))
            #adding amount to user account
            user_data[user_name]["available_balance"]= (user_data[user_name]["available_balance"])+credit_amount
            print("credited amount succesfully")
            #ading statement/history
            user_data[user_name]["history"].append(f"{today} you are credited {credit_amount} from your account")
        else:
            print("Wrong pin")
    else:
        print("Enter a valid name or if you do not have account then create it first")
            
        
while(True):
        # MAKING HEADER SECTION OR MENU SECTION OF THE ATM 
    print("----WELCOME TO E-ATM----\nPLEASE CHOOSE A SERVICE TO PROCEED:")
    print("1.Open an account\n2.Check your balance\n3.withdraw money\n4.Add Credit\n5.Check statement\n")
    response=int(input("Enter the corresponding digit of your chice: "))
    
    if(response==1):
        new_account()
    elif(response==2):
        balance()
    elif(response==3):
        withdraw()
    elif(response==4):
        credit()
    elif(response==5):
        statement()
    else:
        print("Choose response from choice: ")
        continue
    #asking user for if they want another service
    ask=input("If you want to check another options write y if not then n:")
    if(ask=='y' or ask=='Y'):
        continue
    else:
        break


