import time
import kullaniciBilgileri as kb

from selenium import webdriver

class Browser:
    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Chrome()
        Browser.goYoutube(self)

    def goYoutube(self):
        self.browser.get(self.link)
        time.sleep(2)
        Browser.login(self)

    def login(self):
        loginBtn = self.browser.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a")
        loginBtn.click()

        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
        usernameInput.send_keys(kb.username)

        time.sleep(2)

        passwordLoginBtn = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div")
        passwordLoginBtn.click()

        time.sleep(2)

        passwordInput = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        passwordInput.send_keys(kb.password)

        time.sleep(2)

        aloginBtn = self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div")
        aloginBtn.click()

        time.sleep(2)

        self.browser.get("https://www.youtube.com/channel/UCasjj7rytWWY8Cf6jrEsCfA")

        time.sleep(1)

        playAllVideosBtn = self.browser.find_element_by_css_selector("#play-button")
        playAllVideosBtn.click()

        time.sleep(2)

        for i in range(11):
            numb = i * 1080
            self.browser.execute_script(f"window.scrollTo(0, {numb});")

        time.sleep(2)

        commentInput = self.browser.find_element_by_css_selector("#placeholder-area")
        commentInput.click()

        time.sleep(2)

        sendCommentInput = self.browser.find_element_by_css_selector("#contenteditable-root")
        sendCommentInput.send_keys(kb.random.choice(kb.yorumliste))

        time.sleep(1)

        sendCommentBtn = self.browser.find_element_by_css_selector("#submit-button")
        sendCommentBtn.click()

        time.sleep(2)

        self.browser.get("https://www.youtube.com/logout")

