from pages.base_page import BasePage
from pages.login_page_locators import LoginPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class LoginPage(BasePage):

    def wait_and_type_user_name(self, usr_and_pw):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, LoginPageLocators.USER_NAME_TEXT_BOX).send_keys(
            usr_and_pw[0])

    def type_password(self, usr_and_pw):
        self.find_element(LoginPageLocators.PASSWORD_TEXT_BOX).send_keys(
            usr_and_pw[1])

    def click_submit_btn(self):
        self.find_element(LoginPageLocators.SUBMIT_BUTTON).click()
