from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from datetime import datetime


PATHtoChromeDtiver = "./chromedriver"

driver=webdriver.Chrome(PATHtoChromeDtiver)

delimiter = "\t"

def exportLineToFile(file, outputStr):
    file.write(outputStr + "\n")


def exportLawsList(url, fileName):
    print(url)
    filePath = os.getcwd() + "/output/" + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + fileName + ".txt"
    file = open( filePath , "a")
    
    pageId=1
    searchNextPage = True
    
    searchURL = url + str(pageId)

    print(searchURL)
    print(type(searchURL))
    driver.get(searchURL)
    
    tableHeaders = driver.find_elements_by_class_name("rgHeader.LawListHeaderRow")
    outputStr = ""
    for header in tableHeaders:
        outputStr += header.text + delimiter
    exportLineToFile(file, outputStr)
    
    

    while searchNextPage:
        searchURL = url + str(pageId)
        driver.get(searchURL)
        elements = driver.find_elements_by_class_name("rgRow")
        if len(elements) == 0:
            searchNextPage = False
        else:
            for element in elements:
                attributesList = element.find_elements(By.TAG_NAME, "td")
                outputString = ""
                for attribute in attributesList:
                    outputString += attribute.text+ delimiter
                exportLineToFile(file,outputString)
        pageId += 1

    file.close()



exportLawsList("https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawLaws.aspx?t=lawlaws&st=lawlaws&pn=", "LawLaws")

exportLawsList("https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawReshumot.aspx?t=lawreshumot&st=lawreshumotlaws&pn=", "LawReshumot")

exportLawsList("https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawSuggestionsSearch.aspx?t=lawsuggestionssearch&st=currentknesset&ki=23&sb=latestsessiondate&so=d&pn=", "LawSuggestions")

print("finished")

driver.quit()