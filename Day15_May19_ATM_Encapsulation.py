
class ATM():
    def __init__(self,name,balance,pin=1234):
        self.name = name #public
        self._balance = balance #protect
        self.__pin = pin #private
    def pin_change(self):
        old_pin = int(input("please enter the old pin: "))
        if old_pin == self.__pin:
            new_pin = int(input("please enter the new pin: "))
            self.__pin = new_pin
            print(f"PIN Chnaged successfully")
        else:
            print(f"enter correct pin")
    def bank_name(self):
        print(f" Welcome to the bank {self.name}")
    def bal_enq(self):
        pin_1 = int(input(" please enter the pin: "))
        if pin_1 == self.__pin:
            print(f"the available balance is {self._balance}")
        else:
            print(f" WRONG PIN ENTERED")
    def credit(self):
        amount_1 = int(input(f"enter the amount to credit: "))
        self._balance += amount_1
        print(f" the {amount_1} credited successfully, avaiable balance is {self._balance}")
    def exit(self):
        print(f" exiting , Thanks for visiting our branch ATM")
        
        
    
        
        
            
            
            
            
    
    
    
    
        
ICICI = ATM("ICICI",10000) 
        
     
while True:
    print(f"1. Know the Bank Name")
    print(f"2. To Know Balance")
    print(f"3. pin Change")
    print(f"4. Credit")
    print(f"5. exit")
   
    
    choice = int(input("enter the choice:  "))
    
    if choice == 1:
        ICICI.bank_name()
    elif choice == 2:
        ICICI.bal_enq()
    elif choice == 3:
        ICICI.pin_change()
    elif choice == 4:
        ICICI.credit()
    
    else:
        ICICI.exit()
        break
        
        