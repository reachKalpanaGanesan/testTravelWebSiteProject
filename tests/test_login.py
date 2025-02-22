from pages.index_page import IndexPage
from pages.register_page import RegisterPage
from pages.register_success_page import RegisterSuccessPage
from pages.login_page import LoginPage
from pages.login_success_page import LoginSuccessPage
from resources.constants import TEST_SITE_URL
from resources.constants import LOGIN_SUCCESS_PAGE_ASSERTION_TXT
from resources.constants import REGISTERED_SUCCESS_URL
from resources.constants import LOGIN_PAGE_URL
from resources.constants import LOGIN_SUCCESS_PAGE_URL
class TestLogin:
    # Test Case 1 :  Registering the user with a specific credentials.
    def test_register_new_user(self, driver, username_password):
        index_page = IndexPage(driver)

        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_register_button()

        register_page = RegisterPage(driver)
        register_page.wait_and_type_user_name(username_password)
        register_page.type_password(username_password)
        register_page.type_confirm_password(username_password)
        register_page.click_submit_btn()

        register_success_page = RegisterSuccessPage(driver)
        register_success_lbl = register_success_page.get_register_success_label()
        assert register_success_lbl.__contains__(username_password[0]), "User registration failed!"
    # TEST CASE 2: To check if the registered user is able to sign-in using the registered credentials.
    def test_sign_in_registered_user(self,driver, username_password):
        register_success_page = RegisterSuccessPage(driver)
        login_page = LoginPage(driver)
        # checking if the user has just registered and still in the registered success page so we can directly click and move to sign-in url.
        if register_success_page.get_current_url() == REGISTERED_SUCCESS_URL:
            register_success_page.click_login_url()
        else:
            # if user is not in registered success page, we directly load the sign-in page.
            login_page.navigate_to(LOGIN_PAGE_URL)
        # after going to sign-in url, passing the credentials and trying to sign-in.
        login_page.wait_and_type_user_name(username_password)
        login_page.type_password(username_password)
        login_page.click_submit_btn()
        # asserting if the sign-in is successful.
        login_success_page = LoginSuccessPage(driver)
        login_success_lbl = login_success_page.get_login_success_label()
        assert LOGIN_SUCCESS_PAGE_ASSERTION_TXT in login_success_lbl, "User login failed!"

    # TEST CASE 3: To check if the log-off feature is working properly.
    def test_sing_off_user(self, driver, username_password):

        login_success_page = LoginSuccessPage(driver)
        # Checking if the user is logged in
        if login_success_page.get_current_url() != LOGIN_SUCCESS_PAGE_URL:
            # Log in if user is not logged in and then doing the sign-off action.
            login_page = LoginPage(driver)
            login_page.navigate_to(LOGIN_PAGE_URL)
            login_page.wait_and_type_user_name(username_password)
            login_page.type_password(username_password)
            login_page.click_submit_btn()

        #  doing sign-off action.
        login_success_page.click_sign_off()

        # asserting if the sign-off is successful by checking the URL
        assert login_success_page.get_current_url()== TEST_SITE_URL , "User Sign-Off Failed"
