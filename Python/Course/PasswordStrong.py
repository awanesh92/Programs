import re
def minimumNumber(n,password):
    if n<6:
        return 6-n
    return bool(re.search(r'\d',password)) and bool(re.search(r'\w+[a-z]',password)) and bool(re.search(r'\w+[A-Z]',password)) and bool(re.search(r'\w+[!@#$%^&*()_+]',password))