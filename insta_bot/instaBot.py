#!/usr/bin/python3
#written by antymijaljevic@gmail.com

"""
c/p usr/local/bin/chromedriver before
use vim or hexeditor
Search for cdc_ by typing /cdc_ and pressing return.
Enable editing by pressing a.
Delete any amount of $cdc_lasutopfhvcZLmcfl and replace what was deleted with an equal amount characters. If you don't, chromedriver will fail.
After you're done editing, press esc.
To save the changes and quit, type :wq! and press return.
If you don't want to save the changes, but you want to quit, type :q! and press return.
You're done.

THIS IS TO AVOID JAVASCRIPT BOT DETECTION ALGORITHMS
"""

from credentials_insta import user, password, userOrHash, staticPercent
import os
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys
from random import randint
from random import random
os.system('clear');

class bot ():
    """Loading chromedriver, max window, get log in page"""
    def __init__(self):
        self.driver = webdriver.Chrome();
        self.driver.maximize_window();
        self.driver.get('https://www.instagram.com/accounts/login/?hl=en');

    def logIn(self):
        """login form fill up"""
        sleep(1);
        userIn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input');
        passIn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input');
        userIn.clear(); passIn.clear();
        userIn.send_keys(user); passIn.send_keys(password);
        logInButton = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click();
        sleep(2);
        turnOffNo = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click();

    def searchBar(self, hashtag):
        """searching for hashtag or username"""
        x = randint(2,6);  #adding random numbers to avoid bot detection algorithms
        sleep(x);
        search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div').click();
        searchInput = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input');
        searchInput.send_keys(hashtag);
        sleep(x);
        try:
            searchInput.send_keys(Keys.ENTER); searchInput.send_keys(Keys.ENTER);
        except:
            downDropUser = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a/div').click();

    def randomLikeAlgorithm(self):
        """random float numbers for likes to avoid bot detection algorithms"""
        randomPercent = random();
        if (randomPercent < staticPercent):
            like = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button').click();
            try:
                sleep(0.5)
                blockAlert = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]').click();
            except:
                try:
                    sleep(2)
                    blockAlert = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/button[2]').click();
                except:
                    pass

    def profilePicSlide(self):
        """"Open first picture on profile and click right for next, loop until last and x window"""
        y = randint(2,6);  #adding random numbers to avoid bot detection algorithms
        sleep(3);
        try:
            firstPic = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a/div/div[2]').click();
        except Exception:
            try:
                firstPicDiff = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div/div[1]/a/div/div[2]').click();
            except Exception:
                try:
                    firstPicHashtag = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click();
                except:
                    pass

        sleep(y);
        self.randomLikeAlgorithm();
        try:
            firstRight = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a').click();
        except:
            firstRightDiff = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]').click();

        for i in range(9):
            z = randint(2,6); #adding random numbers to avoid bot detection algorithms
            sleep(z);
            self.randomLikeAlgorithm();
            try:
                secondRight = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]').click();
            except:
                exitX = self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click();
                break
        try:
            exitX = self.driver.find_element_by_xpath('/html/body/div[4]/div[3]/button').click();
        except:
            pass

instaAmigo = bot();
instaAmigo.logIn();
while True:
    for i in range(len(userOrHash)):
        instaAmigo.searchBar(userOrHash[i]);
        instaAmigo.profilePicSlide();
    sleep(60*120)
