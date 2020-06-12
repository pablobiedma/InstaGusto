from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter as tk
from tkinter import simpledialog
import time
import random

# author: Pablo Biedma ig: pablo_biedma


class InstagramBot:   # todo add functionality , then develop app

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
        time.sleep(4)

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
            try:
                like_button = driver.find_element_by_xpath('//*[@aria-label="Like"]').click()
                time.sleep(random.randint(1, 2))
                like_button().click()
                time.sleep(random.randint(1, 2))
            except Exception as e:
                time.sleep(2)
            unique_photos -= 1


if __name__ == "__main__":
    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    username = simpledialog.askstring(title="Username",
                                      prompt="Please enter your instagram username: ")
    password = simpledialog.askstring(title="Password",
                                      prompt="Please enter your password: ",
                                      show="*")
    #comment = "Amazingg"
    print("\nLoading Bot...")

    ig = InstagramBot(username, password)
    ig.login()

    hashtags = ["like4follow","likeforfollow", 'followforlike','follow4like', 'film', 'movies','movie', 'petersellers', 'screenplay', 'script', 'writer', 'montgomeryclift',
                'films', 'kubrick', 'FrançoisTruffaut','clinteastwood', 'billywilder', 'alfredhitchcock', 'orsonwelles', 'johnford', 'kirkdouglas', 'jacklemmon', 'laurenceoliver', 'jamesdean',
                'kurosawa', 'cameroncrowe', 'fritzlang', 'Clouzot', 'bergman', 'BibiAndersson', 'hepburn', 'jamesstewart', 'carygrant', 'marylinmonroe', 'perfectshot', 'howardhawks', 'WilliamWyler', 'dustinhoffman',
                'photography', 'filmmaking', 'filmmaker', 'rosenberg', 'CesareZavattini', 'barbarastanwyck','clarkgable', 'vintage', 'director', 'charleslaughton','stevemcqueen', 'marlendietrich',
                'hollywood', 'bettedavis', 'spencertracy', 'audreyhepburn', 'katherinhepburn', 'henryfonda', 'jamestewart', 'follow4follow'
                , 'humphreybogart', 'fredmcmurray', 'shirleymclaine', 'davidlean' ,'peterotoole','josephcotten','gregorypeck','barbarastanwyck',
                'edwardgrobinson','marlonbrando','alpacino','jamesmason','gracekelly','mankiewicz','georgesanders','annebaxter','sidneylumet','johnhuston','williamholden','maxvonsydow',
                'burtlancaster','vittoriodesica','maxophuls','joanfontaine','victorfleming', 'paulettegoddard', 'yvesmontand','rexharrison','edithhead','johnwayne',
                'maureenohara','kimnovak','marlenedietrich', 'johnlund','jamescagney','blakeedwards','waltermatthau','rossellini','frankcapra','glennford'
                , 'charliechaplin', 'busterkeaton', 'joseluisgarci', 'satyajitray', 'ernstlubitsch','franksinatra','stephanzweig', 'ottopreminger', 'garycooper', 'nataliewood', 'gretagarbo', 'paulnewman', 'robertredford', 'tonycurtis', 'jacklemmon','michaelcurtiz']

    while True:
        try:
            # Choose a random hashtag
            tag = random.choice(hashtags)
            ig.like_photo(tag)

        except Exception:
            # ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username, password)
            ig.login()
