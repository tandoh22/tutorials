# validating username

username = input('enter your username: ')
if len(username) > 12:
    print("usernames can not be more than 12")
elif not username.find(' ') == -1:
    print("usernames can not contain space")
elif not username.isalpha():
    print("usernames can not contain digits")  
else:
    print(f"welcome {username}")          
