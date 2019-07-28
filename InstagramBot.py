from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:   # todo change some stuff and add inputs, add functionality , then develope app

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def close_browser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(2)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # getting hashtags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                time.sleep(1)
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1


if __name__ == "__main__":

    username = "pablo_biedma"
    password = "password"

    ig = InstagramBot(username, password)
    ig.login()

    hashtags = ['fitness', 'mindfulness', 'adventure', 'photography', 'nofilter',
                'motivation', 'billywilder', 'trip', 'wanderlust', 'travel', 'travelling', 'discomfort', 'yestheory',
                'cinema', 'movies', 'technology', 'programming', 'deeplearning', 'ai', 'machinelearning', 'datascience', 'science', 'nba', 'basketball', 'okc',
                'gym', 'sports', 'music', 'guitar', 'waterpolo', 'athlete', 'ted','tedtalk','inspiration','workout','cybersecurity', 'data', 'math', 'computer', 'computerscience',
                'followforfollowback', 'follow4followback', 'like4follow', 'followbackinstantly', 'like4likes', 'likeforlikes', 'likeforlikeback', 'likeforfollow','followforlike', 'follow4like','likesforlike', 'likes4like']

    while True:
        try:
            # Choose a random hashtag
            tag = random.choice(hashtags)
            ig.like_photo(tag)

        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot("pablo_biedma", "password")
            ig.login()