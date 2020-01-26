#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gleb Vasilev"

from pages.basic_page import *


class LoginPage(BasicPage):

    def __init__(self, driver):

        super(LoginPage, self).__init__(driver)
        self.__auth_link = 'https://passport.yandex.ru/auth/'

        # XPATH
        self.__xpath_login_box = '//input[@id="passp-field-login"]'
        self.__xpath_pass_box = '//input[@id="passp-field-passwd"]'

    def __execute(self):
        self.driver.get(self.__auth_link)
        # wait for page to load
        self._wait_to_load()
        login = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_element_located((
            By.XPATH, self.__xpath_login_box)))
        login.click()
        login.send_keys(self._config["user_name"])
        login.send_keys(Keys.ENTER)
        password = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_element_located((
            By.XPATH, self.__xpath_pass_box)))
        password.click()
        password.send_keys(self._config["user_password"])
        password.send_keys(Keys.ENTER)
        # wait for page to load
        self._wait_to_load()

    def start(self):
        self.__execute()


