u=[]
p=[]
def create():
    global u,p
    user=input('Choose Username: ')
    pwd=input('Choose Password: ')
    u.append(user)
    p.append(pwd)
    print('Username and password succesfully created')

def login():
    user=input('Enter Username: ')
    pwd=input('Enter Password: ')
    if (user==u[0]) and (pwd==p[0]):
        print('Welcome to our portal')
    else:
        print('Please enter correct username or password')
        
def screen():
    print('1:Create User')
    print('2:Login')
    print('3:Exit')
    a=input('Enter Choice: ')
    try:
        s=int(a)
        return(s)
    except:
        print('You can only enter Number')
    
while True:
    d=screen()
    if d==1:
        create()
    elif d==2:
        login()
    elif d==3:
        break
        
        
    
    
