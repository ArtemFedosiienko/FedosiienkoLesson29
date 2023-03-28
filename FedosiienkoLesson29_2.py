
import hashlib

autorize = dict()
login1 = input("Оберіть Ваш логін: ")
passwd1 = input("Введіть Ваш пароль: ")

while True:
    login2 = input("Оберіть Ваш логін: ")
    if login2 == login1:
        print("Такий логін вже існує!")
    else:
        passwd2 = input("Введіть Ваш пароль: ")
        break

passwd_hash1 = hashlib.md5(bytes(passwd1, 'UTF-8'))
passwd_hash2 = hashlib.md5(bytes(passwd2, 'UTF-8'))

autorize[login1] = passwd_hash1.hexdigest()
autorize[login2] = passwd_hash2.hexdigest()

print(autorize)

my_login = input("Введіть Ваш логін: ")

my_passwd = input("Введіть Ваш пароль : ")
my_passwd_hash = hashlib.md5(bytes(my_passwd, 'UTF-8'))
print(my_passwd_hash.hexdigest())



if my_passwd_hash.hexdigest() in autorize.values():
    print("Ви авторизовані!")
else:
    print("Невірний пароль!")