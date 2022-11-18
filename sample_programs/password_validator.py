import re


def very_weak_password(password):
    regex = re.compile("[0-9]{8,}$")
    result = regex.search(password)
    if result is None:
        return False
    pw = result.group()
    print(pw)
    if pw == password:
        return True
    else:
        return False


def weak_password(password):
    regex = re.compile("[a-zA-Z]{8,}$")
    result = regex.search(password)
    if result is None:
        return False
    pw = result.group()
    print(pw)
    if pw == password:
        return True
    else:
        return False


def strong_password(password):
    regex = re.compile("^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+){8,}$")
    result = regex.search(password)
    if result is None:
        return False
    pw = result.group()
    print(pw)
    if pw == password:
        return True
    else:
        return False


def very_strong_password(password):
    regex = re.compile("^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[\!\@\#\$\%\^\&\*\(\)])([a-zA-Z0-9\!\@\#\$\%\^\&\*\(\)]+){8,}$")
    result = regex.search(password)
    if result is None:
        return False
    pw = result.group()
    print(pw)
    if pw == password:
        return True
    else:
        return False


def main():
    password = input("Enter a password:\n")
    if len(password) < 8:
        return False
    if very_weak_password(password):
        print(f'The password {password} is a very weak password.')

    elif weak_password(password):
        print(f'The password {password} is a weak password.')

    elif strong_password(password):
        print(f'The password {password} is a strong password.')

    elif very_strong_password(password):
        print(f'The password {password} is a very strong password.')

    else:
        print("Invalid Password")


if __name__ == '__main__':
    main()
