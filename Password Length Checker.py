def password_checker(password_final):
    if len(password_final) < 3:
        print("Password is too short! Over 3 characters please!")
    elif len(password_final) > 50:
        print("Password must be a maximum is 50 characters")
    else:
        print("Password looks good!")


password_checker(input("Please enter your password: "))
