def login(login_page):
    def wrapper(user,password):
        if user=="admin" and password=="1234":
            print("login successful")
            login_page(user,password)
        else:
            print("login failed")
    return wrapper

@login
def login_page(user,password):
    print("welcome to dashboard")

login_page("admin","1234")




def login(decorated):
    def wrapper(user, password):
        if user == "admin" and password == "1234":
            print("Login successful")
            decorated(user, password)
        else:
            print("Login failed")
    return wrapper

@login
def login_page(user, password):
    print("welcome to the dashboard")

login_page("admin", "1234")
login_page("someone", "bad")



import time

def execution_time(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        print("Elapsed:", end - start)
    return wrapper

@execution_time
def first_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print("sum :", total)

first_n(1000)



def admin_only(func):

    def wrapper(username):
        if username=="admin":
            print("login success")
            func(username)
        else:
            print("access denied")
    return wrapper

@admin_only
def dashboard(username):
    print("welcome to admin dashboard")        

dashboard('admin')
dashboard("guest")