from selenium import webdriver
from time import sleep


from selenium.webdriver.chrome.options import Options
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

class InstaBot():
    def __init__(self):
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def start(self):
        self.driver.get('https://instagram.com')

    def login(self):

        sleep(4)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('')

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys('')

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        sleep(5)

        popup_3 = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        popup_3.click()

        sleep(5)

    def like(self):
        like_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()
        print('liked')

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()
        print('disliked')

    def auto_swipe(self):
        while True:
            sleep(2)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        sleep(3)
        popup_3 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
    
    def clickMatch(self):

        for a in range(2, 100):
            
            str(a)
            btn = self.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[1]/div[' + a + '2]/a')
            btn.click()

            sleep(3)

            textBox = self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
            testBox.send_keys('Hola ')
            sendButton = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
            sendButton.click()



    def chat(self):
        while True:
            try:
                sleep(2)
                self.clickMatch()
            except Exception:
                try:
                    print(self.driver.window_handles)
                except Exception:
                    print(self.driver.window_handles[1])

bot = InstaBot()
bot.close_popup()
