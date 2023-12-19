from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    first_name_id = "input-firstname"
    last_name_id = "input-lastname"
    email_address_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_checkbox_field_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//input[@name='newsletter'][@value = '1']"
    duplicate_email_warning_message_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_field_warning_message_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_field_warning_message_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_field_warning_message_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_field_warning_message_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_field_warning_message_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name_text):
        self.driver.find_element(By.ID, self.first_name_id).click()
        self.driver.find_element(By.ID, self.first_name_id).clear()
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name_text)

    def enter_last_name(self, last_name_text):
        self.driver.find_element(By.ID, self.last_name_id).click()
        self.driver.find_element(By.ID, self.last_name_id).clear()
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name_text)

    def enter_email(self, email_text):
        self.driver.find_element(By.ID, self.email_address_field_id).click()
        self.driver.find_element(By.ID, self.email_address_field_id).clear()
        self.driver.find_element(By.ID, self.email_address_field_id).send_keys(email_text)

    def enter_telephone(self, telephone_text):
        self.driver.find_element(By.ID, self.telephone_field_id).click()
        self.driver.find_element(By.ID, self.telephone_field_id).clear()
        self.driver.find_element(By.ID, self.telephone_field_id).send_keys(telephone_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def enter_password_confirm(self, confirmed_password_text):
        self.driver.find_element(By.ID, self.confirm_password_field_id).click()
        self.driver.find_element(By.ID, self.confirm_password_field_id).clear()
        self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(confirmed_password_text)

    def select_agree_checkbox_field(self):
        self.driver.find_element(By.XPATH, self.agree_checkbox_field_xpath).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def select_yes_radio_button(self):
        self.driver.find_element(By.XPATH, self.yes_radio_button_xpath).click()

    def retrieve_duplicate_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.duplicate_email_warning_message_xpath).text

    def retrieve_privacy_warning_message(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_warning_xpath).text

    def retrieve_first_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.first_name_field_warning_message_xpath).text

    def retrieve_last_name_warning_message(self):
        return self.driver.find_element(By.XPATH, self.last_name_field_warning_message_xpath).text

    def retrieve_email_warning_message(self):
        return self.driver.find_element(By.XPATH, self.email_field_warning_message_xpath).text

    def retrieve_telephone_warning_message(self):
        return self.driver.find_element(By.XPATH, self.telephone_field_warning_message_xpath).text

    def retrieve_password_warning_message(self):
        return self.driver.find_element(By.XPATH, self.password_field_warning_message_xpath).text