from password_checker import PasswordChecker

"""This is a test-suite to make sure the PasswordChecker class
    plus all its methods are working as intended"""

def test_score_init():
    """Ensure objects initalised with class has self-class variable"""
    temp_object = PasswordChecker("")
    assert temp_object.password_score == 0

def test_has_number():
    """Ensure has number test meets condition correctly"""
    temp_object = PasswordChecker("999")
    temp_object.has_number()
    assert temp_object.password_score == 1

def test_upper_and_lower():
    """Ensure upper and lower test meets condition correctly"""
    temp_object = PasswordChecker("CaKe")
    temp_object.upper_and_lower_check()
    assert temp_object.password_score == 1

def test_alphanum_check():
    """Ensure alphanum test meets condition correctly"""
    temp_object = PasswordChecker("**--*__")
    temp_object.alphanum_check()
    assert temp_object.password_score == 1

def test_common_passwords():
    """Ensure common password test meets condition correctly"""
    temp_object = PasswordChecker("password")
    assert temp_object.common_passwords() == "fail"
