# Author Vladimir SR


def username_checker(username):
    """
    Check the validity of the username
    :type username: str
    """
    if 6 <= len(username) <= 12:
        if username.isalnum():
            return True
    elif len(username) < 6:
        return "User name must be at least 6 characters long"
    elif len(username) > 12:
        return "User name must be at max 12 characters long"
    elif not username.isalnum():
        return "User name must be alphanumeric"


def password_checker(password):
    """
    Checks if the password is safe
    Returns true if it's safe
    Returns str if it's not safe
    :type password: str
    """
    if any(not b.isspace() for b in password):
        if len(password) >= 8:
            if any(l.islower() for l in password):
                if any(u.isupper() for u in password):
                    if any(n.isdigit() for n in password):
                        if any(a.isalpha() for a in password):
                            if any(not an.isalnum() for an in password):
                                return True
    return "Your password is not safe"


# def pass_checker(password):
#     passed = [False, False, False, False, False, False, False]
#     for check in password:
#         if not passed[0]:
#             if not check.isspace():




def login_checker():
    """
    This function asks for username and password
    Calls for the username_checker and password_checker
    And prints the results
    """
    print(username_checker(input("Username:")))
    print(password_checker(input("Password:")))
