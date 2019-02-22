from selenium import webdriver
import pickle
import time

###build and download cookies, once you download the cookies, no need to run in the future for the website
driver = webdriver.Chrome()
driver.get("https://github.com/login")
time.sleep(50)##use this time to log in the website manually, input your username and passward
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb")) ###download the cookies, and save it in files


###use in cralwer data every time need input user name and passwards
driver.get('https://github.com/login')  #load websites
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)   #load cookies, it can automatically login, similar to remember user and user passward
driver.get('https://github.com/login')