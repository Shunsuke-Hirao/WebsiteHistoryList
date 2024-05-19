#Shunsuke Hirao
#Website History List


import urllib.request
import ezsheets
import datetime
import re
import pyinputplus as pyip
import os

# Initialize global variables
validURL = 0
countForSheet = 1
finish = False

# Start to run code
while not finish:
    print("Choose spreadsheet or text file to fill out Date and URL")
    #1 is for spreadsheet. 2 is for text file
    first_question = pyip.inputNum("For Spreadsheet, press 1, for text file, press 2: ")

#spreadsheeet
    if first_question == 1:
        #set up spreadsheet
        spreadsheet = ezsheets.createSpreadsheet(title='Website History List')
        spreadsheet[0].updateRow(1, ["Date", "URL"])
        
        while not finish:
            #function to get valid URL
            def open_websiteForOption1():
                global validURL
                global url
                find = False
                while not find:
                    url = input("Paste URL here: ")
                    if re.search(r"^https?://", url):
                        try:
                            webUrl = urllib.request.urlopen(url)
                            if webUrl.getcode() == 200:
                                validURL = 1
                                print("Succeeded it with option 1")
                                break
                        #case if the URL is forbidden.
                        except Exception:
                            print("It's forbidden to access! Try again")
                    #case if the URL is invalid.
                    else:
                        print("Invalid URL format! Try again!")

            open_websiteForOption1()

            #move to another function to create spreadsheet
            if validURL == 1:
                def creator_spreadsheet():
                    global countForSheet
                    #set up row with for range loop
                    for count in range(countForSheet):
                        count=count+1
                        countForSheet+=count
                        break

                    #get time
                    now = datetime.datetime.now()

                    #if the url.length is pretty long with string slicing
                    tricatedURL = url[:50] + ",,,"
                    #make it short less than 50
                    if len(url) > 50:
                        spreadsheet[0].updateRow(countForSheet, [str(now), tricatedURL])
                    else:
                        spreadsheet[0].updateRow(countForSheet, [str(now),url])

                creator_spreadsheet()

                #usermessage for continue or not
                user_question = pyip.inputYesNo("Date and URL added successfully! Do you want to continue? Yes or No: ")
                if user_question.lower() == "no":
                    print("Okay!")
                    finish = True
                    break

# text file
    elif first_question == 2:
        #set up textfile
        testFile = open(r"C:\Users\shun\Documents\programming practice\SecondSeme\pythonClass\FinalProject\WebsiteHistoryList.txt","w")
        testFile.write("Website History List \n")
        testFile.write("\n")
        
        while not finish:
            #function to get valid URL
            def open_websiteForoption2():
                global validURL
                global url
                find = False
                while not find:
                    url = input("Paste URL here: ")
                    if re.search(r"^https?://", url):
                        try:
                            webUrl = urllib.request.urlopen(url)
                            if webUrl.getcode() == 200:
                                validURL = 2
                                print("Succeeded it with option 2")
                                break
                        #case if the URL is forbidden.
                        except Exception:
                            print("It's forbidden to access! Try again")
                    #case if the URL is invalid.        
                    else:
                        print("Invalid URL format! Try again!")

            open_websiteForoption2()

            #move to another function to create textfile
            if validURL== 2:
                def creator_text_file():
                    #get time
                    now = datetime.datetime.now()

                    testFile.write("Date: "+str(now)+"\n")
                    #if the url.length is pretty long with string slicing
                    if len(url)>50:
                        tricatedURL=url[:50]+",,,"
                        #make it short less than 50
                        testFile.write("URL: "+tricatedURL+"\n")
                    else:
                        testFile.write("URL: "+url+"\n")

                    testFile.write("\n")
                    
                creator_text_file()

                #usermessage for continue or not
                user=pyip.inputYesNo("I put Date and URL successfully Do you want to continue? Yes or No: ")
                if user.lower()=="no":
                    print("Okay!")
                    testFile.close()
                    break
                                  
    #case if user typed not valid number                
    else:
        print("It's not valid number! Try again!")
        continue

    #end message
    print("Thank you for using this app")
    break
