#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gleb Vasilev"

from test import *


class MailTask(unittest.TestCase):

    def setUp(self):
        with open(config_path, 'r') as config_file:
            self._config = yaml.safe_load(config_file)["selenium"]

        self.driver = webdriver.Chrome(self._config["driver_path"])

    def testRun(self):
        LoginPageTest(self.driver).run()
        EmailPageTest(self.driver).run()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()


