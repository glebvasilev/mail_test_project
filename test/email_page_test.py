#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gleb Vasilev"

from test.basic_page_test import *
from pages.email_page import *


class EmailPageTest(BasicPageTest):

    def run(self):
        email_page_obj = EmailPage(self.driver)
        email_page_obj.start()
