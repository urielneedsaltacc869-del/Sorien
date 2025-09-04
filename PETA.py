from datetime import datetime
correct_emails = [
    "Urielneedsaltacc869@gmail.com",
    "ESTUPINPRINCESSMAYBELLINE@gmail.com",
    "angeloemata0915@gmail.com",
    "chevrylinl@gmail.com",
    "aring.sinukuan143@gmail.com",
    "sophiasantos011209@gmail.com",
    "llantoanthiona@gmail.com",
    "ivanchunsim@gmail.com"
]

correct_password = "JACKDANIELS"

logged_in = False
tries = 0

while not logged_in and tries < 3:
    input_email = input("Enter your email: ")
    input_password = input("Enter your password: ")

    if input_email in correct_emails and input_password == correct_password:
        print(" Login successful!\n")
        logged_in = True
    elif input_email not in correct_emails:
        print(" Email not found.\n")
    elif input_password != correct_password:
        print(" Wrong password.\n")
    else:
        print(" Login failed.\n")

    tries += 1

if not logged_in:
    print(" Too many attempts. Try again later.")
else:
    
    name = ""
    age = 0
    hobbies = ""
    birthday = ""

    while name == "" or age == 0 or hobbies == "" or birthday == "":
        name = input("Enter your username: ")

        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print(" Please enter a valid number for age.")
            age = 0
            continue

        hobbies = input("Enter your hobbies: ")
        birthday = input("Enter your birthday (YYYY-MM-DD): ")

       
        try:
            datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            print(" Invalid date format. Use YYYY-MM-DD.\n")
            birthday = ""  
            continue

        if name == "" or age == 0 or hobbies == "" or birthday == "":
            print(" Please complete all fields.\n")
        elif age < 13:
            print(" Sorry, you’re too young to join.")
            break
        else:
            print(f" Welcome {name}!\n   Hobbies: {hobbies}\n   Birthday: {birthday}")
