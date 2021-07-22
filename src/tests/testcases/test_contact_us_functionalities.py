import unittest
import pytest
from pages.main_page import MainPage


@pytest.mark.usefixtures("chrome_driver_init")
class TestCaseContactUsFunctionalities(unittest.TestCase):

    def setUp(self) -> None:
        self.driver.maximize_window()
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.set_page_load_timeout(10)

    def test_submit_fulfilled_form(self):
        main_page = MainPage(self.driver)
        contact_page = main_page.go_to_contact_us_page()
        contact_page.fulfill_form(email="test@test.com",
                                  id_order="123",
                                  message="Automated Test")
        contact_page.click_send()
        assert contact_page.is_submitted_form(), "The contact form was not submitted!"

    def test_submit_form_with_empty_subject(self):
        main_page = MainPage(self.driver)
        contact_page = main_page.go_to_contact_us_page()
        contact_page.fulfill_form(subject_index=0,
                                  email="test@test.com",
                                  message="Automated Test")
        contact_page.click_send()
        assert contact_page.is_displayed_alert_validation(), "The subject field required validation failed!"

    def test_submit_form_with_empty_email(self):
        main_page = MainPage(self.driver)
        contact_page = main_page.go_to_contact_us_page()
        contact_page.fulfill_form(message="Automated Test")
        contact_page.click_send()
        assert contact_page.is_displayed_alert_validation(), "The email field required validation failed!"

    def test_submit_form_with_invalid_email(self):
        main_page = MainPage(self.driver)
        contact_page = main_page.go_to_contact_us_page()
        contact_page.fulfill_form(email="test@.com", message="Automated Test")
        contact_page.click_send()
        assert contact_page.is_displayed_alert_validation(), "The email field required validation failed!"

    def test_submit_form_with_empty_message(self):
        main_page = MainPage(self.driver)
        contact_page = main_page.go_to_contact_us_page()
        contact_page.fulfill_form(email="test@test.com")
        contact_page.click_send()
        assert contact_page.is_displayed_alert_validation(), "The message field required validation failed!"
