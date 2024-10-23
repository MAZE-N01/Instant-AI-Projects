class Bank_Account:
    def __init__(self):
        self.name = input("Enter Your Name")
        self.__age = int(input("Enter Your Age"))
        self.__phone_number = int(input("Enter Your Phone Number"))
        self.__credit = 0
        self.__password = int(input("Create Your Password"))
        self.__national_id = int(input("Enter Your National ID"))
    def __check_password(self):

        check=int(input("Please Enter Your Password First"))
        if check==self.__password:
            return True
        else:
            return False
    def Add_Money(self):
        print("Welcome To,Add Money Service")
        if self.__check_password():
            amount = int(input("Enter Your Deposite"))
            self.__credit += amount
        else:
            print("Wrong Password")

    def Draw(self):
        print("Welcome To,Draw Money Service")
        if self.__check_password():
            amount = int(input("enter your deposite"))
            if amount < self.__credit:
                 self.__credit-=amount
                 print("Done,Please Take Your Money")

            else:
                {
                    print("You Are Poor")

                }
        else:
            print("wrong password")

    def Change_Password(self):
        print("Welcome To,Change Password Service Enter Old Password")
        if self.__check_password():
            newPassword = int(input("Enter Your New Password"))
            self.__password = newPassword
        else:

            {
                 print("Wrong Password")
            }

    def Check_credit(self):
        print("Welcome To,Check Credit Service")
        if self.__check_password():
            {
                print(self.__credit)
            }
        else:
            {
                print("Wrong Password")
            }

class QNB_Bank(Bank_Account):
    def Add_wallet(self):
        print("Welcome To,Add Wallet Service")
        self.__walletpasswod=int(input("Create Wallet Password"))
        self.__wallet=0

    def wallet_deposite(self):
        print("Welcome To,Wallet Deposite Service")
        if self.__ckeck_wallet_password():
            amount=int(input("Enter Wallet Deposit"))
            self.__wallet+=amount
        else:
            print("Wrong Password")
    def wallet_draw(self):
        print("Welcome To,Wallet Draw Service")
        if self.__ckeck_wallet_password():
            amount=int(input("How much did you want to draw?"))
            if amount< self.__wallet:
                self.__wallet-=amount
                print("Done,Take your money")
            else:
                print("sorry,you are poor")
    def wallet_change_password(self):
        print("Welcome To,Wallet Change Password Service Enter Old Password")
        if self.__ckeck_wallet_password():
            newpassword=int(input("Enter Wallet New Password"))
            self.__walletpasswod=newpassword
        else:
            print("Wrong Password")
    def __ckeck_wallet_password(self):

        check=int(input("Enter Wallet Password"))
        if check==self.__walletpasswod:
            return True
        else:
            return False
    def check_wallet_credit(self):
        print("Welcome To,Check Wallet Credit Service")
        if self.__ckeck_wallet_password():
            print(self.__wallet)
        else:
            print("wrong Password")
