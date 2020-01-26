#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gleb Vasilev"

from exceptions import *


class NoDriverException(Exception):
    def __init__(self, message):
        super(NoDriverException, self).__init__("No Selenium driver provided for testing in: {}".format(message))


class ElementIsMissingException(TimeoutException):
    def __init__(self, message):
        super(ElementIsMissingException, self).__init__("PLEASE MAKE SURE PAGE HAS LOADED! "
                                                        "Selenium could not find element on page in time: {}".
                                                        format(message))
