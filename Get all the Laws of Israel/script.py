from selenium import webdriver
PATH = "./chromedriver"

driver=webdriver.Chrome(PATH)
url="https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawLaws.aspx?t=lawlaws&st=lawlaws&pn=2&sb=LatestPublicationDate&so=D"

driver.get(url)
s=driver.find_elements_by_class_name("rgRow")
for i in range(len(s)):
    print(s[i].text)