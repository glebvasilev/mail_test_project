#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gleb Vasilev"

import os
import yaml
from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from test.login_page_test import *
from test.email_page_test import *

config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../config.yml"))
