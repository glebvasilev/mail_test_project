#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gleb Vasilev"

from test.basic_page_test import *
from pages.login_page import *


class LoginPageTest(BasicPageTest):

    def run(self):
        login_page_obj = LoginPage(self.driver)
        login_page_obj.start()
