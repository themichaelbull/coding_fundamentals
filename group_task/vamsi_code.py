class Verify_Password:
    def __init__(self, password):
        self.password = password
        
    def checklength(self):
        if len(self.password) > 6 and len(self.password) < 10 :
            return True
        elif len(self.password) > 10:
            return True
        else:
            self.password_strength = 0   
            return False

    def checkalpha(password):
        if password.isalpha() == True:
            #password_strength += 1
           return True
            
        elif password.isnumeric() == True:
            #password_strength += 1
            return True
        elif password.isalnum() == True:
            #password_strength += 1
            return True
        elif password.isnumeric() and password.isalpha() and password.isalnum() == True:
            #password_strength += 1
            return True
        elif password.isnumeric() and password.isalpha() == True:
            #password_strength += 1
            return True
        else:
            #password_strength =0
            return False

    def checkcase(self,password):
        if password.islower():
            return True
        elif password.isupper():
            return True
        elif password.islower() and password.isupper():
            return True
        else:
            return False 

password_strength =0 

userpassword= input("Enter Password: ")

while True:
    if len(userpassword) > 0:
        password_obj = Verify_Password(userpassword)
        check1 = password_obj.checklength()
        # check1=Verify_Password.checklength(userpassword)
        if check1 is True:
            password_strength=+1
            print (f"Counter for length : {password_strength}")
            break
        #check2 = Verify_Password.checkalpha(userpassword)
        #if check2 is True:
            #password_strength=+1
            print (f"Counter for Alpha: {password_strength}")
            #break
        
        #check3 = Verify_Password.checkcase(userpassword)
        #if check3 is True:
            
        else:
            print("Password needs to be changed")
            break