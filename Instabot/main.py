from selenium import webdriver
from time import sleep

from credentials import username, password

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

        sleep(2)

        # # switch to login popup
        # base_window = self.driver.window_handles[0]
        # self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')
        login_btn.click()

        sleep(5)

        profile_icon_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span')
        profile_icon_btn.click()


        profile_btn = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")
        profile_btn.click()

        sleep(5)

        #go to your followers
        followers_btn = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers_btn.click()

        sleep(5)

        #go to your first follower (or change 'Li[]' value to whatever you want)
        followers_btn2 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[5]/div/div[2]/div[1]/div/div/span/a')
        followers_btn2.click()

        sleep(5)

        #save the number of followers they have to variable
        elem = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span')
        followerCount = elem.get_attribute('innerHTML')
        #replace ',' in followers greater than 1000 eg 1,000 = 1000
        if ',' in followerCount:
            followerCount = followerCount.replace(',', '')
            
        followerCountInt = int(followerCount)

        #bring up their followers and start following everyone
        followers_btn3 = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers_btn3.click()

        sleep(2)

        for i in range(2, followerCountInt):

            try:
                buttonString = '/html/body/div[5]/div/div/div[2]/ul/div/li[' + str(i) + ']/div/div[3]/button'
                #scrollIntoView
                # element = self.driver.find_element_by_xpath(buttonString)
                # self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
                #pressfollow
                followers_btn4 = self.driver.find_element_by_xpath(buttonString)
                followers_btn4.click()
                sleep(0.4)
                #close unfollow window if you click someone you already follow
                try:
                    x = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                    x.click()
                except:
                    print("error clicking off unfollow popup")
            except:
                print("error with button ::: " + buttonString)

            sleep(1)




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



bot = InstaBot()
bot.start()
bot.close_popup()
bot.login()