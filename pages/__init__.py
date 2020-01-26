#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gleb Vasilev"

from selenium import webdriver
import unittest
import os
import yaml
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from exceptions.custom_exceptions import *
from selenium.common.exceptions import TimeoutException

config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../config.yml"))
