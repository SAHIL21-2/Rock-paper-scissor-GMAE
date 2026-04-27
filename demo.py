# nested dict
sahil={"1st-key":{"amount":100,"account-type":"saving"}}

print(sahil["1st-key"]["account-type"])#statement
        #ask for balance query ehnever user deposit or withdraw
        #improve breaking statement
        #if it possible add account type:-saving current
        
        
        
        def optional():
    while(True):
        ask=input("If you want to check another options write y if not then n:")
        if(ask=='y' or ask=='Y'):
            continue
        else:
            break
        
        
        
        def statement():
    user_name=input("write your name: ")
    if user_name in user_data:
        user_pin=int(input("Enter your 4 digit account pin:"))
        if(user_pin==(user_data[user_name]["account_pin"])):
            print(user_data[user_name]["history"])
        else:
            print("Entered wrong pin")
    else:
        print("Wrong name or user does't exist")