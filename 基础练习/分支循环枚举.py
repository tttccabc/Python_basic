account = 'shawn'
password = 'pass'

print('input username:')
username = input()

print('intput password:')
pwd = input()

if account == username and password == pwd:
    print(" auth succeed !")
else:
    print(" auth failure !")

print(list(set((1,2,3,1))))