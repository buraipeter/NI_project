from selenium import webdriver
from selenium.common.exceptions import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.common.by import By

def explore(inputPath="http://www.ni.com/hu-hu.html", outputPath="map.txt", depth=2):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(inputPath)
    myFile = open(outputPath, "w")
    first = True
    URLs = {inputPath}
    map = {}
    lista = driver.find_elements_by_xpath('//body//*')

    for x in range(depth):
        tmpList = []
        for url in URLs:
            if(not first):
                driver.get(url)
                time.sleep(2)
                lista = driver.find_elements_by_xpath('//body//*')
            else: first = False
            tmpList2 = []
            for elem in lista:
                try:
                    WebDriverWait(driver, 2).until(
                        element_to_be_clickable((By.CLASS_NAME, elem.get_attribute('class'))))
                    if(retryingHandleElement(elem,5)):
                        print(elem.tag_name )
                        print(type(elem))
                        elem.click()
                        newUrl = driver.current_url
                        if(newUrl not in tmpList2):
                            tmpList2.append(newUrl)
                        if(newUrl not in map.keys()):
                            tmpList.append(newUrl)
                            continue
                        print(newUrl + "  it has been already explored\n")
                    else:
                        print("There is some problem there")
                except StaleElementReferenceException as e:
                    print("Element is not available")
                    continue
                except WebDriverException:
                    print("Parameter is not of type Element")
            map[url] = tmpList2
            print("ABBA")
        URLs = tmpList

    for key in map.keys():
        myFile.write(map.keys().__str__()+"\n")
        myFile.write("-------------------\n")
        for p in map[key]:
            myFile.write(p+"\n")
        myFile.write("-------------------\n")

    myFile.close()
    driver.quit()
    return


def retryingHandleElement(elem, times):
    attempts = 0
    while( attempts < times):
        try:
            if (elem.is_enabled() and elem.is_displayed()):
                return True
        except StaleElementReferenceException:
            print("Stale element exception")
        attempts = attempts+1
    return False


explore()