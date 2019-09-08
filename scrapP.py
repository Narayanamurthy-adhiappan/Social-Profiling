from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time

options = webdriver.ChromeOptions() 
chromedriver = "/usr/bin/chromedriver";
os.environ["webdriver.chrome.driver"] = chromedriver
options.add_argument("user-data-dir=/home/murthy/.config/google-chrome/")
driver = webdriver.Chrome(chromedriver, chrome_options=options) #I actually used the chromedriver and did not test firefox, but it should work.
profile_link="https://www.linkedin.com/in/narayanamoorthy-a-a927a7102/"
driver.get(profile_link)
time.sleep(20)

html=driver.page_source
soup=BeautifulSoup(html, "html.parser") #specify parser or it will auto-select for you
Name =soup.find('li', { "class" : "inline t-24 t-black t-normal break-words" })
Designation = soup.find('h2', {"class" : "mt1 t-18 t-black t-normal"})
imageurl = soup.find('img', {"class" : "profile-photo-edit__preview"})
print "Name : " + Name.text.strip()
print "Designation : " + Designation.text.strip().split(" at ")[0]
print "Company : " + Designation.text.strip().split(" at ")[1]
print "User Profile DP Source :" + imageurl['src']

