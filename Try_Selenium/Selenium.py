from selenium import webdriver


def explore(inputPath="http://www.ni.com/hu-hu.html", outputPath="map.txt", depth=3):
    driver = webdriver.Chrome("C:\\Users\\Burai Péter\\Egyetem\\NI\\chromedriver.exe")
    driver.get(inputPath)
    myFile = open(outputPath, "w")
    #myFile.write(inputPath+"\n")
    #myFile.write("-------------------\n")

    map = {}
    lista = driver.find_elements_by_tag_name('a')
    tmpList = []
    tmpSubList = []
    lista2= []
    for ref in lista:
        r = ref.get_attribute('href')
        #print(r)
        if (not(r is None or "javascript:void" in r or len(r) == 0)):
            lista2.append(ref.get_attribute('href'))
            #myFile.write(r)
            #myFile.write("\n")
    #myFile.write("\n\n")
    #for ref in lista2:
        #print(ref.text+"  "+ref.get_attribute('href')+"\n")
        #print(lista.index(ref))
    map[inputPath] = lista2


    for x in range(depth-1):
        tmpList = []
        for ref in lista2:
            tmpList2 = []
            #r = ref.get_attribute('href')
            print(ref)
            #myFile.write(ref.get_attribute('href') + "\n")
            #myFile.write("-------------------\n")
            driver.quit()
            driver = webdriver.Chrome("C:\\Users\\Burai Péter\\Egyetem\\NI\\chromedriver.exe")
            driver.get(ref)
            newUrl = driver.current_url
            if(newUrl in map.keys()):
                print(newUrl+"  A ")
                continue
            print(map.keys())
            #driver.implicitly_wait(1000)
            tmpSubList = driver.find_elements_by_tag_name('a')
            print("-----------------------------------------------------")
            for t in tmpSubList:
                print(t.get_attribute('href'))
            print("-----------------------------------------------------")
            for subRef in tmpSubList:
                sr = subRef.get_attribute('href')
                if ( not(sr is None or "javascript:void" in sr or len(sr) == 0)):
                    tmpList.append(subRef.get_attribute('href'))
                    tmpList2.append(subRef.get_attribute('href'))
                    #myFile.write(sr)
                    #myFile.write("\n")
            #myFile.write("\n\n")
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