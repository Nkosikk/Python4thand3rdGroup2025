import time

import pytest

from Pages.homePage import HomePage
from utils.readProperties_data import ReadConfig_data


class Test_LoginToNdosi:
    dev_url = ReadConfig_data().getURLS()
    username = ReadConfig_data().getUsername()
    password = ReadConfig_data().getPassword()

    @pytest.mark.dev
    def test_loginToNdosiWebsite(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.verifyNdosiHeading()

        time.sleep(2)

        self.driver.quit()
