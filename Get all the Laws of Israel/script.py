from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

PATHtoChromeDtiver = "./chromedriver"

driver=webdriver.Chrome(PATHtoChromeDtiver)

def exportLineToFile(file, outputStr):
    print(outputStr)


url="https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawLaws.aspx?t=lawlaws&st=lawlaws&pn=2&sb=LatestPublicationDate&so=D"

driver.get(url)

tableHeaders = driver.find_elements_by_class_name("rgHeader.LawListHeaderRow")
outputStr = ""
for header in tableHeaders:
    outputStr += header.text + ','
exportLineToFile(None, outputStr)

elements = driver.find_elements_by_class_name("rgRow")
for element in elements:
    attributesList = element.find_elements(By.TAG_NAME, "td")
    outputString = ""
    for attribute in attributesList:
       outputString += attribute.text+ ','
    print(outputString)
