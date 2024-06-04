import time
current_balance =5000 
password =1234 

print("Insert your card")

time.sleep(2)
print("Authenticating..")
time.sleep(3)
print("Card scanned successfully")

pin = int(input("Enter your pin: "))

# history list
history =[]
while True:
    if(pin == password):
        print('''\nChooose what you want to do \n 1.Withdraw\n2.Deposit\n3.Transfer\n4.Quit''')


        try:
            option = int(input("Enter your choice: "))

        except:
            print("Enter your choice again: ")

        if option==1:
            withdraw_amount = int(input("\nEnter the amount you want top withdraw: "))
            time.sleep(2)
            print("Collect your cash! ")
            current_balance = current_balance - withdraw_amount
            time.sleep(1)
            print(f"Your updated balance is {current_balance}") 

            dep = "- "+str(withdraw_amount)
            history.append(dep)

        if option ==2:
            deposit_amount = int(input("\nEnter the amount you want to deposit: "))
            print("Processing...")
            time.sleep(1)
            print(f"{deposit_amount} , has been credited successfully!")
            current_balance = current_balance + deposit_amount 
            time.sleep(2)
            print(f"Your updated balance is, {current_balance}")

            crd = "+ "+str(deposit_amount)
            history.append(crd)


        if option ==3:
            taccount = input("Enter the reciever's account no. : ")
            tamount =int(input("Enter the amount you want to transfer: "))
            time.sleep(1)
            
            print("\nAuthenticating...")
            time.sleep(2)

            if(tamount <=current_balance):
                print(f"Money transfered successfully to {taccount}!")
                current_balance = current_balance - tamount
                print(f"Your updated balance is {current_balance}")

                snd = "- "+str(tamount)
                history.append(snd)


            else:
                print("Insufficient balance.")

        if option == 5:
            print("Displaying Transaction History...")
            time.sleep(2)
            print(history)

        if option == 4:
            print("Exiting securly..")
            break
    else:
        time.sleep(1)
        print("\nENTERED PIN IS WRONG")
        print("Exiting...")
        exit()