import re
def checking_length(pwd):
    if len(pwd) >= 8:
         return True
    return False
def checking_uppercase(pwd):
    if re.search(r'[A-Z]', pwd):
        return True
    return False
    return False
def checking_lowercase(pwd):
    if re.search(r'[a-z]', pwd):
        return True
    return False
def checking_special_character(pwd):
    if re.search(r'[!@#$%^&*]', pwd):
            return True
    return False
def checking_digit(pwd):
    if re.search(r'[1-9]', pwd):
            return True
    return False
def checking_sequential(pwd):
    identical_pattern = r'(\d)\1{2,}'
    sequential_pattern = r'012|123|234|345|456|567|678|789'
    if re.search(sequential_pattern, pwd) or re.search(identical_pattern,pwd):
        return False
    return True
