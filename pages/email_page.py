#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gleb Vasilev"

from pages.basic_page import *


class EmailPage(BasicPage):

    def __init__(self, driver):

        super(EmailPage, self).__init__(driver)
        self.__mailbox_link = 'https://mail.yandex.ru/?uid=24934419#inbox'
        self.__email_search_string = 'FROM: Gleb Vasilev'
        self.__email_flags_box = '_nb-checkbox-label'  # flag to find unread emails
        self.__sample_response = 'Тестовое задание. Глеб Василев. Найдено писем: {}'

        # CSS
        self.__email_finder_box_css = 'input.textinput__control'    # search box for email senders
        self.__quick_reply_box_css = '.mail-QuickReply-Placeholder_text'
        # XPATH
        self.__response_text_box_xpath = '//div[@placeholder="Введите сообщение"]'
        self.__send_button_xpath = '//span[text()="Отправить"]'

    def __execute(self):
        # go to emails page
        self.driver.get(self.__mailbox_link)
        # looking for search box
        search_box = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_element_located((
            By.CSS_SELECTOR, self.__email_finder_box_css)))
        search_box.click()
        # input the email sender
        search_box.send_keys(self.__email_search_string)
        search_box.send_keys(Keys.DOWN, Keys.ENTER)
        # wait for page to load
        self._wait_to_load()
        # count number of new emails
        num_emails = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_all_elements_located((
            By.CLASS_NAME, self.__email_flags_box)))
        # for number of unread emails
        emails_num = 0
        # count the number of unread emails
        for _ in num_emails:
            emails_num = emails_num + 1
        # find email sender
        search_email = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_element_located((
            By.CSS_SELECTOR, self.__email_finder_box_css)))
        search_email.click()
        search_email.send_keys(Keys.DOWN, Keys.DOWN, Keys.ENTER)
        # wait for page to load
        self._wait_to_load()
        # working with response field
        try:
            reply_box = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_element_located((
                By.CSS_SELECTOR, self.__quick_reply_box_css)))
            reply_box.click()
            # wait for page to load
            self._wait_to_load()
            # find response text box
            text_box = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_element_located((
                By.XPATH, self.__response_text_box_xpath)))
            text_box.click()
        except TimeoutException as err:
            raise ElementIsMissingException(err)
        # write response
        text_box.send_keys(self.__sample_response.format(emails_num))
        # press response button
        send_button = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_element_located((
            By.XPATH, self.__send_button_xpath)))
        send_button.click()
        # wait for page to load
        self._wait_to_load()

    def start(self):
        self.__execute()
