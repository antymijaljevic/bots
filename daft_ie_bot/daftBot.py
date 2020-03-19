#!/usr/bin/python3
#written by antymijaljevic@gmail.com
#/usr/local/bin/chromedriver c/p before

from credentials import user, password, maxPriceInput, bedroomsInput, yourNumber, message, timer
import os
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
os.system('clear')

class daftBot():
    def __init__(self):
        #selecting chrome browswer and setting to max window size
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://www.daft.ie/')

    def login(self):
        #login form
        logIn = self.driver.find_element_by_xpath('//*[@id="header"]/div/div[1]/div/div/div[1]/ul/li[1]/a').click()
        userIn = self.driver.find_element_by_xpath('//*[@id="auth_username"]')
        userIn.clear()
        userIn.send_keys(user)
        passIn = self.driver.find_element_by_xpath('//*[@id="auth_password"]')
        passIn.clear()
        passIn.send_keys(password)
        logInButton = self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        self.driver.get('https://www.daft.ie/')
        sleep(1)
        toRent = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/div[2]/div/div/div[1]/ul[1]/li[4]/a').click()
        searchButton = self.driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div/div[2]/div/div/div[2]/form/button').click()

    def quickSearch(self):
        #wished set up for quick search
        chooseArea = Select(self.driver.find_element_by_xpath('//*[@id="cc_id"]'))
        chooseArea.select_by_index(2)
        maxPrice = Select(self.driver.find_element_by_xpath('//*[@id="mxp"]'))
        maxPrice.select_by_value(maxPriceInput)
        bedrooms = Select(self.driver.find_element_by_xpath('//*[@id="mxb"]'))
        bedrooms.select_by_index(bedroomsInput)
        searchButton = self.driver.find_element_by_xpath('//*[@id="refine_submit"]').click()
        dateEntered = self.driver.find_element_by_xpath('//*[@id="sr-sort"]/li[3]/a').click()

    def advanceSearch(self):
        #move to advance search
        advanceSearch = self.driver.find_element_by_xpath('/html/body/div[13]/div/div[2]/form/fieldset/a').click()
        #wished set up for advance search
        city = self.driver.find_element_by_xpath('//*[@id="cc_id"]/dt').click()
        city2 = self.driver.find_element_by_xpath('//*[@id="cc_id"]/dd/ul/li[2]').click()
        sleep(1) #should be replaced with wait
        maxPrice = self.driver.find_element_by_xpath('//*[@id="max_price"]/dt').click()
        maxPrice2 = self.driver.find_element_by_xpath('//*[@id="max_price"]/dd/ul/li[30]').click()
        withPhotos = self.driver.find_element_by_xpath('//*[@id="advanced-container"]/form/span/div[11]/span[2]/div/div[1]/label').click()
        searchBig = self.driver.find_element_by_xpath('//*[@id="advanced-container"]/form/span/div[19]/span[2]/input').click()
        dateEntered = self.driver.find_element_by_xpath('//*[@id="sr-sort"]/li[3]/a').click()

    def sending_mail(self):
        try:
            mobNum = self.driver.find_element_by_xpath('//*[@id="your_phone"]')
            mobNum.clear()
            mobNum.send_keys(yourNumber)
            messageToLandlord = self.driver.find_element_by_xpath('//*[@id="your_message"]')
            messageToLandlord.clear()
            messageToLandlord.send_keys(message)
            mobNum = self.driver.find_element_by_xpath('//*[@id="terms-checkbox"]').click()
            #sendMessage = self.driver.find_element_by_xpath('//*[@id="ad_reply_submit"]').click() ~ last trigger

        except:
            self.driver.back()
            sleep(1)

        self.driver.back()
        sleep(1)

    def listingAps(self):
        #looping through all first twenty apartments, div 6 is missing so it's skipped
        divList = list(range(2,6)) + list(range(7,23)) #~activate for more then four adds
        global shortCodeDb
        shortCodeDb = []
        newestAdd = self.driver.find_element_by_xpath('//*[@id="sr_content"]/tbody/tr/td[1]/div[2]/div[1]/h2/a').text
        print("Program has sent email to landlord at:\n")

        for n in divList:
            apartments20title = self.driver.find_element_by_xpath(f'//*[@id="sr_content"]/tbody/tr/td[1]/div[{n}]/div[1]/h2/a').text
            apartments20 = self.driver.find_element_by_xpath(f'//*[@id="sr_content"]/tbody/tr/td[1]/div[{n}]/div[1]/h2/a').click()
            try:
                shortCode = self.driver.find_element_by_xpath('//*[@id="description"]/div[2]/a').text
                shortCodeDb.append(shortCode)
            except:
                shortCode = self.driver.find_element_by_xpath('//*[@id="description"]/div[3]/a').text
                shortCodeDb.append(shortCode)

            if n <= 6:
                ordinal = n - 1
            else:
                ordinal = n - 2
            print(str(ordinal)+".",apartments20title+"\nClick here for more >> "+str(shortCode)+"\n")
            self.sending_mail()

        print(f"\nMost recent apartment: {newestAdd}\nProgram will keep you updated, once when new add appears and send email to the landlord accordingly.")

    def upcomingAdds(self):
        while True:
            apartmentIn = self.driver.find_element_by_xpath('//*[@id="sr_content"]/tbody/tr/td[1]/div[2]/div[1]/h2/a')
            apartmentIn.click()
            apartmentTitle = self.driver.find_element_by_xpath('//*[@id="address_box"]/div[1]/h1').text
            try:
                shortCode = self.driver.find_element_by_xpath('//*[@id="description"]/div[2]/a').text
            except:
                shortCode = self.driver.find_element_by_xpath('//*[@id="description"]/div[3]/a').text

            if shortCode in shortCodeDb:
                self.driver.back()
            else:
                shortCodeDb.append(shortCode)
                Print("f\nWe got new add here! Sending email to landlord now...done\nApartment: {apartmentTitle}\nAdded: " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"\n")
                self.sending_mail()
            sleep(timer)
            self.driver.refresh()

longinus = daftBot()
longinus.login()
#longinus.quickSearch()
longinus.advanceSearch()
longinus.listingAps()
longinus.upcomingAdds()
