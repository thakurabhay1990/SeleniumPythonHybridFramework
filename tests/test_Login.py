from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("amotooricap9@gmail.com")
        login_page.enter_password("1234")
        login_page.click_on_login_button()
        account_page = AccountPage(self.driver)
        assert account_page.display_status_of_edit_your_account_information_option()

    def test_login_with_invalid_email_and_valid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address(self.generate_email_with_time_stamp())
        login_page.enter_password("12345")
        login_page.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_password(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("amotooricap1@gmail.com")
        login_page.enter_password("123456")
        login_page.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_entering_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("")
        login_page.enter_password("")
        login_page.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "amotooricap" + time_stamp + "@gmail.com"