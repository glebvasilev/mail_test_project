#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gleb Vasilev"

from pages import *


class BasicPage(object):

    def __init__(self, driver):
        if driver is None:
            raise NoDriverException(self.__module__)
        self.driver = driver
        with open(config_path, 'r') as config_file:
            self._config = yaml.safe_load(config_file)["selenium"]
        self._wait_time = 1.5

    def _wait_to_load(self):
        time.sleep(self._wait_time)

    def start(self):
        pass

