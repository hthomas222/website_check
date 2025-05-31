import requests

def website_status(url_check):
    pass
    check = requests.get(url_check)
    if check.status_code == 200:
        print("The website is good!")
    elif check.status_code == 400:
        print("There is a client error!!!!")
    elif check.status_code == 500:
        print("There is an internal server error!")


url_check = input("Please input a url that you want to check: ")
website_status(url_check) 
