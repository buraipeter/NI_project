from selenium import webdriver
from selenium.common.exceptions import *

def explore(inputPath="http://www.ni.com/hu-hu.html", outputPath="map.txt", depth=2):
    driver = webdriver.Chrome("chromedriver.exe")
    driver.set_page_load_timeout(30)
    driver.get(inputPath)
    myFile = open(outputPath, "w")


    map = {}
    lista = driver.find_elements_by_tag_name('a')
    lista2= []
    for ref in lista:
        r = ref.get_attribute('href')
        if (not(r is None or "javascript:void" in r or len(r) == 0)):
            lista2.append(ref.get_attribute('href'))
    map[inputPath] = lista2


    for x in range(depth-1):
        tmpList = []
        for ref in lista2:
            tmpList2 = []
            print(ref)
            driver.get(ref)
            newUrl = driver.current_url
            if(newUrl in map.keys()):
                #print(newUrl+"  it has been already explored")
                continue
            print(map.keys())
            tmpSubList = driver.find_elements_by_tag_name('a')
            for subRef in tmpSubList:
                try:
                    sr = subRef.get_attribute('href')
                except StaleElementReferenceException:
                    print("Element is not available")
                    continue

                if ( not(sr is None or "javascript:void" in sr or len(sr) == 0)):
                    tmpList.append(sr)
                    tmpList2.append(sr)
                    #print(sr+"\n")
            map[ref] = tmpList2
        lista2 = tmpList


    for key in map.keys():
        myFile.write(map.keys().__str__()+"\n")
        myFile.write("-------------------\n")
        for p in map[key]:
            myFile.write(p+"\n")
        myFile.write("-------------------\n")


    myFile.close()
    driver.quit()
    return

explore()