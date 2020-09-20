import xml.dom.minidom
import os
from os import path

foodDataList = []
i = 0

class foodData():
    name = ""
    price = ""
    description = ""
    calories = 0

def readXml(file):
    
    doc = xml.dom.minidom.parse(file)
    # print(doc.nodeName)
    # print(doc.firstChild.tagName)

    foods = doc.getElementsByTagName("food")
    for node in foods:
        f = foodData()
        names = node.getElementsByTagName("name")
        prices = node.getElementsByTagName("price")
        descs = node.getElementsByTagName("description")
        cals = node.getElementsByTagName("calories")

        for name in names:
            nameText = name.childNodes[0].nodeValue
            f.name = nameText
            # print(nameText)

        for price in prices:
            nameText = price.childNodes[0].nodeValue
            f.price = nameText
            # print(nameText) 

        for desc in descs:
            nameText = desc.childNodes[0].nodeValue
            f.description = nameText
            # print(nameText) 

        for cal in cals:
            nameText = cal.childNodes[0].nodeValue
            f.calories = nameText
            # print(nameText)
        
        # print("-----------------")
        foodDataList.append(f)

def prepareFile(file):
    if path.exists(file) == True:
        print("Filu löytyi")
        return open(file, "a+")
    else:
        print("Filua ei ole")
        return open(file, "w+")

def writeToCsv(file):
    separator = ";"
    # f = open(file, "w+")
    f = prepareFile(file)
    for fData in foodDataList:
        line = fData.name+separator+fData.description+separator+fData.price+separator+fData.calories+"\n"
        f.write(line)
    
    f.close()

def main():
    print("Reading xml")
    readXml("breakfast_menu.xml")
    print("Writing to csv")
    writeToCsv("breakfast_menu.csv")
    print("All ready! :)")
    # print("Item exists: "+str(path.exists("breakfast_menu.csv")))
    # print(prepareFile("breakfast_menu.csv"))

if __name__ == "__main__":
    main()