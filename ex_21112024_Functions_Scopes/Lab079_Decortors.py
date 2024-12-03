def add_security(func):

    def wrapper():
        print("1.Before the function is called.")
        print("2. Add Helmet, Dashcard, gloves, knee gaurd,licence ")
        func() # # driving scooty
        print("3. After the function is called")
        print("4. Secure Driving, leave all the items")

    return wrapper()

@add_security
def drive_ola_scooter():
    print("ola")

@add_security
def driving_scooty():
    print("Normal function")
    print("I am driving a scooty")