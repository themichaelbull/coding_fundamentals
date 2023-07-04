"""This program checks to see if your password is hot stuff or gross"""

### ### ###
# ASCII Art
### ### ###

import sys

LOCK_ART = """
    .--------.
    / .------.\\
    / /         \\
    | |        | |
_| |________| |_
.' |_| PW Check |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  |      |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'
'.________________.'
    
    """

### ### ###
# Class Stuff
### ### ###

class PasswordChecker:
    """This class contains all the methods relating to password checking"""

    def __init__(self, user_password):
        """Initialises function with users password and empty score variable"""
        self.user_password = user_password
        self.password_score = 0

    def has_number(self):
        """Method checks if password contains a number"""
        criteria_met = False
        for character in self.user_password:
            if character.isdigit():
                criteria_met = True
        if criteria_met is True:
            self.password_score += 1

    def length_check(self):
        """Method checks password is over a specific length"""
        if len(self.user_password) > 12:
            self.password_score += 1

    def upper_and_lower_check(self):
        """Method checks password contains both upper and lower"""
        if self.user_password.isupper() is False and self.user_password.islower() is False:
            self.password_score += 1

    def alphanum_check(self):
        """Method checks password contains non alpha numeric characters"""
        criteria_met = False
        for character in self.user_password:
            if character.isalnum():
                pass
            else:
                criteria_met = True
        if criteria_met is True:
            self.password_score +=1

    def common_passwords(self):
        """Method checks password against list of common passwords"""
        password_list = ["123", "1234", "12345", "123456", "12345678", "password",
                         "password1", "password123", "qwerty", "guest", "vip",
                         "pass@123", "asdasd", "123qwe", "123123123", "aaaaaa",
                         "1234qwer", "football", "master", "dragon"]
        if self.user_password in password_list:
            return "fail"
        return None

    def password_score_result(self, score):
        """Method gets score for user"""
        score_dict = {0: "Very Weak", 1: "Weak", 2: "Moderate", 3: "Strong", 4: "Very Strong"}
        user_score = score_dict[score]
        return user_score

### ### ###
# Main Program
### ### ###

password_history = {}

print(LOCK_ART)
print("*" * 80, "\n\nHey there! Welcome to the Password Checker!")
print("Press Q to quit at anytime!","\n\n", "*" * 80, "\n")

def main():
    """Main function of program"""

    while True:
        print("Previous Password Attempts:\n")
        for password, score in password_history.items():
            print(f"Password: {password}\nScore: {score}")
            print("*" * 80)
        password = input("\n\n\nHey there! Give me your password, and I'll give you a score: ")

        if password == "Q":
            sys.exit()
        else:
            pass
        test_object = PasswordChecker(password)
        common_pw_test = test_object.common_passwords()
        if common_pw_test == "fail":
            password_history[password] = "Failure"
            continue
        test_object.has_number()
        test_object.length_check()
        test_object.upper_and_lower_check()
        test_object.alphanum_check()
        score = test_object.password_score
        result = test_object.password_score_result(score)
        password_history[password] = result

main()