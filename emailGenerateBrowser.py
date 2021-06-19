import random
import time

import database as db

from selenium import webdriver


class Browser2:
    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Chrome()
        Browser2.goGmailGenerator(self)

    def goGmailGenerator(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser2.login(self)

    def login(self):
        listea = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        i = random.choice(listea)
        if i == 0:
            name = db.kisi0.name
            surname = db.kisi0.surname
            gmail = db.kisi0.username
            password = db.kisi0.password
            telephone = db.kisi0.telephone
        elif i == 1:
            name = db.kisi1.name
            surname = db.kisi1.surname
            gmail = db.kisi1.username
            password = db.kisi1.password
            telephone = db.kisi1.telephone
        elif i == 2:
            name = db.kisi2.name
            surname = db.kisi2.surname
            gmail = db.kisi2.username
            password = db.kisi2.password
            telephone = db.kisi2.telephone
        elif i == 3:
            name = db.kisi3.name
            surname = db.kisi3.surname
            gmail = db.kisi3.username
            password = db.kisi3.password
            telephone = db.kisi3.telephone
        elif i == 4:
            name = db.kisi4.name
            surname = db.kisi4.surname
            gmail = db.kisi4.username
            password = db.kisi4.password
            telephone = db.kisi4.telephone
        elif i == 5:
            name = db.kisi5.name
            surname = db.kisi5.surname
            gmail = db.kisi5.username
            password = db.kisi5.password
            telephone = db.kisi5.telephone
        elif i == 6:
            name = db.kisi6.name
            surname = db.kisi6.surname
            gmail = db.kisi6.username
            password = db.kisi6.password
            telephone = db.kisi6.telephone
        elif i == 7:
            name = db.kisi7.name
            surname = db.kisi7.surname
            gmail = db.kisi7.username
            password = db.kisi7.password
            telephone = db.kisi7.telephone
        elif i == 8:
            name = db.kisi8.name
            surname = db.kisi8.surname
            gmail = db.kisi8.username
            password = db.kisi8.password
            telephone = db.kisi8.telephone
        elif i == 9:
            name = db.kisi9.name
            surname = db.kisi9.surname
            gmail = db.kisi9.username
            password = db.kisi9.password
            telephone = db.kisi9.telephone
        elif i == 10:
            name = db.kisi10.name
            surname = db.kisi10.surname
            gmail = db.kisi10.username
            password = db.kisi10.password
            telephone = db.kisi10.telephone
        elif i == 11:
            name = db.kisi11.name
            surname = db.kisi11.surname
            gmail = db.kisi11.username
            password = db.kisi11.password
            telephone = db.kisi11.telephone
        elif i == 12:
            name = db.kisi12.name
            surname = db.kisi12.surname
            gmail = db.kisi12.username
            password = db.kisi12.password
            telephone = db.kisi12.telephone
        elif i == 13:
            name = db.kisi13.name
            surname = db.kisi13.surname
            gmail = db.kisi13.username
            password = db.kisi13.password
            telephone = db.kisi13.telephone
        elif i == 14:
            name = db.kisi14.name
            surname = db.kisi14.surname
            gmail = db.kisi14.username
            password = db.kisi14.password
            telephone = db.kisi14.telephone
        elif i == 15:
            name = db.kisi15.name
            surname = db.kisi15.surname
            gmail = db.kisi15.username
            password = db.kisi15.password
            telephone = db.kisi15.telephone
        elif i == 16:
            name = db.kisi16.name
            surname = db.kisi16.surname
            gmail = db.kisi16.username
            password = db.kisi16.password
            telephone = db.kisi16.telephone
        elif i == 17:
            name = db.kisi17.name
            surname = db.kisi17.surname
            gmail = db.kisi17.username
            password = db.kisi17.password
            telephone = db.kisi17.telephone
        elif i == 18:
            name = db.kisi18.name
            surname = db.kisi18.surname
            gmail = db.kisi18.username
            password = db.kisi18.password
            telephone = db.kisi18.telephone
        elif i == 19:
            name = db.kisi19.name
            surname = db.kisi19.surname
            gmail = db.kisi19.username
            password = db.kisi19.password
            telephone = db.kisi19.telephone
        elif i == 20:
            name = db.kisi20.name
            surname = db.kisi20.surname
            gmail = db.kisi120.username
            password = db.kisi20.password
            telephone = db.kisi20.telephone

        nameInput = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/input")
        nameInput.send_keys(name)

        time.sleep(2)

        surnameInput = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div[1]/input")
        surnameInput.send_keys(surname)

        time.sleep(2)

        mailInput = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input")
        mailInput.send_keys(gmail)

        time.sleep(2)

        passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input")
        passwordInput.send_keys(password)

        time.sleep(2)

        passwordRetyInput = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        passwordRetyInput.send_keys(password)

        time.sleep(2)

        loginBtn = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button")
        loginBtn.click()

        time.sleep(2)

        telBtn = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div/div[2]/div[1]/div/div[1]/input")
        telBtn.send_keys(telephone)